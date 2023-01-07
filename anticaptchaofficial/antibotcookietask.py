from anticaptchaofficial.antinetworking import *
import time


class antibotcookieTask(antiNetworking):

    provider_name = ""

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "AntiBotCookieTask",
                "websiteURL": self.website_url,
                "proxyAddress": self.proxy_address,
                "proxyPort": self.proxy_port,
                "proxyLogin": self.proxy_login,
                "proxyPassword": self.proxy_password
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





