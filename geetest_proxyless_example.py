from anticaptchaofficial.geetestproxyless import *

# V3 example:
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


# V4 example:
solver = geetestProxyless()
solver.set_verbose(1)
solver.set_key("YOUR_API_KEY")
solver.set_website_url("https://address.com")
solver.set_gt_key("captchaId value")
solver.set_version(4)
solver.set_init_parameters({"riskType": "slide"})
token = solver.solve_and_return_solution()
if token != 0:
    print("result tokens: ")
    print(token)
else:
    print("task finished with error "+solver.error_code)

