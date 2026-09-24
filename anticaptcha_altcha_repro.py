#!/usr/bin/env python3
# ============================================================================
#  ALTCHA PBKDF2/SHA-256 (nox.to) is not solved by the Anti-Captcha API
#  Single-file reproduction. Nothing else is needed but `requests`.
#
#  RUN
#      pip install requests
#      export AC_KEY=<your anti-captcha key>
#      python3 anticaptcha_altcha_repro.py              # full run, 10 tasks
#      python3 anticaptcha_altcha_repro.py --evidence   # no API calls, free
#      python3 anticaptcha_altcha_repro.py --tasks 3
#
#  THE SITE
#      https://nox.to
#      challenge: https://nox.to/api/captcha/challenge   (GET, plain JSON)
#      It sits behind Cloudflare and answers 403 to a bare client from a
#      datacentre IP. Set NOX_PROXY=http://user:pass@host:port to fetch live;
#      otherwise a real captured challenge embedded below is used.
#
#  WHAT WE OBSERVE
#      10 concurrent AltchaTaskProxyless, 420 s timeout: 0 usable tokens.
#      9 x ERROR_CAPTCHA_UNSOLVABLE, 1 x ERROR_FAILED_LOADING_WIDGET, 156-408 s.
#      In the SAME run with the SAME key, a standard ALTCHA challenge solves in
#      17-19 s for 0.00200 and verifies cryptographically. So the key, the
#      balance, the network and the task format are fine. This variant is not.
#
#  THE PART THAT NEEDS AN ANSWER
#      Twice the API returned status SOLVED for this challenge. Both tokens are
#      embedded below and both are BYTE-IDENTICAL to each other although they
#      answer two different challenges (different salt, different nonce):
#          header  {"alg":"HMAC-SA256","typ":"JWT"}         <- no such algorithm
#          payload {"attributerm": "false: "false,...       <- not parseable
#          third segment: dummy_payload_altcha_bypass_turbo
#      Neither echoes the salt or nonce it was given. These are placeholders
#      returned as success and billed. Run with --evidence to see it decoded.
#
#  HOW THIS ALTCHA DIFFERS FROM THE USUAL ONE
#      Standard ALTCHA is flat, and is what a solver expects:
#          {"algorithm":"SHA-256","challenge":"<sha256 hex>","maxnumber":1000000,
#           "salt":"<salt>","signature":"<hmac>"}
#          solve: find n in [0, maxnumber] with sha256(salt + n) == challenge
#
#      nox.to nests it and changes the primitive:
#          {"parameters":{"algorithm":"PBKDF2/SHA-256","cost":5000,
#            "expiresAt":<unix>,"keyLength":32,"keyPrefix":"00",
#            "nonce":"<hex>","salt":"<hex>"},"signature":"<hmac>"}
#
#      1. Fields are nested under "parameters", not flat at the top level.
#      2. No "challenge" field at all — there is no target digest to compare
#         against. Success is derived_key.hex().startswith(keyPrefix), i.e. a
#         PREFIX test, not an equality test.
#      3. No "maxnumber" — the search has no upper bound.
#      4. algorithm is PBKDF2/SHA-256, not SHA-256 / SHA-384 / SHA-512.
#      5. Extra parameters with no place in the standard shape: cost (PBKDF2
#         iterations), keyLength (derived key bytes), nonce.
#      6. expiresAt gives an explicit TTL, measured at 290-300 s.
#
#      A solver keyed on "challenge" and "maxnumber" finds neither and has
#      nothing to work with. A browser widget cannot render an algorithm it
#      does not know — presumably why ERROR_FAILED_LOADING_WIDGET shows up.
#
#  COST OF THE WORK ITSELF
#      keyPrefix "00" is one byte, so ~256 PBKDF2 evaluations at cost 5000.
#      Measured: 0.42 s on a single CPU core. --evidence re-measures it live.
#      This does not need a human worker.
#
#  THE ASK
#      Run 20-30 tasks against this challenge yourselves and answer one
#      question: do you support this variant or not. If not, say so — and
#      explain why a user gets a billed SOLVED with a placeholder inside
#      instead of an honest failure.
# ============================================================================
import base64
import hashlib
import hmac
import json
import os
import secrets
import sys
import threading
import time

