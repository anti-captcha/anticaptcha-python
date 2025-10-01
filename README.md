anticaptchaofficial
===================

Official https://anti-captcha.com/ library for solving images with text, Recaptcha v2/v3 Enterprise or non-Enterprise, Funcaptcha Arcoselabs, GeeTest and others.
Anti-Captcha is the most popular and reliable captcha solving service, working since 2007.
Prices for solving captchas start from $0.0005 per token.

#### How to solve:
- [Image captcha](#solve-image-captcha)
- [Recaptcha v2](#how-to-solve-recaptcha-v2)
- [Recaptcha V3](#how-to-solve-recaptcha-v3)
- [Hcaptcha](#solve-hcaptcha)
- [FunCaptcha Arkoselabs](#solve-funcaptcha-arkoselabs)
- [Geetest V3](#solve-geetest-v3)
- [Geetest V4](#solve-geetest-v4)
- [Turnstile](#solve-turnstile)
- [Antigate templates](#antigate-template-tasks)
- [Image to coordinates](#image-to-coordinates)
- [Prosopo](#prosopo-captcha)
- [Friendly Captcha](#friendly-captcha)
- [Amazon WAF](#solve-amazon-waf)
- [Altcha](#solve-altcha)

### Basics

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

### [Solve image captcha with python](https://anti-captcha.com/apidoc/task-types/ImageToTextTask)

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

### How to solve Recaptcha V2

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


### How to solve Recaptcha V3

Example how to create [Recaptcha V3](https://anti-captcha.com/apidoc/task-types/RecaptchaV3TaskProxyless) task and receive g-response:

```python
from anticaptchaofficial.recaptchav3proxyless import *

solver = recaptchaV3Proxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_page_action("home_page")
solver.set_min_score(0.9)

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print "g-response: "+g_response
else:
    print "task finished with error "+solver.error_code
```
___

&nbsp;
### Solve Hcaptcha

Solve [HCaptcha](https://anti-captcha.com/apidoc/task-types/HCaptchaTask) and receive its token:

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

### Solve FunCaptcha Arkoselabs
Solve [Funcaptcha](https://anti-captcha.com/apidoc/task-types/FunCaptchaTaskProxyless) (Arkoselabs) and receive the token:

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

### Solve GeeTest v3

Solve [GeeTest](https://anti-captcha.com/apidoc/task-types/GeeTestTask) captcha and receive its token:

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

### Solve Geetest v4

Solve [GeeTest v4](https://anti-captcha.com/apidoc/task-types/GeeTestTask) captcha and receive its token:

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

### Solve Turnstile

Example how to solve [Turnstile](https://anti-captcha.com/apidoc/task-types/TurnstileTaskProxyless) task and receive a token:

```python
from anticaptchaofficial.turnstileproxyless import *

solver = turnstileProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

# Optionally specify page action
solver.set_action("login")

# Optionally specify cData and chlPageData tokens for Cloudflare pages
#solver.set_cdata("cdata_token")
#solver.set_chlpagedata("chlpagedata_token")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

token = solver.solve_and_return_solution()
if token != 0:
    print "token: "+token
else:
    print "task finished with error "+solver.error_code
```
____

&nbsp;

### Antigate template tasks

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

### Image to coordinates

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

&nbsp;

### Prosopo captcha

Example how to create [Prosopo](https://anti-captcha.com/apidoc/task-types/ProsopoTaskProxyless) captcha and receive a token:

```python
from anticaptchaofficial.prosopoproxyless import *

solver = prosopoProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

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

### Friendly captcha

Example how to create [Friendly Captcha](https://anti-captcha.com/apidoc/task-types/FriendlyCaptchaTaskProxyless) task and receive a token:

```python
from anticaptchaofficial.friendlycaptchaproxyless import *

solver = friendlyCaptchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

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

### Solve Amazon WAF

Two options here:
1. When captcha is at the bot filtering page and you need aws-was-token cookie:

```python
from anticaptchaofficial.amazonproxyless import *

solver = amazonProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("key_value_from_window.gokuProps_object")
solver.set_iv("iv_value_from_window.gokuProps_object")
solver.set_context("context_value_from_window.gokuProps_object")

# Optional script URLs
solver.set_captcha_script("https://e9b10f157f38.9a96e8b4.us-gov-west-1.captcha.awswaf.com/e9b10f157f38/76cbcde1c834/2a564e323e7b/captcha.js")
solver.set_challenge_script("https://e9b10f157f38.9a96e8b4.us-gov-west-1.token.awswaf.com/e9b10f157f38/76cbcde1c834/2a564e323e7b/challenge.js")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

token = solver.solve_and_return_solution()
if token != 0:
    print "token: "+token
else:
    print "task finished with error "+solver.error_code
```

2. When captcha is a standalone widget which is triggered by user's action:
```python
from anticaptchaofficial.amazonproxyless import *

solver = amazonProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("Captcha widget's API key from AwsWafCaptcha.renderCaptcha function")
solver.set_waf_type("widget")
solver.set_jsapi_script("https://164cb210e333.edge.captcha-sdk.awswaf.com/164cb210e333/jsapi.js")

token = solver.solve_and_return_solution()
if token != 0:
    print "token: "+token
else:
    print "task finished with error "+solver.error_code
```
  
For more details visit [Anti-Captcha Amazon WAF documentation](https://anti-captcha.com/apidoc/task-types/AmazonTaskProxyless).
____


&nbsp;
### Solve Altcha

Solve [Altcha](https://anti-captcha.com/apidoc/task-types/AltchaTaskProxyless) and receive its token:

```python
from anticaptchaofficial.altchaproxyless import *

solver = altchaProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_challenge_url("/path/to/challenge/url")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

token = solver.solve_and_return_solution()
if token != 0:
    print("token: "+token)
else:
    print("task finished with error "+solver.error_code)
```
___


Check out [examples](https://github.com/anti-captcha/anticaptcha-python) for other captcha types

---
Useful links:
- [Как решить рекапчу автоматически](https://anti-captcha.com/ru/apidoc/task-types/RecaptchaV2TaskProxyless)
- [Обход капчи](https://anti-captcha.com/ru/apidoc/task-types/ImageToTextTask)
- [Cómo resolver un recaptcha automáticamente](https://anti-captcha.com/es/apidoc/task-types/RecaptchaV2TaskProxyless)
- [Como resolver um recaptcha automaticamente](https://anti-captcha.com/pt/apidoc/task-types/RecaptchaV2TaskProxyless)