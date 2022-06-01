from anticaptchaofficial.antinetworking import *
import time


class recaptchaV2EnterpriseProxyon(antiNetworking):

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "RecaptchaV2EnterpriseTask",
                "websiteURL": self.website_url,
                "websiteKey": self.website_key,
                "enterprisePayload": self.recaptcha_enterprise_payload,
                "proxyType": self.proxy_type,
                "proxyAddress": self.proxy_address,
                "proxyPort": self.proxy_port,
                "proxyLogin": self.proxy_login,
                "proxyPassword": self.proxy_password,
                "userAgent": self.user_agent,
                "cookies": self.cookies
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
        task_result = self.wait_for_result(300)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["gRecaptchaResponse"]
