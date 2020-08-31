import time
from locust import HttpUser, task, between,TaskSet
import config



class DataSyncApisLoadTesting(TaskSet):
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
