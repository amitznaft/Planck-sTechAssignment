import flask
from flask import Blueprint, jsonify
from fetch_api import fetch_api

pizzas_api = Blueprint('pizzas_api', __name__)
data = fetch_api()

def convert(item):
    return {"Id" : item["dishId"], "Name" : item["dishName"], "Description" : item["dishDescription"], "price" : int(item["dishPrice"])}

@pizzas_api.route('/pizzas', methods=['GET'])
def pizzas():
    result = list(map(convert, data["Data"]["categoriesList"][3]["dishList"]))
    return jsonify({"pizzas" : result})

@pizzas_api.route('/pizzas/<id>', methods=['GET'])
def pizza(id):
    p = data["Data"]["categoriesList"][3]["dishList"]
    j = None
    for pizza in p:
        if pizza["dishId"] == int(id):
            j = convert(pizza)
            break
    if not j:
        return flask.redirect('/404')
    return jsonify(j)