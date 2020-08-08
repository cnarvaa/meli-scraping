from itertools import chain
from itertools import repeat
from typing import List
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import concurrent.futures

from src.settings import MAX_THREADS
from src.transform.preprocessing import preprocess_article


def get_content(name: str, attributes: dict, url: str, limit: int = None):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print("Server not found")
        return None
    try:
        bs = BeautifulSoup(html, "html.parser")
        element = bs.find_all(name, attributes, limit=limit)
    except AttributeError as e:
        print(e)
        return None
    return element


def get_meli_links(url: str, limit: int = 5):
    page_links = get_content('a', {'class': 'andes-pagination__link'}, url, limit)[1:]
    page_links = [link.attrs["href"] for link in page_links]
    return [url]+page_links


def get_articles_titles(urls: List[str]):
    threads = min(MAX_THREADS, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        records = executor.map(get_content, repeat('span'), repeat({'class': 'main-title'}), urls)
    return set(map(preprocess_article, chain(*records)))


# Getting all the Xiaomi phones from gsmarena since mi.com doesn't have all the models
def get_xiaomi_links(url: str, product: str):
    page_links = get_content('div', {'class': 'nav-pages'}, url+product)
    page_links = [url+link.attrs["href"] for link in page_links[0].find_all("a")]
    return [url+product]+page_links


def get_xiaomi_models(urls: str):
    threads = min(MAX_THREADS, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        records = executor.map(get_content, repeat('div'), repeat({'class': 'makers'}), urls)
    return sorted([model.get_text().lower() for record in records for model in record[0].find_all("span")])
