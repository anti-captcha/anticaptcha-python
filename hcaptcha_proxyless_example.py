from anticaptchaofficial.hcaptchaproxyless import *

# Non-Enterprise version
solver = hCaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_user_agent("YOUR FULL USER AGENT HERE")

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
else:
    print("task finished with error "+solver.error_code)


# Enterprise version
solver = hCaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_user_agent("YOUR FULL USER AGENT HERE")
solver.set_enterprise_payload({
    "rqdata": "rq data value from target website",
    "sentry": True,
    # ... etc, see https://anti-captcha.com/apidoc/task-types/HCaptchaTaskProxyless for more
})

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
else:
    print("task finished with error "+solver.error_code)
