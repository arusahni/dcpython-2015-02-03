#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, abort
import json
import requests
from bs4 import BeautifulSoup

import logging

APP = Flask(__name__)

URL = "http://arusahni.net/slack-demo/listing.html"

TOKEN = None # REPLACE THIS WITH YOUR SLACK TOKEN
WEBHOOK_URL = "https://hooks.slack.com/services/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"

def scrape_food_trucks():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text)
    trucks = soup.find_all("li")
    return [truck.text for truck in trucks]

@APP.route("/trucks")
def get_trucks():
    if TOKEN and request.args.get("token") != TOKEN:
        abort(401) # Unauthorized
    payload = json.dumps({
        "text": ", ".join(scrape_food_trucks())
    })
    resp = requests.post(WEBHOOK_URL, data={"payload": payload})
    if resp.status_code != 200:
        return "ERROR - HTTP {}: {}".format(resp.status_code, resp.text)
    return ""

if __name__ == '__main__':
    APP.run(debug=True, port=9000)
