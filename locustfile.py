

import time
from locust import HttpUser, task, between,TaskSet
from datasyncapis import DataSyncApisLoadTesting
from skillsapis import SkillsApisLoadTesting
from datasyncpostapis import DataSyncPostLoadTesting
from emailclassify import Emailclassify
from resume import ResumeApisLoadTesting

class MainLoadTesting(HttpUser):
    tasks = [DataSyncApisLoadTesting,SkillsApisLoadTesting,DataSyncPostLoadTesting,Emailclassify,ResumeApisLoadTesting]
    #tasks = [DataSyncPostLoadTesting]