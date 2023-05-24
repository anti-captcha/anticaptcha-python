from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")

# example of raw image from disc or
with open('captcha.jpeg', 'rb') as img:
    raw_img = img.read()

# example of raw image from requests
# import requests
# ses = requests.session()
# r = ses.get('url_to_captcha_image')
# raw_img = r.content

captcha_text = solver.solve_and_return_solution(None, body=raw_img)
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)
