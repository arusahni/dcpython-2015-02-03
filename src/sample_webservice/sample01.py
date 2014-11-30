#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
import requests
from bs4 import BeautifulSoup

import logging

APP = Flask(__name__)

URL = "http://arusahni.net/slack-demo/listing.html"

def scrape_food_trucks():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    trucks = soup.find_all("li")
    return [truck.text for truck in trucks]

@APP.route("/trucks")
def get_trucks():
	return ", ".join(scrape_food_trucks())

if __name__ == '__main__':
	APP.run(debug=True, port=9000)
