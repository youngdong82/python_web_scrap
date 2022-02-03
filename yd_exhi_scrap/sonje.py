import requests
from bs4 import BeautifulSoup


def extract_info(current_link):
  response = requests.get(current_link)
  soup = BeautifulSoup(response.text, "html.parser")

  info_box = soup.find('div',{'id':'info_wrap'})

  title = info_box.find('h1').string
  date_location = info_box.find_all('li')
  exhi_date = date_location[1].string
  location = date_location[2].string

  if '아트선재센터' in exhi_date:
    location,exhi_date = exhi_date,location

  return {
    "title": title,
    "artist": "No available",
    "exhi_date": exhi_date,
    "location": location,
    "link": current_link
    }


def extract_link(each_exhi):
  return each_exhi['href']

def move_current_page():
  URL = "http://artsonje.org/"
  infos = []

  response = requests.get(f'{URL}category/exhibition/')
  soup = BeautifulSoup(response.text, "html.parser")

  lists = soup.find('div',{'class': 'lists'})
  exhi_list = lists.find_all('a')

  for each_exhi in exhi_list[0:3]:
    each_link = extract_link(each_exhi)
    info = extract_info(each_link)
    infos.append(info)
    

  return infos






