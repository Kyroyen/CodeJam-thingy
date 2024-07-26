from typing import List

from util.scrape_wiki import Scapers
from util.time_finder import TimerFunction

class WhiteFunction:

    def __init__(
        self,
        messages: List[str]
    ) -> None:
        self.messages = messages
    
    @classmethod
    def scrape_wiki_article(cls, url):
        return Scapers.scrape_wiki_article(url)

    @classmethod
    def findT(cls, c1, c2): #city 1,2
        time = TimerFunction.findT(c1,c2)
        return time
    