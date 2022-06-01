from anticaptchaofficial.antinetworking import *
import time


class geetestProxyless(antiNetworking):

    js_api_domain = ""
    gt = ""
    challenge = ""
    geetest_lib = ""
    version = 3
    init_parameters = {}

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "GeeTestTaskProxyless",
                "websiteURL": self.website_url,
                "gt": self.gt,
                "challenge": self.challenge,
                "geetestApiServerSubdomain": self.js_api_domain,
                "geetestGetLib": self.geetest_lib,
                "version": self.version,
                "initParameters": self.init_parameters
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
            return task_result["solution"]

    def set_gt_key(self, value):
        self.gt = value

    def set_challenge_key(self, value):
        self.challenge = value

    def set_js_api_domain(self, value):
        self.js_api_domain = value

    def set_geetest_lib(self, value):
        self.geetest_lib = value

    def set_version(self, value):
        self.version = value

    def set_init_parameters(self, object):
        self.init_parameters = object



