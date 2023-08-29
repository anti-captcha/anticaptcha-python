from anticaptchaofficial.imagecoordinates import *

solver = imagecoordinates()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_mode("points")
solver.set_comment("Select in specified order")

coordinates = solver.solve_and_return_solution("coordinates.png")
if coordinates != 0:
    print("coordinates: ", captcha_text)
else:
    print("task finished with error "+solver.error_code)
