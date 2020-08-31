import time
from locust import HttpUser, task, between,TaskSet
import config


class SkillsApisLoadTesting(TaskSet):
    wait_time = between(1, 2)

    @task
    def Search(self):
        self.client.get("/search/search/html?account-name="+str(config.account_name)+"")

    @task
    def skills(self):
        self.client.get("/skill/css?account-name="+str(config.account_name)+"")

    @task
    def SkillsMatchbylang(self):
        self.client.get("/skill/match/css?account-name="+str(config.account_name)+"")

    @task
    def SkillsMatch(self):
        self.client.get("/skillextract/all:5e86bdab718bf237a97fefe2:1/html 5,css_3,angular_js?account-name="+str(config.account_name)+"")

    @task
    def getJobStatus(self):
        self.client.get("/resume/getJobStatus/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")
