import logging
import requests

from bs4 import BeautifulSoup

from app.core.logger import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

CHARACTERS = ["Rice_Shower"]
BASEURL = "https://umamusu.wiki/"

def scrape_data(url, characters):
    for character in characters:
        url = f"{url}{character}"
        logging.info(f"Fetching url for this {character} umamusume")
        
        reponse = requests.get(url)
        logging.info(reponse.status_code)
        if reponse.status_code == 200:
            logging.info("Scraped succes")
            print("it work bro")
        else:
            logging.info("Cant scrape")
            print("It did not work bro")
        
        
    
scrape_data(url=BASEURL,
            characters=CHARACTERS)
