from anticaptchaofficial.antinetworking import *
import time


class recaptchaV3Proxyless(antiNetworking):

    min_score = 0.9
    page_action = ""

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "RecaptchaV3TaskProxyless",
                "websiteURL": self.website_url,
                "websiteKey": self.website_key,
                "minScore": self.min_score,
                "pageAction": self.page_action
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
        task_result = self.wait_for_result(60)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["gRecaptchaResponse"]

    def set_page_action(self, value):
        self.page_action = value

    def set_min_score(self, value):
        available_scores = [0.5, 0.7, 0.9]
        if value in available_scores:
            self.min_score = value
        else:
            self.min_score = 0.9

