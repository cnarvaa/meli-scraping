from itertools import chain
from itertools import repeat
from typing import List
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import concurrent.futures
from bs4 import BeautifulSoup

from src.settings import MAX_THREADS
from src.transform.preprocessing import preprocess_article


def get_content(name: str, attributes: dict, url: str, limit: int = None):
    """Get data from the web and extract the specified name

    Args:
        name (str): HTML element to extract
        attributes (dict): additional HTML attributes to extract
        url (str): url to scrap
        limit (int, optional): number of elements to return from the scrapping. Defaults to None.

    Returns:
        bs element: the HTML elements found, bs4 format
    """
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
    """Extract MELI links to paginate requests

    Args:
        url (str): url to scrap
        limit (int, optional): max number of results to return. Defaults to 5.

    Returns:
        List[str]: page urls to paginate
    """
    page_links = get_content('a', {'class': 'andes-pagination__link'}, url, limit)[1:]
    page_links = [link.attrs["href"] for link in page_links]
    return [url]+page_links


def get_articles_titles(urls: List[str]):
    """Thread function to download data from different links

    Args:
        urls (List[str]): urls to scrap

    Returns:
        set: articles' title found in the scraped urls
    """
    threads = min(MAX_THREADS, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        records = executor.map(get_content, repeat('span'), repeat({'class': 'main-title'}), urls)
    return set(map(preprocess_article, chain(*records)))


def get_xiaomi_links(url: str, product: str):
    """links to scrap to obtain Xiaomi models info
    Getting all the Xiaomi phones from gsmarena since mi.com doesn't have all the models

    Args:
        url (str): url to scrap
        product (str): product to scrap

    Returns:
        List[str]: the links to paginate the scraping
    """
    page_links = get_content('div', {'class': 'nav-pages'}, url+product)
    page_links = [url+link.attrs["href"] for link in page_links[0].find_all("a")]
    return [url+product]+page_links


def get_xiaomi_models(urls: str):
    """Thread function to download data from different links

    Args:
        urls (List[str]): urls to scrap

    Returns:
        List[str]: sorted list with the scraped elements
    """
    threads = min(MAX_THREADS, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        records = executor.map(get_content, repeat('div'), repeat({'class': 'makers'}), urls)
    return sorted([model.get_text().lower() for record in records for model in record[0].find_all("span")])
