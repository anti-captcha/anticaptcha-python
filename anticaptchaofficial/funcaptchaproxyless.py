from anticaptchaofficial.antinetworking import *
import time


class funcaptchaProxyless(antiNetworking):

    js_api_domain = ""

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaTaskProxyless",
                "websiteURL": self.website_url,
                "funcaptchaApiJSSubdomain": self.js_api_domain,
                "websitePublicKey": self.website_key
            }
        }) == 1:
            self.log("created task with id "+str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0
        #checking result
        time.sleep(3)
        task_result = self.wait_for_result(600)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["token"]

    def set_js_api_domain(self, value):
        self.js_api_domain = value



