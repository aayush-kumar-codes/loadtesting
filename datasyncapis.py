import time
from locust import HttpUser, task, between,TaskSet
import config


class DataSyncApisLoadTesting(TaskSet):
    wait_time = between(1, 2)


    @task
    def datasyncaccountname(self):
        response = self.client.get("/datasync/filter/fetch/5e86bdab718bf237a97fefe2/job_profile/0?account-name="+str(config.account_name)+"&accessToken="+str(config.access_token)+"")
        assert response.status_code == 200
        assert response
            
    @task
    def datasync(self):
        response = self.client.get("/datasync/filter/fetch/5e86bdab718bf237a97fefe2/job_profile/0/5e86bdab718bf237a97fefe5/True?account-name="+str(config.account_name)+"&accessToken="+str(config.access_token)+"")
        assert response.status_code == 200
        assert response

    @task
    def JobProfileDatasync(self):
        response = self.client.get("/datasync/job-profile/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response


    @task
    def FilterExperiance(self):
        response = self.client.get("/datasync/filter/get/experiance/display?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def FilterEducationByDegree(self):
        response = self.client.get("/datasync/filter/get/education/display/B.tech?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def FilterEducation(self):
        response = self.client.get("/datasync/filter/get/education/display?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def FilterEducationfull(self):
        response = self.client.get("/datasync/filter/get/education/display/full?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def profilemoved(self):
        response = self.client.get("/datasync/job-profile-moved/5f3e393da226750039dc36c7/5e86bdab718bf237a97fefe2/5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"")
        assert response.status_code == 200
        assert response

    @task
    def datasyncdulldata(self):
        response = self.client.get("/datasync/full?account-name="+str(config.account_name)+"")
        assert response.status_code == 200  
        assert response