#!/usr/bin/env python3
# encoding: utf-8

""" Standalone food truck scraping script. """

import requests
from bs4 import BeautifulSoup

URL = "http://arusahni.net/slack-demo/listing.html"

def scrape_food_trucks():
    """Acquire food trucks

    :returns: A list of food truck names

    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    trucks = soup.find_all("li")
    return [truck.text for truck in trucks]

if __name__ == '__main__':
    print(scrape_food_trucks())
