def count_products(tree, n_products: int = 0):
    """This function counts the number of products using a recursive approach
    This recursive function stop the leaf exploration when the edge counter is = to 1. Then,
    the sum of the products in the leaf is returned.

    Args:
        tree (tree:dict): The tree you want to count products from
        n_products (int, optional): accumulator for the number of products in each leaf Defaults to 0.

    Returns:
        int: number of products found
    """
    # se detiene cuando el counter se hace 1, en ese caso agrega 1 al producto
    if tree.get("counter") == 1:
        return 1
    for key, sub_tree in tree.items():
        if key != "counter":
            n_products += count_products(sub_tree)
    return n_products
