import json
import requests
from bs4 import BeautifulSoup
from config_data.config import URL


def pars(file_name):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html')
    cards = soup.find_all('article', class_ = 'eHNixi M8Lgt1')
    dict_news = {}
    for article in cards:
        article_title = article.find('h3', class_ = 'YxvQCi')
        article_title = article_title.find('span').text
        article_url = article.find('a', class_ = 'aR0VY2')
        article_id = article_url.get('href').split('-')[1]
        article_url = f'https://sport24.ru{article_url.get("href")}'
        article_desc = article.find('div', class_ = 'xfcRfR').text
        article_data_time = article.find('div', class_ = 'GCohXx').find('span').text
        
        dict_news[article_id] = {
            'article_title': article_title,
            'article_url': article_url,
            'article_desc': article_desc,
            'article_time': article_data_time
        }
    with open(f'{file_name}.json', 'w', encoding='utf-8') as file:
        json.dump(dict_news, file, indent = 4, ensure_ascii=False)