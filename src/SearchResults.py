"""

"""


class SearchResults:
    def __init__(self):
        self.search_results = []
        self.result_count = 0

    def build(self, products):
        for product in products:
            search_result = SearchResult()
            search_result.set_results(product)
            self.search_results.append(search_result.get_search_result())

        self.result_count = len(self.search_results)

    def get_results(self, from_count=0, size_count=1):
        if from_count * size_count > self.result_count:
            raise Exception("Pagination Exception")

        pagination_start = size_count * from_count
        return self.search_results[pagination_start: pagination_start + size_count]


class SearchResult:
    def __init__(self):
        self.search_result = {}

    def set_results(self, product):
        self.search_result["productId"] = product.get_id()
        self.search_result["title"] = product.get_title()
        self.search_result["brandId"] = product.get_brand_id()
        self.search_result["brandName"] = product.get_brand_name()
        self.search_result["categoryId"] = product.get_category_id()
        self.search_result["categoryName"] = product.get_category_name()

    def get_search_result(self):
        return self.search_result


