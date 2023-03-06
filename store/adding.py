from .models import Product, Category, Website


# 10NGAH PRODUCTS
from scraping.tengah_laptops import tengah_laptop_names, tengah_laptop_prices, tengah_laptop_images, tengah_laptop_links
from scraping.classifieds_laptops import classifieds_laptop_names, classifieds_laptop_prices, classifieds_laptop_links, \
    classifieds_laptop_images
from scraping.tengah_phones import tengah_phones_names, tengah_phones_prices, tengah_phones_images, tengah_phones_links

# CLASSIFIEDS PRODUCTS
from scraping.classifieds_phones import classifieds_cellphones_prices, classifieds_cellphones_names, \
    classifieds_cellphones_links, classifieds_cellphones_images
from scraping.tengah_headphones import tengah_headphones_names, tengah_headphones_prices, tengah_headphones_images, \
    tengah_headphones_links
from scraping.classifieds_headphones import classifieds_headphones_names, classifieds_headphones_prices, \
    classifieds_headphones_links, classifieds_headphones_images

# ZIMALL PRODUCTS
from scraping.zimall_audio import zimall_audio_images, zimall_audio_links, zimall_audio_names, zimall_audio_prices
from scraping.zimall_laptops import zimall_laptops_images, zimall_laptops_links, zimall_laptops_names,\
    zimall_laptops_prices
from scraping.zimall_phones import zimall_cellphones_images, zimall_cellphones_links, zimall_cellphones_names,\
    zimall_cellphones_prices


description = 'Wanna see more products like this?  Our rich database has an abundance of quality products that caters' \
              ' for your need, all you gotta do is to keep scrolling!'


def process():
    laptops = Category.objects.get(name='Laptops')
    cellphones = Category.objects.get(name='Cellphones')
    headphones = Category.objects.get(name='Headphones')
    tengah_website = Website.objects.get(name='10ngah')
    classifieds_website = Website.objects.get(name='Classifieds')
    zimall_website = Website.objects.get(name='Zimall')

    # Insert 10ngah laptops into database
    for name, price, image, link in zip(tengah_laptop_names, tengah_laptop_prices, tengah_laptop_images,
                                        tengah_laptop_links):
        Product.objects.get_or_create(category=laptops, name=name,
                                      price=price, website=tengah_website,
                                      image=image, url=link,
                                      description=description)

    # Insert Classifieds laptops into database
    for name, price, image, link in zip(classifieds_laptop_names, classifieds_laptop_prices, classifieds_laptop_images,
                                        classifieds_laptop_links):
        Product.objects.get_or_create(category=laptops,
                                      name=name,
                                      price=price,
                                      website=classifieds_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert 10ngah phones into database
    for name, price, image, link in zip(tengah_phones_names, tengah_phones_prices, tengah_phones_images,
                                        tengah_phones_links):
        Product.objects.get_or_create(category=cellphones,
                                      name=name,
                                      price=price,
                                      website=tengah_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert Classifieds phones into database
    for name, price, image, link in zip(classifieds_cellphones_names, classifieds_cellphones_prices,
                                        classifieds_cellphones_images, classifieds_cellphones_links):
        Product.objects.get_or_create(category=cellphones,
                                      name=name,
                                      price=price,
                                      website=classifieds_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert 10ngah headphones into database
    for name, price, image, link in zip(tengah_headphones_names, tengah_headphones_prices, tengah_headphones_images,
                                        tengah_headphones_links):
        Product.objects.get_or_create(category=headphones,
                                      name=name,
                                      price=price,
                                      website=tengah_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert Classifieds headphones into database
    for name, price, image, link in zip(classifieds_headphones_names, classifieds_headphones_prices,
                                        classifieds_headphones_images, classifieds_headphones_links):
        Product.objects.get_or_create(category=headphones,
                                      name=name,
                                      price=price,
                                      website=classifieds_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert Zimall laptops into database
    for name, price, image, link in zip(zimall_laptops_names, zimall_laptops_prices, zimall_laptops_images,
                                        zimall_cellphones_links):
        Product.objects.get_or_create(category=laptops, name=name,
                                      price=price, website=zimall_website,
                                      image=image, url=link,
                                      description=description)

    # Insert Zimall phones into database
    for name, price, image, link in zip(zimall_cellphones_names, zimall_cellphones_prices, zimall_cellphones_images,
                                        zimall_cellphones_links):
        Product.objects.get_or_create(category=cellphones,
                                      name=name,
                                      price=price,
                                      website=zimall_website,
                                      image=image,
                                      url=link,
                                      description=description)

    # Insert Zimall headphones into database
    for name, price, image, link in zip(zimall_audio_names, zimall_audio_prices, zimall_audio_images,
                                        zimall_audio_links):
        Product.objects.get_or_create(category=headphones,
                                      name=name,
                                      price=price,
                                      website=zimall_website,
                                      image=image,
                                      url=link,
                                      description=description)
