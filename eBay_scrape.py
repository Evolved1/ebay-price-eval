import requests
from bs4 import BeautifulSoup
import pandas as pd

ERROR_0 = 'Error 0: No Data or Not Parsed Correctly'

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
            'sold price': sold_price(item),
            'solddate': sold_date(item),
            'link': link(item)}
        product_list.append(products)
        #print(products)
    return product_list

def title(item):
    title = item.find('div', {'class': 's-item__title'})
    if title:
        title = title.text
    else:
        title = ERROR_0
    return title

def sold_price(item):
    separator = 't'
    sold_price = item.find('span', {'class':'s-item__price'})
    if sold_price:
        sold_price = float(sold_price.text.replace('AU','').replace(' ', '').replace('$','').replace(',','').split(separator,1)[0].strip())
    else:
        sold_price = ERROR_0
    return sold_price

def sold_date(item):
    sold_date = item.find('span', {'class': 'POSITIVE'})
    if sold_date:
        sold_date = sold_date.text
    else:
        sold_date = ERROR_0
    return sold_date

def link(item):
    link = item.find('a', {'class': 's-item__link'})['href']
    if link:
        link = link
    else:
        link = ERROR_0
    return link


def loadup(product_list):
    return

def export(product_list, search_term):
    productsdf = pd.DataFrame(product_list)
    productsdf.to_csv(search_term +'.csv', index=False)
    print('Saved to CSV')
    return


if __name__ == '__main__':
    main()

