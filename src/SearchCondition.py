"""
This class maintains all search conditions and returns results with products that satisfy all search condifion.
"""
import enum


class SearchCondition:
    def __init__(self):
        self.search_condition = dict()
        self.condition_type = None
        self.condition_values = []

    def build(self, condition_dict):
        if 'type' in condition_dict or 'values' in condition_dict:
            self.condition_type = condition_dict["type"]
            self.condition_values = condition_dict["values"]

    def is_satisfied(self, product):
        if (self.condition_type == "productId") and (product.get_id() in self.condition_values):
            return True
        elif (self.condition_type == "productTitle") and (product.get_title() in self.condition_values):
            return True
        elif (self.condition_type == "brandId") and (product.get_brand_id() in self.condition_values):
            return True
        elif (self.condition_type == "brandName") and (product.get_brand_name() in self.condition_values):
            return True
        elif (self.condition_type == "categoryId") and (product.get_category_id() in self.condition_values):
            return True
        elif (self.condition_type == "categoryName") and (product.get_category_name() in self.condition_values):
            return True
        else:
            return False


class ConditionType(enum.Enum):
    productId = 1
    productTitle = 2
    brandId = 3
    brandName = 4
    categoryId = 5
    categoryName = 6


class SearchConditions:
    def __init__(self):
        self.conditions = []

    def add_condition(self, search_condition):
        self.conditions.append(search_condition)
