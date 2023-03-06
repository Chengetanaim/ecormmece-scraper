from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd


my_url = 'https://10ngah.com/704-laptop-deals'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

tengah_laptop_names = []
tengah_laptop_prices = []
tengah_laptop_images = []
tengah_laptop_links = []

containers = page_soup.findAll('div', {'class': 'tvproduct-wrapper grid'})
for container in containers:
    images = container.findAll('div', {'class': 'tvproduct-image'})
    for image in images:
        links = image.a['href']
        img = image.a.img['src']
        tengah_laptop_images.append(img)
        tengah_laptop_links.append(links)
    information = container.findAll('div', {'class': 'tvproduct-info-box-wrapper'})
    for info in information:
        descriptions = info.findAll('div', {'class': 'product-description'})
        for description in descriptions:
            titles = description.findAll('div', {'class': 'tvproduct-name product-title'})

            for title in titles:
                tengah_laptop_names.append(title.a.h6.text)
                # print(title.a.h6.text)

            prices = description.findAll('div', {'class': 'tv-product-price tvproduct-name-price-wrapper'})
            for price in prices:
                actual_price = price.div.span.text
                tengah_laptop_prices.append(actual_price)
                # print(actual_price)


# dict = {
#     'Laptops': tengah_laptop_names,
#     'Prices': tengah_laptop_prices
# }
#
# df = pd.DataFrame(dict)
#
# df.to_csv('tengah_Laptops.csv')
# print('Done')