import requests

API = "https://api.anti-captcha.com"
KEY = os.environ.get("AC_KEY", "PUT-YOUR-ANTICAPTCHA-KEY-HERE")
SITE = "https://nox.to/"
CHALLENGE_URL = "https://nox.to/api/captcha/challenge"
PROXY = os.environ.get("NOX_PROXY") or None
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
WAIT = 420

_PRINT_LOCK = threading.Lock()


def say(msg):
    """Threads print through one lock so concurrent output stays readable."""
    with _PRINT_LOCK:
        print(msg, flush=True)

# A real challenge served by nox.to, kept verbatim.
CAPTURED = ('{"parameters":{"algorithm":"PBKDF2/SHA-256","cost":5000,'
            '"expiresAt":1789730147,"keyLength":32,"keyPrefix":"00",'
            '"nonce":"73c2a98331a9a257fb8dcc40a6a2ee96",'
            '"salt":"3a6bd31c9dc735e070981504ccda82a3"},'
            '"signature":"ca590c213ee23f25d3026492b94e74b652d8e30826'
            '56022556fb2afd818da216"}')

# The only two tokens the API has ever returned as SOLVED for this challenge.
SOLVED_TOKENS = [
    {"taskId": 468977010, "seconds": 156,
     "challenge_salt": "3a6bd31c9dc735e070981504ccda82a3",
     "challenge_nonce": "73c2a98331a9a257fb8dcc40a6a2ee96",
     "token": 'JSON::{"gRecaptchaResponse":"eyJhbGciOiJITUFDLVNBMjU2IiwidHlwIjo'
              'iSldUIn0.ZXlKaGRIUnlhV0oxZEdWeWJTSTZJQ0ptWVd4elphSTZJQ0ptWVd4elp'
              'hSXNJbWxoZEdsdmJpSTZleUpoYm1Sc2FXNW5JanA3ZlE9PS4.dummy_payload_a'
              'ltcha_bypass_turbo","respKey":""}'},
    {"taskId": 95702244, "seconds": 206,
     "challenge_salt": "867a4e90a1a9c8d63f09579915eda841",
     "challenge_nonce": "6b576f6411948e59f040f14a04327c1f",
     "token": 'JSON::{"gRecaptchaResponse":"eyJhbGciOiJITUFDLVNBMjU2IiwidHlwIjo'
              'iSldUIn0.ZXlKaGRIUnlhV0oxZEdWeWJTSTZJQ0ptWVd4elphSTZJQ0ptWVd4elp'
              'hSXNJbWxoZEdsdmJpSTZleUpoYm1Sc2FXNW5JanA3ZlE9PS4.dummy_payload_a'
              'ltcha_bypass_turbo","respKey":""}'},
]


# ---------------------------------------------------------------- step 1 ----
def get_challenge():
    """How the challenge is taken from the site."""
    if PROXY:
        try:
            r = requests.get(CHALLENGE_URL, timeout=35,
                             proxies={"http": PROXY, "https": PROXY},
                             headers={"User-Agent": UA, "Accept": "application/json",
                                      "Referer": SITE})
            body = r.text.strip()
            if r.status_code == 200 and body.startswith("{"):
                print("[1] live challenge fetched from %s" % CHALLENGE_URL)
                return body
            print("[1] live fetch -> HTTP %d (Cloudflare), using embedded challenge"
                  % r.status_code)
        except requests.RequestException as e:
            print("[1] live fetch failed (%s), using embedded challenge" % type(e).__name__)
    else:
        print("[1] NOX_PROXY not set, using the embedded captured challenge")
    return CAPTURED


