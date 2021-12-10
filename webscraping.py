# -*- coding: utf-8 -*-
"""
We have the list of jobs available along with the name of Company here
"""

import requests
from bs4 import BeautifulSoup as bs

fake_url= "https://realpython.github.io/fake-jobs/"
req=requests.get(fake_url)
content=req.content



soup= bs(content, 'html.parser')

all_jobs= soup.find(id="ResultsContainer")
job_elements = all_jobs.find_all("div", {"class":"card-content"})


for job in job_elements:
   title= job.find("h2", class_="title").text
   company=job.find("h3", class_="company").text
   #location= job.find("p",class_="location").text
   print()
   print("Job title is",title)
   print("Company name is",company)
  # print("Location : ",location)
   print()
   
    
    