#!/usr/bin/env python
# encoding: utf-8

""" Sample food truck acquisition webapp, take two """

from flask import Flask, request, abort
import os
import json
import requests
from bs4 import BeautifulSoup

APP = Flask(__name__)

URL = "http://arusahni.net/slack-demo/listing.html"

TOKEN = None # REPLACE THIS WITH YOUR SLACK TOKEN
# WEBHOOK_URL = "https://hooks.slack.com/services/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"
WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

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

    On a success, it posts the food truck data to an external webservice.

    :returns: A blank page on success, an error message otherwise.

    """
    if TOKEN and request.args.get("token") != TOKEN:
        abort(401) # Unauthorized
    payload = json.dumps({
        "text": ", ".join(scrape_food_trucks())
    })
    resp = requests.post(WEBHOOK_URL, data={"payload": payload})
    if resp.status_code != 200:
        return "ERROR - HTTP {}: {}".format(resp.status_code, resp.text), resp.status_code
    return ""

if __name__ == '__main__':
    APP.run(debug=True, port=9000)
