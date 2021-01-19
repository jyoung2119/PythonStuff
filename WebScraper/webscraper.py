import requests
from bs4 import BeautifulSoup
import json

url = "https://www.indeed.com/q-software-developer-l-San-Antonio,-TX-jobs.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

for job in job_elems:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('span', class_='company')
    location_elem = job.find('span', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print("\n")