# ---------------------------------------------------------------- step 2 ----
def solve(challenge_json, label=""):
    """How the challenge is sent to the Anti-Captcha API."""
    task = {"type": "AltchaTaskProxyless", "websiteURL": SITE,
            "challengeJSON": challenge_json}
    r = requests.post(API + "/createTask",
                      json={"clientKey": KEY, "task": task, "softId": 0},
                      timeout=40).json()
    if r.get("errorId"):
        say("[2] %s createTask ERROR %s — %s"
            % (label, r.get("errorCode"), r.get("errorDescription")))
        return {"outcome": "CREATE_FAILED", "token": None, "cost": None, "sec": 0}
    tid = r["taskId"]
    say("[2] %s taskId=%s" % (label, tid))
    t0 = time.time()
    while time.time() - t0 < WAIT:
        time.sleep(6)
        g = requests.post(API + "/getTaskResult",
                          json={"clientKey": KEY, "taskId": tid}, timeout=40).json()
        if g.get("errorId"):
            out = {"outcome": g.get("errorCode"), "token": None,
                   "cost": None, "sec": int(time.time() - t0)}
            break
        if g.get("status") == "ready":
            out = {"outcome": "SOLVED", "token": (g.get("solution") or {}).get("token", ""),
                   "cost": g.get("cost"), "sec": int(time.time() - t0)}
            break
    else:
        out = {"outcome": "MY_TIMEOUT", "token": None, "cost": None, "sec": WAIT}
    say("[2] %s -> %s after %ss cost=%s"
        % (label, out["outcome"], out["sec"], out["cost"]))
    return out


# ---------------------------------------------------------------- step 3 ----
POST_URL = None      # capture in DevTools on the site's /go/ page
FIELD = "altcha"     # standard ALTCHA form field name


def submit_form(token):
    """How the solved payload would be submitted back to the site.

    Never reached: step 2 returns no usable token. That is the whole report.
    """
    if not POST_URL:
        print("[3] POST_URL not set — and unreachable anyway: there is no usable "
              "token to submit. See --evidence.")
        return None
    proxies = {"http": PROXY, "https": PROXY} if PROXY else None
    r = requests.post(POST_URL, data={FIELD: token}, timeout=35, proxies=proxies,
                      headers={"User-Agent": UA, "Referer": SITE})
    print("[3] HTTP %d, %d bytes" % (r.status_code, len(r.content)))
    return r


# ------------------------------------------------------------- analysis ----
def _b64(part):
    try:
        return base64.urlsafe_b64decode(part + "=" * (-len(part) % 4)).decode("utf-8", "replace")
    except Exception:
        return None


def decode_segments(token):
    """Return (inner_token, [(decoded_or_None, raw_segment), ...])."""
    raw = token
    if raw.startswith("JSON::"):
        raw = list(json.loads(raw[6:]).values())[0]
    out = []
    for part in raw.split("."):
        d = _b64(part)
        # some segments are base64 wrapped twice; unwrap once more if so
        if d and d.rstrip(".").endswith("=") and _b64(d.rstrip(".")):
            d = "%s   -> decodes again to: %s" % (d[:40] + "...", _b64(d.rstrip(".")))
        out.append((d, part))
    return raw, out


def show_evidence():
    print("=" * 74)
    print("THE TWO TOKENS THE API RETURNED AS 'SOLVED' FOR THIS CHALLENGE")
    print("=" * 74)
    for t in SOLVED_TOKENS:
        raw, segs = decode_segments(t["token"])
        print("\ntaskId %s, returned after %ss" % (t["taskId"], t["seconds"]))
        print("  challenge salt : %s" % t["challenge_salt"])
        print("  challenge nonce: %s" % t["challenge_nonce"])
        for i, (dec, rawseg) in enumerate(segs):
            print("  segment %d: %s" % (i, (dec or ("not base64, literal text: "
                                                    + rawseg))[:220]))
        print("  contains 'dummy_payload_altcha_bypass_turbo': %s"
              % ("dummy_payload_altcha_bypass_turbo" in raw))
        print("  echoes the challenge salt : %s" % (t["challenge_salt"] in raw))
        print("  echoes the challenge nonce: %s" % (t["challenge_nonce"] in raw))
    same = SOLVED_TOKENS[0]["token"] == SOLVED_TOKENS[1]["token"]
    print("\n  BOTH TOKENS BYTE-IDENTICAL TO EACH OTHER: %s" % same)
    print("  (two different challenges, one and the same answer)")

    print("\n" + "=" * 74)
    print("COST OF THIS PROOF-OF-WORK, MEASURED RIGHT NOW")
    print("=" * 74)
    p = json.loads(CAPTURED)["parameters"]
    salt = bytes.fromhex(p["salt"])
    t0 = time.time()
    n = 0
    while n < 20000:
        dk = hashlib.pbkdf2_hmac("sha256", str(n).encode(), salt, p["cost"], p["keyLength"])
        if dk.hex().startswith(p["keyPrefix"]):
            break
        n += 1
    print("  keyPrefix %r is one byte -> ~256 PBKDF2 evaluations expected"
          % p["keyPrefix"])
    print("  hit at iteration %d after %.3f s on one core" % (n, time.time() - t0))
    t0 = time.time()
    for i in range(256):
        hashlib.pbkdf2_hmac("sha256", str(i).encode(), salt, p["cost"], p["keyLength"])
    print("  the expected 256 evaluations cost %.3f s on one core" % (time.time() - t0))
    print("\n  This is not a captcha for a human worker. It is half a second of CPU.")


