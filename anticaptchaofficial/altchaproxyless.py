from anticaptchaofficial.antinetworking import *
import time


class altchaProxyless(antiNetworking):

    challenge_url = ''
    challenge_json = ''

    def set_challenge_url(self, value):
        self.challenge_url = value

    def set_challenge_json(self, value):
        self.challenge_json = value

    def solve_and_return_solution(self):
        task = {
            "type": "AltchaTaskProxyless",
            "websiteURL": self.website_url,
            "challengeURL": self.challenge_url,
            "challengeJSON": self.challenge_json
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
        #checking result
        time.sleep(3)
        task_result = self.wait_for_result(300)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["token"]
