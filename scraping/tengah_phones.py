from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



tengah_phones_names = []
tengah_phones_prices = []
tengah_phones_images = []
tengah_phones_links = []

# my_url = 'https://10ngah.com/968-kindle-tablets'
urls = ['https://10ngah.com/968-kindle-tablets', 'https://10ngah.com/283-cellphones', 'https://10ngah.com/17-motorola',
        'https://10ngah.com/703-phone-deals']
for url in urls:
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()


    page_soup = soup(page_html, "html.parser")


    containers = page_soup.findAll('div', {'class': 'tvproduct-wrapper grid'})
    for container in containers:
        images = container.findAll('div', {'class': 'tvproduct-image'})
        for image in images:
            links = image.a['href']
            img = image.a.img['src']
            tengah_phones_images.append(img)
            tengah_phones_links.append(links)
        information = container.findAll('div', {'class': 'tvproduct-info-box-wrapper'})
        for info in information:
            descriptions = info.findAll('div', {'class': 'product-description'})
            for description in descriptions:
                titles = description.findAll('div', {'class': 'tvproduct-name product-title'})

                for title in titles:
                    tengah_phones_names.append(title.a.h6.text)
                    # print(title.a.h6.text)

                prices = description.findAll('div', {'class': 'tv-product-price tvproduct-name-price-wrapper'})
                for price in prices:
                    actual_price = price.div.span.text
                    tengah_phones_prices.append(actual_price)

# print(tengah_phones_names)
# print(len(tengah_phones_names))