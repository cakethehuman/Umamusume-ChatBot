import requests
import json

from pydantic import BaseModel, PrivateAttr, Field
from bs4 import BeautifulSoup

from app.core.logger import get_logger

logger = get_logger(__name__)

BASEURL = 'https://umamusu.wiki/'
class CharacterScraper(BaseModel):
    base_url : str | None = BASEURL
    data_result : list[dict] = Field(default_factory=list)
    _session : requests.Session = PrivateAttr(default_factory=requests.Session)
    
    def scrape_character(self, character_name) -> dict:
        url = f"{self.base_url}{character_name}"
        logger.info(f"Fetching Character data for {character_name}")
        response = self._session.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
                
        tag_find = soup.find_all(['h1','h2','p','tr', 'td', 'li'])
        
        for tag in tag_find:
            uma_data = tag.get_text(strip=True)
            data.append(uma_data)
            
        return {
            "title" : character_name,
            "url" : url,
            "content" : " ".join(data).strip()
        }
    
    def scrape_characters_list(self):
        logger.info("SCRAPING DATA FROM ", self.base_url)
        character_response = self._session.get(self.base_url + 'List_of_Characters')
        character_response.raise_for_status()
        soup = BeautifulSoup(character_response.text, "html.parser")
        
        for box in soup.find_all('div', class_ = 'name-box overflow'):
            for char in box.find_all('a'):
                character_name = char.text.strip()
                self.data_result.append(self.scrape_character(character_name))

        logger.info("Scrapper is succesful", len(self.data_result))
        with open("data/uma_data.json", "w", encoding="utf-8") as file:
            json.dump(self.data_result, 
                      file, 
                      ensure_ascii=False,
                      indent=4)
               

