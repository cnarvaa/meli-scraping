from src.settings import URL_PATTERN
from src.settings import GB_PATTERN
from src.settings import GB_MERGED_PATTERN
from src.settings import KEY_PATTERN
from src.settings import STOPWORDS
from src.settings import COLLECTION_WORDS

from typing import List


def remove_stopwords(sentence):
    return [word for word in sentence if word not in STOPWORDS]


def preprocess_article(article) -> List[str]:
    """normalize texts
    * lowercase
    * strip
    * <number> gb -> <number>gb
    * Send Xiaomi and the rest of the message to the start of the article
    """
    article = URL_PATTERN.sub('', article.get_text()).lower().strip()
    article = GB_PATTERN.sub(r'\2gb', article)
    article = GB_MERGED_PATTERN.sub(r'\2gb \3gb', article)
    article = KEY_PATTERN.sub(r'\3 \2', article)
    article = " ".join([word for word in article.split() if not (word in COLLECTION_WORDS or word in STOPWORDS)])
    return article
