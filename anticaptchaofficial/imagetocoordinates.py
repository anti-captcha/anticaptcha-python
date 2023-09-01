from anticaptchaofficial.antinetworking import *
from base64 import b64encode


class imagetocoordinates(antiNetworking):

    solve_mode = "points"

    def solve_and_return_solution(self, file_path, **kwargs):
        """
        :param file_path: path to captcha image on disk
        :param kwargs: contains key-value pairs for updating task_data dict
        """
        if file_path is not None:
            with open(file_path, 'rb') as img:
                img_str = img.read()
                img_str = b64encode(img_str).decode('ascii')
        else:
            img_str = kwargs.get('body')
            if type(img_str) is bytes:
                img_str = b64encode(img_str).decode('ascii')
                kwargs.update({'body': img_str})

        if file_path is None and img_str is None:
            self.log("file_path or body (in kwargs) has to be provided")
            return 0

        task_data = {
            "type": "ImageToCoordinatesTask",
            "body": img_str,
            "mode": self.solve_mode,
            "comment": self.comment
        }
        task_data.update(kwargs)
        if self.create_task({
            "clientKey": self.client_key,
            "task": task_data,
            "softId": self.soft_id
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
            return task_result["solution"]["coordinates"]

    def set_mode(self, value):
        if value in ["points", "rectangles"]:
            self.solve_mode = value
