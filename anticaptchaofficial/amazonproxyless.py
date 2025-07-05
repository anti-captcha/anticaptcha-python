from anticaptchaofficial.antinetworking import *
import time


class amazonProxyless(antiNetworking):

    iv = ''
    context = ''
    captcha_script = ''
    challenge_script = ''
    jsapi_script = ''
    waf_type = 'default'

    def set_iv(self, value):
        self.iv = value

    def set_context(self, value):
        self.context = value

    def set_challenge_script(self, value):
        self.challenge_script = value

    def set_captcha_script(self, value):
        self.captcha_script = value

    def set_jsapi_script(self, value):
        self.jsapi_script = value

    def set_waf_type(self, value):
        self.waf_type = value

    def solve_and_return_solution(self):
        task = {
            "type": "AmazonTaskProxyless",
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "waf_type": self.waf_type,
            "iv": self.iv,
            "context": self.context,
            "captchaScript": self.captcha_script,
            "challengeScript": self.challenge_script,
            "jsapiScript": self.jsapi_script
        }
        if self.create_task({
            "clientKey": self.client_key,
            "task": task,
            "softId": self.soft_id
        }) == 1:
            self.log("created task with id "+str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0
        time.sleep(3)
        task_result = self.wait_for_result(300)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["token"]
