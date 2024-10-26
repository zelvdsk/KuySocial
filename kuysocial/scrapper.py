import re, time, json, random
from .other import domain, save, soup

class Scrapper:
    def __init__(self, ses) -> None:
        self.ses = ses

    # Get post
    def get_post_data(self, url: str=None) -> dict:
        output = []
        source = soup(self.ses.get(url or domain()).text)

        for post in source.find_all('div', class_='post'):
            try: output.append(post['data-id'])
            except KeyError: continue

        return output


