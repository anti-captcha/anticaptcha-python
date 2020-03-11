from anticaptchaofficial.recaptchav2proxyless import *

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key("ACCOUNT_KEY")

print("account balance: " + str(solver.get_balance()))