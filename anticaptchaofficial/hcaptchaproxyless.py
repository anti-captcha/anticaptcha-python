from anticaptchaofficial.antinetworking import *
import time


class hCaptchaProxyless(antiNetworking):

    respkey = ""

    def get_user_agent(self):
        return self.user_agent

    def get_respkey(self):
        return self.respkey

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "HCaptchaTaskProxyless",
                "websiteURL": self.website_url,
                "websiteKey": self.website_key,
                "userAgent": self.user_agent,
                "isInvisible": self.is_invisible,
                "enterprisePayload": self.recaptcha_enterprise_payload
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
            if "userAgent" in task_result["solution"]:
                self.user_agent = task_result["solution"]["userAgent"]
            if "respKey" in task_result["solution"]:
                self.respkey = task_result["solution"]["respKey"]
            return task_result["solution"]["gRecaptchaResponse"]
