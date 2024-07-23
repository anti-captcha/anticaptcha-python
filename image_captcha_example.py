from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")

# optional parameters, see https://anti-captcha.com/apidoc/task-types/ImageToTextTask for details
# solver.set_phrase(True)                      # 2 words
# solver.set_case(True)                        # case sensitivity
# solver.set_numeric(1)                        # only numbers
# solver.set_minLength(1)                      # minimum captcha text length
# solver.set_maxLength(10)                     # maximum captcha text length
# solver.set_math(True)                        # math operation result, for captchas with text like 50+5
# solver.set_comment("only green characters")  # comment for workers
# solver.set_language_pool("en")               # language pool


captcha_text = solver.solve_and_return_solution("captcha.jpeg")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)
