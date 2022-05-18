import re
import requests
from bs4 import BeautifulSoup
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    return pages[-1] # max page


def extract_jobs(soup):
    job_title = soup.find('h2', {'class': 'jobTitle'}).find('a').find('span')['title']
    company = soup.find('span', {'class': 'companyName'}).string
    tmp = soup.find('div', {'class': 'companyLocation'})
    if tmp is not None:
        location = tmp.string
    else:
        location = "Not submitted"
    job_dk, job_tk = soup.find('a')['data-jk'], soup.find('a')['data-mobtk']
    return {'title': job_title,
            'company': company,
            'location': location,
            "link": f"https://www.indeed.com/viewjob?jk={job_dk}&tk={job_tk}&from=serp&vjs=3"
            }


def get_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class', re.compile('^cardOutline')})
        for result in results:
            job = extract_jobs(result)
            jobs.append(job)
    return jobs


def get_job():
    last_page = get_last_pages()
    jobs = get_jobs(last_page)
    return jobs
