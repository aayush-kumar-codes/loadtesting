import time
from locust import HttpUser, task, between,TaskSet
import config


class SkillsApisLoadTesting(TaskSet):
    wait_time = between(1, 2)

    @task
    def Search(self):
        response = self.client.get("/search/search/html?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def skills(self):
        response = self.client.get("/skill/css?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def SkillsMatchbylang(self):
        response = self.client.get("/skill/match/css?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def SkillsMatch(self):
        response = self.client.get("/skillextract/all:5e86bdab718bf237a97fefe2:1/html 5,css_3,angular_js?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def getJobStatus(self):
        response = self.client.get("/resume/getJobStatus/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response