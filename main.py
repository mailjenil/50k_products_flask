import flask
from flask import request, jsonify
import json
from src.product_container_builder import ProductContainerBuilder
from src.product import ProductTypes
from src.AutoComplete import AutoComplete
from src.SearchDispatcher import SearchDispatcher
from src.KeywordsDB import KeywordsDB

app = flask.Flask(__name__)
product_path = "data/sample_product_data.tsv"

product_container_builder = ProductContainerBuilder()
product_container = product_container_builder.build_container(product_path)
products = product_container.get_products()

auto_complete_index_server = AutoComplete()
auto_complete_index_server.build(products)

search_dispatcher = SearchDispatcher(products)

keywords_db = KeywordsDB()
keywords_db.build(products)


@app.route('/api/products/autocomplete', methods=['POST'])
def auto_complete_api():
    request_dict = json.loads(request.data)
    if 'type' in request_dict and request_dict['type'] in ProductTypes.__members__:
        return jsonify(auto_complete_index_server.search(request_dict))
    else:
        return jsonify({})


@app.route('/api/products/search', methods=['POST'])
def search_api():
    """
     Search API
    :param box:
    :return:
    """
    request_dict = json.loads(request.data)
    if 'conditions' not in request_dict:
        return jsonify({})
    search_dispatcher.build_conditions(request_dict)
    search_results = search_dispatcher.search()
    return jsonify(search_results.get_results(request_dict["pagination"]["from"], request_dict["pagination"]["size"]))


@app.route('/api/products/keywords', methods=['POST'])
def keywords_api():
    request_dict = json.loads(request.data)
    print(request_dict)
    if 'keywords' not in request_dict:
        return jsonify({})

    final_output = keywords_db.find_all_frequencies(request_dict)
    return jsonify(final_output)


if __name__ == '__main__':
    app.run(debug=True)