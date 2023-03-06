import requests, bs4

zimall_audio_names = []
zimall_audio_prices = []
zimall_audio_images = []
zimall_audio_links = []

url = 'https://www.zimall.co.zw/shop/categories/12/personal-audio.html'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
containers = soup.findAll('div', {'class': 'product-container'})
for container in containers:
    left_block = container.findAll('div', {'class': 'left-block'})
    for lb in left_block:
        link = lb.div.a['href']
        zimall_audio_links.append(link)
        image = lb.div.a.img['src']
        zimall_audio_images.append(image)
    right_block = container.findAll('div', {'class': 'right-block'})
    for rb in right_block:
        name = rb.div.h4.a.text
        zimall_audio_names.append(name)
        product_meta = rb.findAll('div', {'class': 'product-meta'})
        for pm in product_meta:
            content_price = pm.findAll('div', {'class': 'content_price price'})
            for cp in content_price:
                price = cp.div.span.text
                zimall_audio_prices.append(price)



