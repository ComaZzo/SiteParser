import requests
from bs4 import BeautifulSoup


def load_habr_news_posts() -> list:
    page = requests.get('https://habr.com/ru/news/')
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('article', {'class': 'post post_preview'})
    result_list = list()
    for article in articles:
        title = article.find(class_="post__title").text
        author = article.find(class_="user-info__nickname user-info__nickname_small").text
        href = article.find(class_="post__title").find('a').get("href")
        comms = article.find(class_="post-stats__comments-count")
        comms = comms.text if comms is not None else 0
        votes = article.find(class_="voting-wjt__counter").text
        
        result_list.append({'author': str(author),
                            'href': str(href),
                            'title': str(title),
                            'comms': str(comms),
                            'votes': str(votes)})
    
    return result_list
