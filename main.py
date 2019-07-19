import flask
from flask import request, jsonify
import json
from src.product_container_builder import ProductContainerBuilder
from src.product import ProductTypes
from src.AutoComplete import AutoComplete

app = flask.Flask(__name__)
product_path = "data/sample_product_data.tsv"

product_container_builder = ProductContainerBuilder()
product_container = product_container_builder.build_container(product_path)
products = product_container.get_products()

auto_complete_index_server = AutoComplete()
auto_complete_index_server.build(products)


@app.route('/', methods=['GET'])
def get_tasks():
    return "Hi, I got the task"


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)


# find a book in the list
@app.route('/api/v1/resources/books', methods=['GET'])
def search_engine_api():
    """
    Search wrt ID
    :return:
    """
    results = []
    for i in range(10):
        results.append(products[i].title)
    return jsonify(results)


@app.route('/api/products/autocomplete', methods=['POST'])
def auto_complete_api():
    request_dict = json.loads(request.data)
    if 'type' in request_dict and request_dict['type'] in ProductTypes.__members__:
        return jsonify(auto_complete_index_server.search(request_dict))
    else:
        return jsonify({})


@app.route("/search/<string:box>")
def search_api(box):
    """
    Autocomplete API
    :param box:
    :return:
    """
    if box == 'names':
        suggestions = [{'value': 'joe', 'data': 'joe'}, {'value': 'jim', 'data': 'jim'}]
    if box == 'songs':
        suggestions = [{'value': 'song1', 'data': '123'}, {'value': 'song2', 'data': '234'}]
    return jsonify({"suggestions": suggestions})


@app.route('/update', methods=['GET', 'POST', 'PUT'])
def keywords_api():
    return "upadte"


if __name__ == '__main__':
    app.run(debug=True)