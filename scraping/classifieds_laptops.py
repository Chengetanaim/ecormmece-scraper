# from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests, bs4

classifieds_laptop_names = []
classifieds_laptop_prices = []
classifieds_laptop_images = []
classifieds_laptop_links = []

urls = ['https://www.classifieds.co.zw/zimbabwe-laptops', 'https://www.classifieds.co.zw/zimbabwe-laptops?page=2',
        'https://www.classifieds.co.zw/zimbabwe-laptops?page=10', 'https://www.classifieds.co.zw/zimbabwe-laptops?page=3'
                                                                  'https://www.classifieds.co.zw/zimbabwe-laptops?page=4'
                                                                  'https://www.classifieds.co.zw/zimbabwe-laptops?page=5'
                                                                  'https://www.classifieds.co.zw/zimbabwe-laptops?page=6'
                                                                  'https://www.classifieds.co.zw/zimbabwe-laptops?page=7'
                                                                  'https://www.classifieds.co.zw/zimbabwe-laptops?page=8']

# url = 'https://www.classifieds.co.zw/zimbabwe-laptops'
try:
    for url in urls:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        containers = soup.findAll('div', {'class': 'panel-body'})
        for container in containers:
            media = container.findAll('div', {'class': 'pull-left image col-md-5 col-sm-5 col-xs-4'})
            for med in media:
                gallery = med.findAll('div', {'class': 'gallery'})
                for g in gallery:
                    images = 'https://www.classifieds.co.zw' + g.div.div.div.a.img['src']
                    links = g.div.div.div.a['href']
                    classifieds_laptop_images.append(images)
                    classifieds_laptop_links.append(links)
            details = container.findAll('div', {'class': 'details col-md-7 col-sm-7 col-xs-8'})
            for detail in details:
                name = detail.h5.text
                # print(name.strip())
                classifieds_laptop_names.append(name.strip())
                prices = detail.div.div.div.div.text
                # print(prices.strip())
                classifieds_laptop_prices.append(prices.strip())
            # print(details.div.div.div.h3.a['href'])
            # prices = details.findAll('div', {'class': 'panel-title'})
            # # print(prices.div.div.div.string)

except:
    url = 'https://www.classifieds.co.zw/zimbabwe-laptops'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    containers = soup.findAll('div', {'class': 'panel-body'})
    for container in containers:
        media = container.findAll('div', {'class': 'pull-left image col-md-5 col-sm-5 col-xs-4'})
        for med in media:
            gallery = med.findAll('div', {'class': 'gallery'})
            for g in gallery:
                images = 'https://www.classifieds.co.zw' + g.div.div.div.a.img['src']
                links = g.div.div.div.a['href']
                classifieds_laptop_images.append(images)
                classifieds_laptop_links.append(links)
        details = container.findAll('div', {'class': 'details col-md-7 col-sm-7 col-xs-8'})
        for detail in details:
            name = detail.h5.text
            # print(name.strip())
            classifieds_laptop_names.append(name.strip())
            prices = detail.div.div.div.div.text
            # print(prices.strip())
            classifieds_laptop_prices.append(prices.strip())

        # print(details.div.div.div.h3.a['href'])
        # prices = details.findAll('div', {'class': 'panel-title'})
        # # print(prices.div.div.div.string)
# # my_url = 'https://www.classifieds.co.zw/zimbabwe-electronics'
# my_url = 'https://www.classifieds.co.zw/zimbabwe-jobs'
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
#
# page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll('div', {'class': 'panel-body'})
# for container in containers:
#     details = container.findAll('div', {'class': 'details col-md-7 col-sm-7 col-xs-8'})
#     print(details)