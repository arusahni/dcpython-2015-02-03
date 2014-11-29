#!/usr/bin/env python3
# encoding: utf-8

import requests
from bs4 import BeautifulSoup

URL = "http://arusahni.net/slack-demo/listing.html"

def get_trucks():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    trucks = soup.find_all("li")
    return [truck.text for truck in trucks]

if __name__ == '__main__':
    print(get_trucks())
