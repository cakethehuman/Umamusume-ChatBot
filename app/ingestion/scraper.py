import logging
import requests

from bs4 import BeautifulSoup

from app.core.logger import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

CHARACTERS = ["Rice_Shower"]
BASEURL = "https://umamusu.wiki/"

def scrape_data(base_url, characters):
    for character in characters:
        url = f"{base_url}{character}"
        logging.info(f"Fetching url for this {character} umamusume")
        
        reponse = requests.get(url)
        logging.info(reponse.status_code)
        if reponse.status_code == 200:
            logging.info("Scraped status code 200")
            soup = BeautifulSoup(reponse.text, 'html.parser')
            data = []
            
            tag_find = soup.find_all(['h1','h2','p','tr','span'])
            for tag in tag_find:
                uma_data = tag.text.strip()
                data.append(uma_data)
            return {
                "title" : character,
                "url" : url,
                "content" : " ".join(data).strip()
            }
     
        else:
            logging.info(f"Failed to scrape status code : {reponse.status_code}")

        
data_result = scrape_data(base_url=BASEURL, characters=CHARACTERS)
print(data_result)