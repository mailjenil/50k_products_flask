"""
This class dispatches search. First builds Search dispatcher and then uses it.
"""
from src.SearchCondition import SearchCondition
from src.SearchResults import SearchResults


class SearchDispatcher:
    def __init__(self, products):
        self.products = products
        self.search_conditions = list()

    def build_conditions(self, request):
        conditions = request['conditions']
        if len(conditions) == 0:
            return {}

        for condition in conditions:
            search_condition = SearchCondition()
            search_condition.build(condition)
            self.search_conditions.append(search_condition)

    def search(self):
        result_products = list()
        for product in self.products:
            for condition in self.search_conditions:
                if condition.is_satisfied(product) is True:
                    result_products.append(product)

        search_results = SearchResults()
        search_results.build(result_products)
        return search_results
