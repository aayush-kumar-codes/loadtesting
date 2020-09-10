import time
from locust import HttpUser, task, between,TaskSet
import config
import payloads



class DataSyncPostLoadTesting(TaskSet):
    wait_time = between(1,3)

    @task
    def candidate_score_bulk(self):
        response = self.client.post("/datasync/filter/get/candidate_score_bulk/5e86bd62718bf237a97fefbc?account-name="+str(config.account_name)+"",json=payloads.CandidateScorePayload)
        assert response.status_code == 200
        assert response
        


    @task
    def candidate_score_bulk_full(self):
        response = self.client.post("/datasync/filter/get/candidate_score_bulk/all:5e86bdab718bf237a97fefe2?account-name="+str(config.account_name)+"",json=payloads.CandidateScorePayload)
        assert response.status_code == 200
        assert response
        
    
    @task
    def candidate(self):
        response = self.client.post("/datasync/candidate/5e86bd62718bf237a97fefbc/unread?account-name="+str(config.account_name)+"",json=payloads.CandidatePayload)
        assert response.status_code == 200
        assert response
    