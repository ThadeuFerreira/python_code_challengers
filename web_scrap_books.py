import re
import requests
from bs4 import BeautifulSoup

def get_books(url,topic):

    books = {}
    r = requests.get(url + topic)

    while r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('ol', class_='row')
        products = s.find_all('article', class_='product_pod')
        for product in products:
            title = product.find('h3').find('a').get_attribute_list('title')[0]
            available = product.find('p', class_='instock availability').text
            title = title.strip().lower()
            available = available.strip().lower()
            books[title] = available	
        next_page = soup.find('li', class_='next')
        if next_page:
            next_url = (url + topic).replace('index.html',next_page.find('a')['href'])

            r = requests.get(next_url)

        else:
            break
    return books
topics_list = {}

def checkCache(title,topic):
    if topic in topics_list:
        if title in topics_list[topic]:
            if topics_list[topic][title] == 'in stock':
                return True
        return False

def in_stock(title,topic):
    r = requests.get('https://books.toscrape.com/catalogue/category/books_1/index.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('ul', class_='nav nav-list')
    topics = s.find_all('li')
    topic_n = topic.strip().lower()
    title_n = title.strip().lower()
    if topic_n in topics_list:
        if checkCache(title_n,topic_n):
            return title + ' is available in ' + topic
        return title + ' is not available in ' + topic
    for t in topics:
        topic_name = t.find('a').text.strip().lower()
        topic_href = t.find('a')['href']
        
        if topic_href != 'index.html' and topic_name == topic_n:
            topics_list[topic_name] = get_books('https://books.toscrape.com/catalogue/category/books/', topic_href)

    if checkCache(title_n,topic_n):
        return title + ' is available in ' + topic

    return title + ' is not is available in ' + topic

p = in_stock("While You Were Mine", "Science")
print(p)
p = in_stock("The MooSEwood Cookbook: Recipes from Moosewood Restaurant, Ithaca, New York", "food and driNk")
print(p)
p = in_stock("Online Marketing for Busy Authors: A Step-By-Step guide", "Self help")
print(p)
p = in_stock("While You Were Mine", "Historical Fiction")
print(p)
p = in_stock("While You Were Mine", "Science")
print(p)
