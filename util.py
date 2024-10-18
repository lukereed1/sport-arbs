from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError


def get_soup(url, strainer):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        return BeautifulSoup(response.content, "lxml", parse_only=strainer)
    except HTTPError as hp:
        print(f"Http Error: {hp}")

