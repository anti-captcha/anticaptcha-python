from anticaptchaofficial.antinetworking import *
import time


class amazonProxyon(antiNetworking):

    iv = ''
    context = ''
    captcha_script = ''
    challenge_script = ''

    def set_iv(self, value):
        self.iv = value

    def set_context(self, value):
        self.context = value

    def set_challenge_script(self, value):
        self.challenge_script = value

    def set_captcha_script(self, value):
        self.captcha_script = value

    def solve_and_return_solution(self):
        task = {
            "type": "AmazonTask",
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "iv": self.iv,
            "context": self.context,
            "captchaScript": self.captcha_script,
            "challengeScript": self.challenge_script,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password
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
