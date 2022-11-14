from pynytimes import NYTAPI

import os
from dotenv import load_dotenv
import datetime


load_dotenv() # look in the ".env" file for env vars

API_KEY = os.getenv("NY_API_KEY")

nyt = NYTAPI("2", parse_dates=True)

articles = nyt.article_search(
    query = "Obama",
    results = 30,
    dates = {
        "begin": datetime.datetime(2019, 1, 31),
        "end": datetime.datetime(2019, 2, 28)
    },
    options = {
        "sort": "oldest",
        "sources": [
            "New York Times",
            "AP",
            "Reuters",
            "International Herald Tribune"
        ],
        "news_desk": [
            "Politics"
        ],
        "type_of_material": [
            "News Analysis"
        ]
    }
)

print(articles)