import requests
from bs4 import BeautifulSoup
import statics

import helpers.Helpers as Helpers
import re
from tqdm import tqdm
from classes.chat import Chat
from classes.video import Video

slugify = Helpers.ToolHelper.slugify
verify_link_hash = Helpers.ToolHelper.verify_link_hash

class Scrapper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36',
        }
        self.statics = statics
        self.chat = Chat()
        self.video = Video()

    def scrapp_unique(self,search='',pages={}):
        
        list = []

        try:
            url = requests.get(pages.get('link'), headers=self.headers)
            soup = BeautifulSoup(url.content, "html.parser")
            links = soup.find_all('a', href=True)
            
            for l in tqdm(links):
                link = l.get('href')
                text = l.text
                slugtext = slugify(text)
                slugsearch = slugify(search)
                
                link = verify_link_hash(link, pages.get('link'))

                if search != '':

                    if re.search(slugsearch, slugtext, re.IGNORECASE):

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

                        link = verify_link_hash(link, pages.get('link'))

                        if search != '':

                            if re.search(slugsearch, slugtext, re.IGNORECASE):
                                
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
            link = verify_link_hash(link, page)

            list.append({
                'link': link,
                'texto': text,
                'portal': page
            })

        return list

    def scrap_get_resume(self, url='',  prompt='Me faça um resumo do mais importante dentro deste conteúdo'):
        try:
            if url == '':
                return False
            
            content = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(content.content, "html.parser")
            
            html = soup.get_text()
            html = html.replace('\n', ' ')

            #remove all blank spaces from list
            html = re.sub('\s+', ' ', html)
            html = ' '.join(html.split())
                        
            resume = self.chat.chat_with_intelligence(prompt=prompt, content=html)

            return resume
        
        except:
            return Exception('Ocorreu um erro ao gerar o resumo')

    def scrap_get_resume_youtube(self, url='',  prompt='Me faça um resumo do mais importante dentro deste conteúdo'):
        
        if url == '':
            return False
        
        try:
            content = self.video.video_to_speech(youtube_url=url)
            resume = self.chat.chat_with_intelligence(prompt=prompt, content=content.text)
            return resume
        except:
            return Exception('Ocorreu um erro ao gerar o resumo')
