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
KEY_PATTERN = re.compile(r'(([^\n\r]*)\s+({}\s[^\n\r]*))'.format(SEARCH_WORD))  # Send the model to the string start

COLLECTION_WORDS = ("celular", "permuto", "vendo", "smartphone", "izalo",
                    "telefono", "xiaomi", "xioami", "xiomi", "xiaomo")

COLLECTION_COLORS = ("red", "yellow", "blue", "orange", "green", "violent", "purple", "black", "white", "gold", "grey", "transparent",
                     "rojo", "amarillo", "azul", "anaranjado", "naranja", "verde", "morado", "violeta", "negro", "blanco", "dorado", "transparente", "gris")

# Selected from the scraped results in Xiaomi model
COLLECTION_XIAOMI_WORDS = ('10', '10x', '1s', '2', '2a', '2s', '3', '3s', '3x', '4', '4a', '4c', '4g', '4i', '4s', '4x', '5', '5a', '5c', '5g', '5s', '5x', '6', '6a', '6c', '6x', '7', '79', '7a', '7s', '8', '8a', '8t', '9', '9a', '9c', '9s', '9t', '9x', 'a1', 'a2', 'a3', 'ai', 'alpha', 'black', 'camera', 'cc9', 'cc9e',
                           'china', 'color', 'dual', 'explorer', 'f1', 'f2', 'go', 'helo', 'india', 'k20', 'k30', 'k30i', 'lite', 'lte', 'm2', 'max', 'mediatek', 'mi', 'mix', 'note', 'pad', 'play', 'plus', 'poco', 'pocophone', 'premium', 'prime', 'pro', 'racing', 'redmi', 's2', 'se', 'shark', 'watch', 'x2', 'y1', 'y2', 'y3', 'youth', 'zoom')

COLLECTION_GB = ('1286gb',
                 '128gb',
                 '12gb'
                 '16gb',
                 '256gb',
                 '2gb',
                 '32gb',
                 '332gb',
                 '3gb',
                 '464gb',
                 '4gb',
                 '64gb',
                 '664gb',
                 '6gb',
                 '8gb')  # checked based in the words that wont appear

DOCS_LOCATION = "docs"
