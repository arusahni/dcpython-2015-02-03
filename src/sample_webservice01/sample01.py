#!/usr/bin/env python
# encoding: utf-8

""" Sample food truck acquisition webapp """

from flask import Flask, request, abort
import requests
from bs4 import BeautifulSoup

APP = Flask(__name__)

URL = "http://arusahni.net/slack-demo/listing.html"

TOKEN = None # REPLACE THIS WITH YOUR SLACK TOKEN

def scrape_food_trucks():
    """Acquire food trucks

    :returns: A list of food truck names

    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    trucks = soup.find_all("li")
    return [truck.text for truck in trucks]

@APP.route("/trucks")
def get_trucks():
    """The main entry point.

    :returns: A comma delimited string of food trucks

    """
    if TOKEN and request.args.get("token") != TOKEN:
        abort(401) # Unauthorized
    return ", ".join(scrape_food_trucks())

if __name__ == '__main__':
    APP.run(debug=True, port=9000)
