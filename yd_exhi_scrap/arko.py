import requests
from bs4 import BeautifulSoup


def move_current_page():
  URL = "https://www.arko.or.kr/"
  infos = []

  response = requests.get(f'{URL}artcenter/board/list/506?bid=266&dateLocation=now')
  soup = BeautifulSoup(response.text, "html.parser")

  title_link = soup.find("div",{"class": "textBox"})
  link = title_link.find('a')['href']
  current_link = f'{URL}{link}'

  title = soup.find("span",{"class": "subject"}).get_text()

  artist_box = soup.find("dl",{"class": "col1"})
  artist = artist_box.find('dd').string


  date_location = soup.find_all("dl",{"class": "col2"})
  date_box = date_location[0].find_all('dd')
  exhi_date = date_box[0].string

  location_box = date_location[1].find_all('dd')
  location = location_box[1].string

  info =  {
  "title": title,
  "artist": artist,
  "exhi_date": exhi_date,
  "location": location,
  "link": current_link
  }
  infos.append(info)

  return infos
  
