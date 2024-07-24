from typing import List
import requests
from bs4 import BeautifulSoup
from util.cities import Database as db
class WhiteFunction:
    speeds = {
    "car": {"speed": 80, "path": "road"},  # average highway speed
    "bus": {"speed": 60, "path": "road"},  # average city bus speed
    "commercial_plane": {"speed": 900, "path": "air"},
    "jet_plane": {"speed": 2400, "path": "air"},
    "helicopter": {"speed": 400, "path": "air"},
    "saturn_5": {"speed": 40000, "path": "air"},
    "starship sn15": {"speed": 27000, "path": "air"},
    "tesla": {"speed": 80, "path": "road"},  # average highway speed
    "walking": {"speed": 6, "path": "ground"},
    "scooter": {"speed": 25, "path": "road"},  # average electric scooter speed
    "f1_car": {"speed": 370, "path": "road"},
    "light_in_vacuum": {"speed": 299792458, "path": "air"},
    "dragon": {"speed": 200, "path": "air"},
    "proton": {"speed": 299792457, "path": "air"},
    "drill": {"speed": 15, "path": "ground"}
}

    def __init__(
        self,
        messages: List[str]
    ) -> None:
        self.messages = messages

    def scrape_wiki_article(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the title of the page
        title = soup.find(id="firstHeading").text

        # Get the first 600 char of the content
        content_div = soup.find(id="bodyContent")
        content_paragraphs=content_div.find_all('p')
        content = "\n".join([p.text for p in content_paragraphs[:3]])  # Adjust the number of paragraphs as needed
        lines = [line for line in content.split("\n") if line.strip() != '']  # Filter out empty lines
        for list in content_div.find_all('ul'):
            for each in list.find_all('li'):
                lines.append(each.get_text())
        first_600_chars = ('\n'.join(lines))[:600] + "..."  # Get the first 600 characters and append "..."

        # Find the first link to another wiki article
        all_links = soup.find(id="bodyContent").find_all("a", href=True)
        next_link = None
        for link in all_links:
            href = link['href']
            if href.startswith("/wiki/") and not href.startswith(("/wiki/Special:", "/wiki/Help:", "/wiki/Wikipedia","/wiki/File")) and title.upper() not in href.upper():
                print(href)
                next_link = "https://en.wikipedia.org" + href
                break

        return title, first_600_chars, next_link     
    def findT(self,c1,c2): #city 1,2
        time=[]
        for v in self.speeds.values():
            print(v)
            path=v["path"]
            speed=v["speed"]
            dist=db.get_distance(c1,c2,path)
            time.append(dist/speed)
        vehicles=self.speeds.keys()
        times=dict(zip(vehicles,time))
        return times


        

    #add functions here
    