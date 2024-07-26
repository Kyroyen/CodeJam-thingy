import requests
from bs4 import BeautifulSoup

class Scapers:
    
    @classmethod
    def scrape_wiki_article(cls, url):
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
    