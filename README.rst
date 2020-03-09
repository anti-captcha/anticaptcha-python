Official https://anti-captcha.com/ library for solving images with text, Recaptcha v2/v3, Funcaptcha and GeeTest.
Anti-Captcha is the most popular and reliable captcha solving service.
Prices for solving captchas start from $0.0005 per item.

Python 3:
>>> pip3 install anticaptchaofficial

Python 2:
>>> pip install anticaptchaofficial==1.0.22

.. code:: python

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


Check out examples for other captcha types