import re
import requests
from bs4 import BeautifulSoup
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    return pages[-1] # max page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    # results = soup.find_all("div", {"class": "fs-unmask"})
    results = soup.find_all('div', {'class', re.compile('^cardOutline')})
    for result in results:
        job_title = result.find('h2', {'class': 'jobTitle'}).find('a').find('span')['title']
        company = result.find('span', {'class': 'companyName'}).string
        print(company)
    return jobs
