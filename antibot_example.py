from anticaptchaofficial.antibotcookietask import *
import requests

solver = antibotcookieTask()
solver.set_verbose(1)
solver.set_key("API_KEY_HERE")
solver.set_website_url("https://www.somewebsite.com/")
solver.set_proxy_address("1.2.3.4")
solver.set_proxy_port(3128)
solver.set_proxy_login("login")
solver.set_proxy_password("password")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

result = solver.solve_and_return_solution()
if result == 0:
    print("could not solve task")
    exit()

print(result)

cookies, localStorage, fingerprint = result["cookies"], result["localStorage"], result["fingerprint"]

if len(cookies) == 0:
    print("empty cookies, try again")
    exit()

cookie_string = '; '.join([f'{key}={value}' for key, value in cookies.items()])
user_agent = fingerprint['self.navigator.userAgent']
print(f"use these cookies for requests: {cookie_string}")
print(f"use this user-agent for requests: {user_agent}")

s = requests.Session()
proxies = {
  "http": "http://login:password@1.2.3.4:3128",
  "https": "http://login:password@1.2.3.4:3128"
}
s.proxies = proxies

content = s.get("https://www.somewebsite.com/", headers={
    "Cookie": cookie_string,
    "User-Agent": user_agent
}).text
print(content)

