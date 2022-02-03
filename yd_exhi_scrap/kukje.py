import requests
from bs4 import BeautifulSoup

def extract_info(current_URL,URL):
  response = requests.get(current_URL)
  soup = BeautifulSoup(response.text, "html.parser")

  title_link = soup.find("a",{"class": "exhibitions_name"})
  title = title_link.string
  link = title_link['href']
  current_link = f'{URL}/{link}'

  artist = soup.find("div",{"class": "exhibitions_artists"}).string
  exhi_date = soup.find("span",{"class": "exhibitions_date"}).string
  location = soup.find("span",{"class": "exhibitions_location"}).string

  return {
    "title": title,
    "artist": artist,
    "exhi_date": exhi_date,
    "location": location,
    "link": current_link
    }

def move_current_page():
  URL = "https://www.kukjegallery.com/"
  infos = []

  response = requests.get(URL)
  soup = BeautifulSoup(response.text, "html.parser")

  big_div = soup.find('div', {'id': 'slides'})
  current_exhi_link = big_div.find('a')['href']
  current_URL = f'{URL}/{current_exhi_link}'

  
  info = extract_info(current_URL,URL)
  infos.append(info)

  return infos

