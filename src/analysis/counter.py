def count_products(tree, n_products=0):
    # se detiene cuando el counter se hace 1, en ese caso agrega 1 al producto
    if tree.get("counter") == 1:
        return 1
    for key, sub_tree in tree.items():
        if key != "counter":
            n_products += count_products(sub_tree)
    return n_products
