import time
from locust import HttpUser, task, between,TaskSet
import config
import payloads


class Emailclassify(TaskSet):
    wait_time = between(1, 2)

    @task
    def emailclassify(self):
        response = self.client.get("/emailclassify/?account-name="+str(config.account_name)+"",json=payloads.EmailclassifyPayload)
        assert response.status_code == 200
        assert response
