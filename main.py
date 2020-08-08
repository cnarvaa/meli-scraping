from src.settings import GSMARENA_URL
from src.settings import GSMARENA_PRODUCT
from src.settings import MELI_URL
from src.data.scraping import get_xiaomi_models
from src.data.scraping import get_xiaomi_links
from src.data.scraping import get_meli_links
from src.data.scraping import get_articles_titles
from src.transform.tree import Tree
from src.settings import DOCS_LOCATION

# all_xiaomi_models = get_xiaomi_models(get_xiaomi_links(GSMARENA_URL, GSMARENA_PRODUCT))
# print(all_xiaomi_models)

articles_titles = get_articles_titles(get_meli_links(MELI_URL))
print(sorted(articles_titles))
articles_tree = Tree(articles_titles)
for i in range(2, 6):
    articles_tree.write_tree(f"{DOCS_LOCATION}/graph_level_{i}.png", i)
    # articles_tree.write_tree(f"{DOCS_LOCATION}/graph_level_{i}_ns.png", i, simplify=False)
print()
