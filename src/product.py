"""
This defines data structure of each product in database.
"""
import enum


class Product:

    def __init__(self):
        self.id = None
        self.title = None
        self.brand_id = None
        self.brand_name = None
        self.category_id = None
        self.category_name = None

        # Define types
        types = set()
        types.add(ProductTypes.brand)
        types.add(ProductTypes.category)
        types.add(ProductTypes.name)
        self.types = types

    def set_product(self, raw_data):
        list_of_entities = raw_data
        self.id = list_of_entities[0]
        self.title = list_of_entities[1]
        self.brand_id = list_of_entities[2]
        self.brand_name = list_of_entities[3]
        self.category_id = list_of_entities[4]
        self.category_name = list_of_entities[5]

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_brand_id(self):
        return self.brand_id

    def get_brand_name(self):
        return self.brand_name

    def get_category_id(self):
        return self.category_id

    def get_category_name(self):
        return self.category_name


class ProductTypes(enum.Enum):
    name = 1
    category = 2
    brand = 3