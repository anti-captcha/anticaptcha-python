from anticaptchaofficial.antinetworking import *
import time


class funcaptchaProxyon(antiNetworking):

    js_api_domain = ""
    data_blob = ""

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaTask",
                "websiteURL": self.website_url,
                "funcaptchaApiJSSubdomain": self.js_api_domain,
                "data": self.data_blob,
                "websitePublicKey": self.website_key,
                "proxyType": self.proxy_type,
                "proxyAddress": self.proxy_address,
                "proxyPort": self.proxy_port,
                "proxyLogin": self.proxy_login,
                "proxyPassword": self.proxy_password,
                "userAgent": self.user_agent
            },
            "softId": self.soft_id
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

    def set_data_blob(self, value):
        self.data_blob = value