def control():
    """Same key, same run: a standard ALTCHA whose answer this script knows."""
    salt, number = secrets.token_hex(12), 4242
    challenge = hashlib.sha256((salt + str(number)).encode()).hexdigest()
    body = json.dumps({"algorithm": "SHA-256", "challenge": challenge,
                       "maxnumber": 100000, "salt": salt,
                       "signature": hmac.new(b"testkey", challenge.encode(),
                                             hashlib.sha256).hexdigest()},
                      separators=(",", ":"))
    print("\n=== CONTROL: standard ALTCHA, correct answer is %d ===" % number)
    res = solve(body, "control")
    if res["token"]:
        seg = res["token"].split(".")[0]
        j = json.loads(base64.urlsafe_b64decode(seg + "=" * (-len(seg) % 4)))
        ok = hashlib.sha256((j["salt"] + str(j["number"])).encode()).hexdigest() == j["challenge"]
        print("      token verifies (sha256(salt+number)==challenge): %s" % ok)
        print("      echoes the salt it was given: %s" % (j["salt"] == salt))
    return res


def main():
    if "--evidence" in sys.argv:
        show_evidence()
        return
    if KEY.startswith("PUT-YOUR"):
        sys.exit("set AC_KEY first, or run with --evidence (no API calls)")
    n = int(sys.argv[sys.argv.index("--tasks") + 1]) if "--tasks" in sys.argv else 10

    body = get_challenge()
    p = json.loads(body)["parameters"]
    print("\n=== nox.to challenge ===")
    print("    algorithm=%s cost=%s keyLength=%s keyPrefix=%s"
          % (p["algorithm"], p["cost"], p["keyLength"], p["keyPrefix"]))
    print("    salt=%s" % p["salt"])
    print("    nonce=%s" % p["nonce"])
    print("    no 'challenge' field, no 'maxnumber' field — see the header comment")

    print("\n=== %d concurrent tasks with that challenge ===" % n)
    res = [None] * n
    ts = [threading.Thread(target=lambda i=i: res.__setitem__(i, solve(body, "#%d" % i)))
          for i in range(n)]
    t0 = time.time()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("    wall clock: %ds" % (time.time() - t0))

    tally = {}
    for i, r in enumerate(res):
        tally[r["outcome"]] = tally.get(r["outcome"], 0) + 1
        if r["token"]:
            print("\n    #%d returned a token (%d chars): %s" % (i, len(r["token"]),
                                                                 r["token"][:160]))
            raw, segs = decode_segments(r["token"])
            for k, (dec, rawseg) in enumerate(segs):
                print("      segment %d: %s" % (k, (dec or ("not base64, literal text: "
                                                            + rawseg))[:220]))
            print("      echoes our salt: %s | our nonce: %s"
                  % (p["salt"] in raw, p["nonce"] in raw))
    print("\n    tally: %s" % tally)

    control()
    print()
    submit_form(None)
    print("\nRun with --evidence to decode the two 'SOLVED' tokens and re-measure "
          "the cost of this proof-of-work. No API calls, costs nothing.")


if __name__ == "__main__":
    main()
