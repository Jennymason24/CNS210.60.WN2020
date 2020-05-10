#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
page = requests.get("http://python.org/downloads/")
import urllib

url = 'https://www.python.org/downloads/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
python_versions = soup.select('.download-list-widget .list-row-container li')
for version in python_versions:
    print(version)