"""
This class takes input raw_data file and outputs a product container.
i/p: File path for local file.
o/p: DS a product container which has all products inside it
"""
import csv
from .product_container import ProductContainer
import logging


class ProductBuilder:

    def __init__(self):
        self.product_container = ProductContainer()

    @classmethod
    def clean_product(cls, raw_product):
        """
        This function should be used to clean product data. As of now, its a shell method. Could be implemented later
        :param raw_product:
        :return:
        """
        return raw_product

    def build(self, data_path):
        list_of_raw_products = []
        if data_path is None:
            raise Exception("Data path not specified")

        with open(data_path) as tsv_data_file:
            reader = csv.reader(tsv_data_file, delimiter='\t')
            for each_raw_product in reader:
                clean_product_data = self.clean_product(each_raw_product)
                product_entities = clean_product_data.split("\t")

                if len(product_entities) == 6:
                    list_of_raw_products.append(product_entities)
                else:
                    logging.log("Bad product data found")

        return self.product_container.set_products(list_of_raw_products)



