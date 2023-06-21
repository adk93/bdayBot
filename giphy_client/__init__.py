import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

GIPHY_API_KEY = os.getenv("giphy_api_key")


def get_giphy_url() -> str:
    base_url = "https://api.giphy.com/v1/gifs/search"

    params = {
        "api_key": GIPHY_API_KEY,
        "q": "happy birthday",
        "limit": 1,
        "rating": "pg-13",
        "offset": random.randint(1, 100)
    }

    r = requests.get(base_url, params=params)

    return r.json().get("data")[0].get('images').get('downsized').get('url')#.get("preview_gif").get("url")

