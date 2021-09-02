from models import Jobs
import urllib.request
from . import MOCK_DATA.json 

job_url = MOCK_DATA.json


def main():
    '''
    Fetch all the data
    '''
    get_job_data = job_url

    with urllib.request .format(get_job_data):
        job_results = url.read(get_job_data)
        get_job_response = 

    for jobs in get_job_response:
        first_name = jobs.get('first_name')
        last_name = jobs.get('last_name')
        gender = jobs.get('gender')
        job_title = jobs.get('job_title')


        jobs = Jobs(first_name = first_name, last_name = last_name, gender = gender,job_title=job_title)

        return jobs


    # Total male and female
    # Table UI for front end



    # Things to work on
    # Speed
    # Solve in the simplest way
    # Research on simpler ways a kata could have been solved.




