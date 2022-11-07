import pandas as pd


_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

def is_product_available(product_name, quantity):
    """Checks if a product is available in the database.
    Args:
        product_name (str): Name of the product.
        quantity (int): Quantity of the product.
    Returns:
        bool: True if the product is available, False otherwise.
    """

    product = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]

    if product.empty:
        return False
        
    return product["quantity"].values[0] >= quantity


