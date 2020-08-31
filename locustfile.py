

import time
from locust import HttpUser, task, between,TaskSet
import config


class GetApisLoadTesting(TaskSet):
    wait_time = between(1, 2)

    @task
    def datasync(self):
        self.client.get("/datasync/filter/fetch/5e86bdab718bf237a97fefe2/job_profile/0/5e86bdab718bf237a97fefe5/True?account-name="+str(config.account_name)+"&accessToken="+str(config.access_token)+"")
    
    @task
    def JobProfileDatasync(self):
        self.client.get("/datasync/job-profile/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")

    @task
    def FilterExperiance(self):
        self.client.get("/datasync/filter/get/experiance/display?account-name="+str(config.account_name)+"")

    @task
    def FilterEducationByDegree(self):
        self.client.get("/datasync/filter/get/education/display/B.tech?account-name="+str(config.account_name)+"")

    @task
    def FilterEducation(self):
        self.client.get("/datasync/filter/get/education/display?account-name="+str(config.account_name)+"")

    @task
    def FilterEducationfull(self):
        self.client.get("/datasync/filter/get/education/display/full?account-name="+str(config.account_name)+"")

    @task
    def classifymoved(self):
        self.client.get("/datasync/classify-moved/5f3e393da226750039dc36c7/HR/softwaredevelopment?account-name="+str(config.account_name)+"")

    @task
    def profilemoved(self):
        self.client.get("/datasync/job-profile-moved/5f3e393da226750039dc36c7/5e86bdab718bf237a97fefe2/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")

    @task
    def datasyncdulldata(self):
        self.client.get("/datasync/full?account-name="+str(config.account_name)+"")


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


class Memory(HttpUser):
    tasks = [GetApisLoadTesting,SkillsApisLoadTesting]
