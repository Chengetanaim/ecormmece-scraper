import requests, bs4

classifieds_cellphones_names = []
classifieds_cellphones_prices = []
classifieds_cellphones_images = []
classifieds_cellphones_links = []

urls = ['https://www.classifieds.co.zw/zimbabwe-cell-phones', 'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=2'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=3'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=4'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=5'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=6'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=7'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=8'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=9'
                                                              'https://www.classifieds.co.zw/zimbabwe-cell-phones?page=10']
# url = 'https://www.classifieds.co.zw/zimbabwe-cell-phones'
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
                classifieds_cellphones_images.append(images)
                classifieds_cellphones_links.append(links)
        details = container.findAll('div', {'class': 'details col-md-7 col-sm-7 col-xs-8'})
        for detail in details:
            name = detail.h5.text
            # print(name.strip())
            classifieds_cellphones_names.append(name.strip())
            prices = detail.div.div.div.div.text
            # print(prices.strip())
            classifieds_cellphones_prices.append(prices.strip())
# print(len(classifieds_cellphones_names))