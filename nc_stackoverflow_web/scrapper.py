import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find('a', {'class': 's-link stretched-link'})["title"]

    c_l = html.find('h3', {'class': 'mb4'}).find_all("span")
    if c_l[0].string == None:
        company = 'CAN\'T FIND COMPANY'
    else:
        company = c_l[0].string.strip()
    location = c_l[-1].string.strip()

    job_id = html["data-jobid"]
    
    return {"title": title, "company": company, "location": location, "link": f'https://stackoverflow.com/jobs/{job_id}'}


def extract_jobs(last_page,url):
    jobs = []
    # for page in range(1,last_page+1):
    for page in range(last_page - 5):
        result = requests.get(f'{url}&pg={page}')
        soup = BeautifulSoup(result.text, "html.parser")
        each_jobs = soup.find_all("div", {"class": "-job"})
        for i in each_jobs:
            extract_job(i)
            job = extract_job(i)
            jobs.append(job)
    return jobs


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"})
    anchors = pagination.find_all("a")
    last_page = anchors[-3].get_text(strip=True)
    return int(last_page) + 2


def get_jobs(word):
    url = f'https://stackoverflow.com/jobs?q={word}'
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page,url)
    return jobs
