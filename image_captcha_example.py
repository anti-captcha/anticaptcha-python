from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")

captcha_text = solver.solve_and_return_solution("captcha.jpeg")
if captcha_text != 0:
    print "captcha text "+captcha_text
else:
    print "task finished with error "+solver.error_code
