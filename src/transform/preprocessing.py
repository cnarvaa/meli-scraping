from src.settings import URL_PATTERN
from src.settings import GB_PATTERN
from src.settings import GB_MERGED_PATTERN
from src.settings import KEY_PATTERN
from src.settings import COLLECTION_COLORS
from src.settings import COLLECTION_XIAOMI_WORDS
from src.settings import COLLECTION_GB


def preprocess_article(article: str) -> str:
    """text normalization based in expert knowledge and web data

    Normalization process
    * lowercase and strip
    * Gigabytes normalization -> <number> gb -> <number>gb
    * Send Xiaomi and the rest of the message to the start of the article
    * Filter the words that are not part of the expert knowledge or web data

    Args:
        article (str): text to normalize

    Returns:
        str: normalized text
    """
    article = URL_PATTERN.sub('', article.get_text()).lower().strip()
    article = GB_PATTERN.sub(r'\2gb', article)
    article = GB_MERGED_PATTERN.sub(r'\2gb \3gb', article)
    article = KEY_PATTERN.sub(r'\3 \2', article)
    article = " ".join([word for word in article.split() if (
        word in COLLECTION_XIAOMI_WORDS or word in COLLECTION_GB or word in COLLECTION_COLORS)])
    return article
