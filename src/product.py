"""
This defines data structure of each product in database.
"""


class Product:

    def __init__(self):
        self.id = None
        self.title = None
        self.brand_id = None
        self.brand_name = None
        self.category_id = None
        self.category_name = None

    def set_product(self, raw_data):
        list_of_entities = raw_data.split("\t")
        self.id = list_of_entities[0]
        self.title = list_of_entities[1]
        self.brand_id = list_of_entities[2]
        self.brand_name = list_of_entities[3]
        self.category_id = list_of_entities[4]
        self.category_name = list_of_entities[5]
