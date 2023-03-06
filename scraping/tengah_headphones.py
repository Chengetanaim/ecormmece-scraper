from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



tengah_headphones_names = []
tengah_headphones_prices = []
tengah_headphones_images = []
tengah_headphones_links = []

my_url = 'https://10ngah.com/861-earbuds-headphones'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll('div', {'class': 'tvproduct-wrapper grid'})
for container in containers:
    images = container.findAll('div', {'class': 'tvproduct-image'})
    for image in images:
        links = image.a['href']
        img = image.a.img['src']
        tengah_headphones_images.append(img)
        tengah_headphones_links.append(links)
    information = container.findAll('div', {'class': 'tvproduct-info-box-wrapper'})
    for info in information:
        descriptions = info.findAll('div', {'class': 'product-description'})
        for description in descriptions:
            titles = description.findAll('div', {'class': 'tvproduct-name product-title'})

            for title in titles:
                tengah_headphones_names.append(title.a.h6.text)
                # print(title.a.h6.text)

            prices = description.findAll('div', {'class': 'tv-product-price tvproduct-name-price-wrapper'})
            for price in prices:
                actual_price = price.div.span.text
                tengah_headphones_prices.append(actual_price)
#
# print(tengah_headphones_names)
# print(len(tengah_headphones_names))