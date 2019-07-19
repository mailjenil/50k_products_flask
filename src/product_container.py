"""
This class holds all products in database. This will expose a datastructure of List<Product> for client to consume.
Input: all_products_raw_data: List<String> : Each String is a single row in a file
"""

from .product import Product


class ProductContainer:

    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def set_products(self, all_products_raw_data):
        for each_product in all_products_raw_data:
            product = Product()
            product.set_product(each_product)

        self.products.append(product)
