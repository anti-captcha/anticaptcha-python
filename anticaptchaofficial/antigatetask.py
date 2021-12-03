from anticaptchaofficial.antinetworking import *
import time


class antigateTask(antiNetworking):

    template_name = ""
    variables = {}

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "AntiGateTask",
                "websiteURL": self.website_url,
                "templateName": self.template_name,
                "variables": self.variables,
                "proxyAddress": self.proxy_address,
                "proxyPort": self.proxy_port,
                "proxyLogin": self.proxy_login,
                "proxyPassword": self.proxy_password
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

    def set_template_name(self, value):
        self.template_name = value

    def set_variables(self, value):
        self.variables = value



