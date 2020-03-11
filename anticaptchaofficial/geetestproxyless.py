from anticaptchaofficial.antinetworking import *
import time


class geetestProxyless(antiNetworking):

    js_api_domain = ""
    gt = ""
    challenge = ""

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "GeeTestTaskProxyless",
                "websiteURL": self.website_url,
                "gt": self.gt,
                "challenge": self.challenge,
                "geetestApiServerSubdomain": self.js_api_domain
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
            return task_result["solution"]

    def set_gt_key(self, value):
        self.gt = value

    def set_challenge_key(self, value):
        self.challenge = value

    def set_js_api_domain(self, value):
        self.js_api_domain = value



