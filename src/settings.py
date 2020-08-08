import re
from nltk.corpus import stopwords

SEARCH_WORD = 'xiaomi'
MELI_URL = f'https://listado.mercadolibre.com.ar/{SEARCH_WORD}#D[A:{SEARCH_WORD}]'
GSMARENA_URL = 'https://www.gsmarena.com/'
GSMARENA_PRODUCT = 'xiaomi-phones-80.php'

MAX_THREADS = 10

STOPWORDS = set(stopwords.words("spanish"))-set(["mi"])
URL_PATTERN = re.compile(r'[^\w\s]')
GB_PATTERN = re.compile(r"(([0-9]*) gb)")
GB_MERGED_PATTERN = re.compile(r"(([0-9]*)gb([0-9]*)gb)")
KEY_PATTERN = re.compile(r'(([^\n\r]*)\s+({}\s[^\n\r]*))'.format(SEARCH_WORD))
COLLECTION_WORDS = ("celular", "permuto", "vendo", "smartphone", "izalo",
                    "telefono", "xiaomi", "xioami", "xiomi", "xiaomo")

DOCS_LOCATION = "docs"
