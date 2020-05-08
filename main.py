# web scraping
import bs4
import webbrowser
import requests

# host info
import datetime
import socket
import pygeoip

# misc
import random

country = 'us'
now = datetime.datetime.now()
year = str(now.year)

def getIP():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address

def getCountryCode():
    #implement later
    return 0

def genURL(model, size, gender):
    base = 'https://www.adidas.com/'
    country_url = country + '/'
    model_url = model + '.html?forceSelSize='
    size_url = ""
    if(gender == 'M' or gender == 'F'):
        size_url = str(size)
    else:
        male_size = size
        female_size = int(size) + 1
        size_url = 'M%' + year[2:4] + str(male_size) + "%20%2F%20W%20" + str(female_size)
    url = base + country_url + model_url + size_url
    return url

def checkStock():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = genURL('EG0710', 10, 'M')
    res = requests.get(url, timeout=1, headers=headers)
    page = bs4.BeautifulSoup(res.text, "lxml")
    print(page.title.string)


def main():
    model = input('Model: #')
    size = input('Size: ')
    gender = input('Gender (M/F/O): ')
    url = genURL(model.upper(), size, gender.upper())
    print(url)

checkStock()
#main()