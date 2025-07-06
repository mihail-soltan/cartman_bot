from bs4 import BeautifulSoup
import requests
import pandas as pd

test_script = "https://southpark.fandom.com/wiki/Cartman_Gets_an_Anal_Probe/Script"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
         }
api = "https://spapi.dev/api/episodes?page="

episode_urls = []
characters = []
lines = []

def get_episode_urls(api):
    # response = requests.get(api)
    # episodes = response.json()
    page=1
    for page in range(1, 33):
        response = requests.get(api+str(page))
        episodes = response.json()
        for episode in episodes['data']:
            episode_urls.append(episode['wiki_url']+"/Script")
        page+=1

test_script_html = requests.get(test_script, headers=headers)
soup = BeautifulSoup(test_script_html.content, 'html.parser')

def grab_script(soup):
    # print(soup.find_all('table', {'class': 'headersthemes'}))
    for line in soup.find_all('table', {'class': 'headerscontent'}):
       for x in line.find_all('td', {'class': 'DLborderBOT DLborderRIGHT'}):

           if x.text.replace('\n','') != '':
               characters.append(x.text.replace('\n', ''))
               # print(x.find_next_sibling('td'))
               lines.append(x.find_next_sibling('td').text.replace('\n',''))
           else:
               continue

get_episode_urls(api)
print(episode_urls)
# grab_script(soup)