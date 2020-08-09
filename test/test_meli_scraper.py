import json
from unittest import TestCase

from src.transform.preprocessing import preprocess_article
from src.transform.tree import Tree
from src.analysis.counter import count_products


def test_preprocess_article(MELI_xiaomi_data, MELI_xiaomi_data_normalized):
    normalized = list(map(preprocess_article, MELI_xiaomi_data))
    assert normalized == MELI_xiaomi_data_normalized


def test_tree_generation(MELI_xiaomi_data_normalized):
    articles_tree = Tree(MELI_xiaomi_data_normalized)
    expected_tree = json.loads('{"redmi": {"counter": 4, "note": {"counter": 3, "8": {"counter": 2, "azulado": {"counter": 1, "3": {"counter": 1, "32gb": {"counter": 1}}}, "pro": {"counter": 1, "6gb": {"counter": 1, "64gb": {"counter": 1, "dual": {"counter": 1, "blanco": {"counter": 1}}}}}}, "9": {"counter": 1, "pro": {"counter": 1, "128gb": {"counter": 1}}}}, "9": {"counter": 1, "4gb": {"counter": 1, "64gb": {"counter": 1, "dual": {"counter": 1, "gris": {"counter": 1}}}}}}, "note": {"counter": 2, "8t": {"counter": 1, "32gb": {"counter": 1, "128gb": {"counter": 1}}}, "9": {"counter": 1, "pro": {"counter": 1}}}}')
    assert articles_tree.json_tree == expected_tree
    assert articles_tree.max_depth == max([len(model.split()) for model in MELI_xiaomi_data_normalized])


def test_product_count(MELI_xiaomi_data_normalized):
    articles_tree = Tree(MELI_xiaomi_data_normalized)
    count_p = count_products(articles_tree.json_tree)
    assert count_p == 6


def test_full_process(MELI_xiaomi_data):
    normalized = list(map(preprocess_article, MELI_xiaomi_data))
    articles_tree = Tree(normalized)
    count_p = count_products(articles_tree.json_tree)
    assert count_p == 6
