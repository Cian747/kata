from .models import Jobs
import os
import json

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
rawdata_url = os.path.join(SITE_ROOT, 'static', 'MOCK_DATA.json')
job_url = open(rawdata_url, encoding = "cp437")
job_url2 = json.load(job_url)
job = []

def main():
    '''
    Fetch all the data
    '''
    for jobs in job_url2:
        job_id = jobs['id']
        first_name = jobs['first_name']
        last_name = jobs['last_name']
        gender = jobs['gender']
        job_title = jobs['job_title']

        jobs = Jobs(job_id,first_name,last_name,gender,job_title)

        job.append(jobs)      

    return job


    # Total male and female
    # Table UI for front end



    # Things to work on
    # Speed
    # Solve in the simplest way
    # Research on simpler ways a kata could have been solved.




