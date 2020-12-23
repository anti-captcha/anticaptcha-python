anticaptchaofficial
===================

Official https://anti-captcha.com/ library for solving images with text, Recaptcha v2/v3 Enterprise/non-Enterprise, Funcaptcha Arcoselabs, GeeTest and hCaptcha.
Anti-Captcha is the most popular and reliable captcha solving service, working since 2007.
Prices for solving captchas start from $0.0005 per item.

Python 3:


```bash
pip3 install anticaptchaofficial
```

Python 2 not supported.
___
Example how to create Recaptcha V2 task and receive g-response:

```python
from anticaptchaofficial.recaptchav2proxyless import *

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print "g-response: "+g_response
else:
    print "task finished with error "+solver.error_code
```
___

Solve image captcha:

```python
from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")

captcha_text = solver.solve_and_return_solution("captcha.jpeg")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)
```
___

Solve Funcaptcha (Arkoselabs):

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

Solve GeeTest captcha:

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

Check out [examples](https://github.com/AdminAnticaptcha/anticaptcha-python) for other captcha types