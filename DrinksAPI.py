import flask
from flask import Blueprint, jsonify
from fetch_api import fetch_api

drinks_api = Blueprint('drinks_api', __name__)
data = fetch_api()

def convert(item):
    return {"Id" : item["dishId"], "Name" : item["dishName"], "Description" : item["dishDescription"], "price" : int(item["dishPrice"])}

@drinks_api.route('/drinks', methods=['GET'])
def drinks():
    result = list(map(convert, data["Data"]["categoriesList"][5]["dishList"]))
    return jsonify({"drinks" : result})

@drinks_api.route('/drinks/<id>', methods=['GET'])
def drink(id):
    d = data["Data"]["categoriesList"][5]["dishList"]
    j = None
    for drink in d:
        if drink["dishId"] == int(id):
            j = convert(drink)
            break
    if not j:
        return flask.redirect('/404')
    return jsonify(j)
