

import json
import requests
from openpyxl import Workbook # import Workbook class from module openpyxl
import re


api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"


def get_number_of_jobs_T(technology):
    number_of_jobs = 0
    response = requests.get(api_url)
    if response.ok:             
        data = response.json()

    for jobs in data:
        skills = jobs.get('Key Skills')
        if technology in skills:
            number_of_jobs += 1

    return number_of_jobs


def get_number_of_jobs_L(location):
    number_of_jobs = 0
    response = requests.get(api_url)
    if response.ok:             
        data = response.json()

    for jobs in data:
        skills = jobs.get('Location')
        if location in skills:
            number_of_jobs += 1

    return number_of_jobs

list_of_locations = ("Los Angeles", "New York", "San Francisco", "Washington DC", "Seattle")
list_of_key_skills = ("C", "C#", "C++", "Java", "JavaScript", "Python", "Scala", "Oracle", "SQL Server", "MySQL Server", "PostgreSQL", "MongoDB")


wb=Workbook()                                            # create a workbook object
ws=wb.active                                             # use the active worksheet
ws.append(['Technology', 'Number of Jobs'])              # add a row with two columns 'Technology' and 'Number of Jobs'


for lname in list_of_locations:
    lcount = get_number_of_jobs_L(lname)
    ws.append([str(lname), str(lcount)])
    print("Appended ", lname, " and ", lcount)


for tname in list_of_key_skills:

    tcount = get_number_of_jobs_T(tname)
    ws.append([str(tname), str(tcount)])                 # add a row with two columns input of 'get_number_of_jobs(technology)' and the result of 'get_number_of_jobs(technology)'
    print("Appended ", tname, " and ", tcount)

wb.save(r"D:/Programming/Jobs count.xlsx")               # save the workbook into a file called countries.xlsx


