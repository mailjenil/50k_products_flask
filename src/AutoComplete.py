"""
This class builds Tries for all types and searches as per prefix
"""
from src.Trie import ProductTrie
from src.product import ProductTypes
from src.Trie import TrieStatus


class AutoComplete:
    def __init__(self):
        self.name_index = ProductTrie()
        self.brand_index = ProductTrie()
        self.category_index = ProductTrie()

    def build(self, products):
        """
        Builds a Trie given complete Product database
        :param products:
        :return:
        """

        name_keys = [product.get_title() for product in products]
        brand_keys = [product.get_brand_name() for product in products]
        category_keys = [product.get_category_name() for product in products]

        self.name_index.form_product_trie(name_keys)
        self.brand_index.form_product_trie(brand_keys)
        self.category_index.form_product_trie(category_keys)

    def search(self, request_data):

        if ProductTypes[request_data['type']] == ProductTypes.brand:
            suggestions = self.brand_index.get_auto_completions(request_data['prefix'])
        elif ProductTypes[request_data['type']] == ProductTypes.category:
            suggestions = self.category_index.get_auto_completions(request_data['prefix'])
        else:
            suggestions = self.name_index.get_auto_completions(request_data['prefix'])

        if suggestions == TrieStatus.not_found or suggestions == TrieStatus.others_not_found:
            return []
        else:
            return suggestions


