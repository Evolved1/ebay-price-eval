import requests
from bs4 import BeautifulSoup
import utility
import hashlib


def get_data(url):
    r = requests.get(url)
    if r.status_code != 200:
        print('Failed to get data: ', r.status_code)
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.text)
    return soup

def parse(soup):
    product_list = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {'title': title(item),
            'sold_price': sold_price(item),
            'sold_date': sold_date(item),
            'link': link(item),
            'hash': hashlib.md5(link(item).encode('utf-8'))}
        product_list.append(products)
        #print(products)
    return product_list

def title(item):
    title = item.find('div', {'class': 's-item__title'})
    if title:
        title = title.text
    else:
        title = utility.error_4()
    return title

def sold_price(item):
    separator = 't'
    sold_price = item.find('span', {'class':'s-item__price'})
    if sold_price:
        sold_price = float(sold_price.text.replace('AU','').replace(' ', '').replace('$','').replace(',','').split(separator,1)[0].strip())
    else:
        sold_price = utility.error_4()
    return sold_price

def sold_date(item):
    sold_date = item.find('span', {'class': 'POSITIVE'})
    if sold_date:
        sold_date = sold_date.text
    else:
        sold_date = utility.error_4()
    return sold_date

def link(item):
    link = item.find('a', {'class': 's-item__link'})['href']
    if link:
        link = link
    else:
        link = utility.error_4()
    return link


def loadup(product_list):
    return
