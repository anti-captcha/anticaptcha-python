anticaptchaofficial
===================

Official https://anti-captcha.com/ library for solving images with text, Recaptcha v2/v3 Enterprise or non-Enterprise, Funcaptcha Arcoselabs, GeeTest and hCaptcha Enterprise or non-Enterprise.
Anti-Captcha is the most popular and reliable captcha solving service, working since 2007.
Prices for solving captchas start from $0.0005 per item.

```bash
pip3 install anticaptchaofficial
```

&nbsp;
Check API key balance before creating tasks:
```python
balance = solver.get_balance()
if balance <= 0:
    print("too low balance!")
    return
```
&nbsp;
<br>
Check subscription credits balance if you have one:
```python
credits = solver.get_credits_balance()
if credits <= 0:
    print("too low credits balance!")
    return
```
&nbsp;

Example how to create [Recaptcha V2](https://anti-captcha.com/apidoc/task-types/RecaptchaV2TaskProxyless) task and receive g-response:

```python
from anticaptchaofficial.recaptchav2proxyless import *

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

# Set True if it is Recaptcha V2-invisible
#solver.set_is_invisible(True)

# Set data-s value for google.com pages
#solver.set_data_s('a_long_string_here')

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print "g-response: "+g_response
else:
    print "task finished with error "+solver.error_code
```
Report previosly solved Recaptcha V2/V3/Enterprise as incorrect:
```python
solver.report_incorrect_recaptcha()
```
Report it as correct to improve your quality:
```python
solver.report_correct_recaptcha()
```
___

&nbsp;

Solve [image captcha](https://anti-captcha.com/apidoc/task-types/ImageToTextTask):

```python
from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

captcha_text = solver.solve_and_return_solution("captcha.jpeg")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)
```
Report previosly solved image captcha as incorrect:
```python
solver.report_incorrect_image_captcha()
```
___

&nbsp;

Solve [HCaptcha](https://anti-captcha.com/apidoc/task-types/HCaptchaTask):

```python
from anticaptchaofficial.hcaptchaproxyless import *

solver = hCaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_user_agent("YOUR FULL USER AGENT HERE")

# tell API that Hcaptcha is invisible
#solver.set_is_invisible(1)

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
    # use this user-agent to make requests to your target website
    print("user-agent: "+solver.get_user_agent())
    print("respkey, if any: ", solver.get_respkey())
else:
    print("task finished with error "+solver.error_code)
```
Report previosly solved Hcaptcha as incorrect:
```python
solver.report_incorrect_hcaptcha()
```
___
&nbsp;

Solve [Funcaptcha](https://anti-captcha.com/apidoc/task-types/FunCaptchaTaskProxyless) (Arkoselabs):

```python
from anticaptchaofficial.funcaptchaproxyless import *

solver = funcaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX")

token = solver.solve_and_return_solution()
if token != 0:
    print("result token: "+token)
else:
    print("task finished with error "+solver.error_code)
```
___

&nbsp;

Solve [GeeTest](https://anti-captcha.com/apidoc/task-types/GeeTestTask) captcha:

```python
from anticaptchaofficial.geetestproxyless import *

solver = geetestProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://address.com")
solver.set_gt_key("CONSTANT_GT_KEY")
solver.set_challenge_key("VARIABLE_CHALLENGE_KEY")
token = solver.solve_and_return_solution()
if token != 0:
    print("result tokens: ")
    print(token)
else:
    print("task finished with error "+solver.error_code)
```
___

&nbsp;

Solve [GeeTest v4](https://anti-captcha.com/apidoc/task-types/GeeTestTask) captcha:

```python
from anticaptchaofficial.geetestproxyless import *

solver = geetestProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://address.com")
solver.set_version(4)
solver.set_init_parameters({"riskType": "slide"})
token = solver.solve_and_return_solution()
if token != 0:
    print("result tokens: ")
    print(token)
else:
    print("task finished with error "+solver.error_code)
```
___


&nbsp;

Solve [HCaptcha Enterprise](https://anti-captcha.com/apidoc/task-types/HCaptchaTask):

```python
from anticaptchaofficial.hcaptchaproxyless import *

solver = hCaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_user_agent("YOUR FULL USER AGENT HERE")

# tell API that Hcaptcha is invisible
#solver.set_is_invisible(1)

# tell API that Hcaptcha is Enterprise
#solver.set_is_enterprise(1)

# set here optional Enterprise parameters like rqdata, sentry, apiEndpoint, endpoint, reportapi, assethost, imghost
solver.set_enterprise_payload({
    "rqdata": "rq data value from target website",
    "sentry": True
})

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
    # use this user-agent to make requests to your target website
    print("user-agent, use it to post the form: ", solver.get_user_agent())
    print("respkey, if any: ", solver.get_respkey())
else:
    print("task finished with error "+solver.error_code)
```
___

&nbsp;

Example how to create [Turnstile](https://anti-captcha.com/apidoc/task-types/TurnstileTaskProxyless) task and receive a token:

```python
from anticaptchaofficial.turnstileproxyless import *

solver = turnstileProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

# Optionally specify page action
solver.set_action("login")

# Optionally specify cData token
solver.set_action("some_custom_token")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

token = solver.solve_and_return_solution()
if token != 0:
    print "token: "+token
else:
    print "task finished with error "+solver.error_code
```
___

&nbsp;

Solve [AntiGate](https://anti-captcha.com/apidoc/task-types/AntiGateTask) task:

```python
from anticaptchaofficial.antigatetask import *

solver = antigateTask()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("http://antigate.com/logintest.php")
solver.set_template_name("Sign-in and wait for control text")
solver.set_variables({
    "login_input_css": "#login",
    "login_input_value": "test login",
    "password_input_css": "#password",
    "password_input_value": "test password",
    "control_text": "You have been logged successfully"
})

result  = solver.solve_and_return_solution()
if result != 0:
    cookies, localStorage, fingerprint, url, domain = result["cookies"], result["localStorage"], result["fingerprint"], result["url"], result["domain"]
    print("cookies: ", cookies)
    print("localStorage: ", localStorage)
    print("fingerprint: ", fingerprint)
    print("url: "+url)
    print("domain: "+domain)
else:
    print("task finished with error "+solver.error_code)
```
___

&nbsp;

Solve [AntiBotCookieTask](https://anti-captcha.com/apidoc/task-types/AntiBotCookieTask) task to bypass Cloudflare, Datadome and others:

```python
from anticaptchaofficial.antibotcookietask import *

solver = antibotcookieTask()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://www.somewebsite.com/")
solver.set_proxy_address("1.2.3.4")
solver.set_proxy_port(3128)
solver.set_proxy_login("login")
solver.set_proxy_password("password")

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
```
___

&nbsp;

Get [object coordinates](https://anti-captcha.com/apidoc/task-types/ImageCoordinatesTask) in an image:

```python
from anticaptchaofficial.imagetocoordinates import *

solver = imagetocoordinates()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_mode("points")
solver.set_comment("Select in specified order")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

coordinates = solver.solve_and_return_solution("coordinates.png")
if coordinates != 0:
    print("coordinates: ", captcha_text)
else:
    print("task finished with error "+solver.error_code)
```
Report previosly solved captcha as incorrect:
```python
solver.report_incorrect_image_captcha()
```
___

Check out [examples](https://github.com/anti-captcha/anticaptcha-python) for other captcha types

---
Useful links:
- [Как решить рекапчу автоматически](https://anti-captcha.com/ru/apidoc/task-types/RecaptchaV2TaskProxyless)
- [Обход капчи](https://anti-captcha.com/ru/apidoc/task-types/ImageToTextTask)
- [Cómo resolver un recaptcha automáticamente](https://anti-captcha.com/es/apidoc/task-types/RecaptchaV2TaskProxyless)
- [Como resolver um recaptcha automaticamente](https://anti-captcha.com/pt/apidoc/task-types/RecaptchaV2TaskProxyless)