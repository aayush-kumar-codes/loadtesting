

import time
from locust import HttpUser, task, between,TaskSet
from datasyncapis import DataSyncApisLoadTesting
from skillsapis import SkillsApisLoadTesting




class MainLoadTesting(HttpUser):
    tasks = [DataSyncApisLoadTesting,SkillsApisLoadTesting]
