import time
from locust import HttpUser, task, between,TaskSet
import config
import payloads



class ResumeApisLoadTesting(TaskSet):
    wait_time = between(1, 2)


    @task
    def resumeapi(self):
        response = self.client.get("/resume/743549474f79e5698e63f1757a40fcc2.docx/5f48c5fb40effb1c18c9f6a5?account-name="+str(config.account_name)+"",json=payloads.ResumePayload)
        assert response.status_code == 200
        assert response

    @task
    def resumebyskillapi(self):
        response = self.client.get("/resume/743549474f79e5698e63f1757a40fcc2.docx/5f48c5fb40effb1c18c9f6a5/css?account-name="+str(config.account_name)+"",json=payloads.ResumePayload)
        assert response.status_code == 200
        assert response
