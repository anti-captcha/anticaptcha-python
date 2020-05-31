from anticaptchaofficial.antinetworking import *
from base64 import b64encode

class imagecaptcha(antiNetworking):

    def solve_and_return_solution(self, file_path, **kwargs):
        img = open(file_path, 'rb')
        img_str = b64encode(img.read()).decode('ascii')
        task_data = {
            "type": "ImageToTextTask",
            "body": img_str,
            "phrase": self.phrase,
            "case": self.case,
            "numeric": self.numeric,
            "math": self.math,
            "minLength": self.minLength,
            "maxLength": self.maxLength,
        }
        task_data.update(kwargs)
        if self.create_task({
            "clientKey": self.client_key,
            "task": task_data
        }) == 1:
            self.log("created task with id "+str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0

        task_result = self.wait_for_result(60)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["text"]
