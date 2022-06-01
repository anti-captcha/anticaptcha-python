from anticaptchaofficial.antigatetask import *
import time

solver = antigateTask()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("http://antigate.com/logintest2fa.php")
solver.set_template_name("Sign-in with 2FA and wait for control text")
solver.set_variables({
    "login_input_css": "#login",
    "login_input_value": "test login",
    "password_input_css": "#password",
    "password_input_value": "test password",
    "2fa_input_css": "#2facode",
    "2fa_input_value": "_WAIT_FOR_IT_",
    "control_text": "You have been logged successfully"
})

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

task_id  = solver.send_antigate_task()
if task_id == 0:
    print("could not create task")
    exit()

time.sleep(5)  # emulating actual 2fa retrieval
solver.push_variable(task_id, "2fa_input_value", "349001")
result = solver.wait_for_result(600)

if result != 0:
    cookies, localStorage, fingerprint, url, domain = result["cookies"], result["localStorage"], result["fingerprint"], result["url"], result["domain"]
    print("cookies: ", cookies)
    print("localStorage: ", localStorage)
    print("fingerprint: ", fingerprint)
    print("url: "+url)
    print("domain: "+domain)
else:
    print("task finished with error "+solver.error_code)
