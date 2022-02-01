import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}&vjk=f72db9a6eca68b5f'

# https://www.indeed.com/jobs?q=python&limit=50&start=50&vjk=1d18042b01f32ea6


def extract_job(anchor):
    each_h2 = anchor.find('h2', {'class': 'jobTitle'})
    titles = each_h2.find_all('span')
    each_title = str(titles[-1].string)

    company = anchor.find('span', {"class": "companyName"})
    each_company = str(company.string)

    location = anchor.find('div', {"class": "companyLocation"})
    each_location = location.string

    job_page = anchor["id"]
    job_id = job_page.split('_')[1]

    return {
        "title":
        each_title,
        "company":
        each_company,
        "location":
        each_location,
        "link":
        f'https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3'
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        anchors = soup.find_all("a", {"class": "tapItem"})

        for i in anchors:
            job = extract_job(i)
            jobs.append(job)
    return jobs

def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    uls = pagination.find('ul', {"class": "pagination-list"})
    links = uls.find_all('li')

    pages = []
    for link in links[1:-1]:
        pages.append(int(link.string))
    pages = pages
    max_page = pages[-1]

    return max_page

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs