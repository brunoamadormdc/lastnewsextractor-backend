import requests
from bs4 import BeautifulSoup
import statics
from slugify import slugify
import re
from tqdm import tqdm

class Scrapper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36',
        }
        self.statics = statics

    def scrapp(self,search='',type=''):


            list = []
            list_scrapp = self.statics.tipos[type]

            for pages in tqdm(list_scrapp):
                try:

                    url = requests.get(pages.get('link'), headers=self.headers)
                    soup = BeautifulSoup(url.content, "html.parser")
                    links = soup.find_all('a', href=True)

                    for l in links:
                        link = l.get('href')
                        text = l.text
                        slugtext = slugify(text)
                        slugsearch = slugify(search)

                        if search != '':

                            if re.search(slugsearch, slugtext, re.IGNORECASE) and link != '#':

                                if link[0] == '/':
                                    link = pages.get('link') + link

                                list.append({
                                    'link': link,
                                    'texto': text,
                                    'portal': pages.get('nome')
                                })

                        else:

                            list.append({
                                'link': link,
                                'texto': text,
                                'portal': pages.get('nome')
                            })

                except:
                    pass

            return list

    def scrapPage(self,page):


        list = []

        url = requests.get(page, headers=self.headers)
        soup = BeautifulSoup(url.content, "html.parser")
        links = soup.find_all('a', href=True)

        for l in links:

            link = l.get('href')
            text = l.text


            list.append({
                'link': link,
                'texto': text,
                'portal': page
            })

        return list


