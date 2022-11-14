from pynytimes import NYTAPI
from pprint import pprint

import os
from dotenv import load_dotenv
import datetime


load_dotenv() # look in the ".env" file for env vars

API_KEY = os.getenv("NY_API_KEY")

nyt = NYTAPI(API_KEY, parse_dates=True)

articles = nyt.article_search(
    query = "Amazon",
    results = 1,
    dates = {
        "begin": datetime.datetime(2022, 1, 31),
        "end": datetime.datetime(2022, 2, 28)
    },
    options = {
        "sort": "oldest",
        "sources": [
            "New York Times",
            "AP",
            "Reuters",
            "International Herald Tribune"
        ],
        "type_of_material": [
            "News"
        ]
    }
)

pprint(articles)