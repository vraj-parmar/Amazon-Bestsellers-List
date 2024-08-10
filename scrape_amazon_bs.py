# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_prod_title(prod_title_tags):
    prod_titles = []
    for tag in prod_title_tags:
        prod_titles.append(tag.find("span").text)
    return prod_titles

def get_all_stars(rating_tags):
    stars=[]
    for tag in rating_tags:
        stars.append(tag.find('span').text)
    return stars

def get_all_price(prod_price_tags):
    prod_price=[]
    for tag in prod_price_tags:
        prod_price.append(tag.find('span',{'class':'p13n-sc-price'}).text)
    return prod_price

def get_all_url(prod_url_tag):
    prod_title_urls=[]
    base_url="https://www.amazon.co.uk"
    for tag in prod_url_tag:
        prod_title_urls.append(base_url + tag.find('a',{'class':'a-link-normal'})['href'])
    return prod_title_urls

#This function is used to scrap multiple pages by providing page url
def scrape_page(page_number):
    global url
    title = get_prod_title(prod_title_tags)
    stars = get_all_stars(rating_tags)
    price = get_all_price(prod_price_tags)
    title_url = get_all_url(prod_url_tag)
    return title,stars,price,title_url

url = "https://www.amazon.co.uk/Best-Sellers-Beauty"
response = requests.get(url)
page_contents = response.text

doc = BeautifulSoup(page_contents, "html.parser")

prod_title_tags = doc.find_all("div",{"class": "zg-grid-general-faceout"})

rating = 'a-icon a-icon-star-small a-star-small-4-5 aok-align-top'
rating_tags = doc.find_all('i',{'class': rating})

prod_price_tags = doc.find_all('div',{"class": "zg-grid-general-faceout"})

prod_url_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})

all_titles,all_stars,all_price,all_urls = [], [], [], []
for page_number in range(1,3):
    title,stars,price,title_url= scrape_page(page_number)
    all_titles += title
    all_stars += stars
    all_price += price
    all_urls += title_url

all_prod = {
             'Product': all_titles,
             'Rating': all_stars ,
             'Price': all_price ,
             'URL':all_urls}

dataframe = pd.DataFrame.from_dict(all_prod, orient='index')
dataframe = dataframe.transpose()

dataframe.to_csv("products2.csv")