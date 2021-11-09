import flask
from flask import Blueprint, jsonify
from fetch_api import fetch_api

desesets_api = Blueprint('desserts_api', __name__)
data = fetch_api()

def convert(item):
    return {"Id" : item["dishId"], "Name" : item["dishName"], "Description" : item["dishDescription"], "price" : int(item["dishPrice"])}

@desesets_api.route('/desserts', methods=['GET'])
def desserts():
    result = list(map(convert, data["Data"]["categoriesList"][4]["dishList"]))
    return jsonify({"desserts" : result})

@desesets_api.route('/desserts/<id>', methods=['GET'])
def dessert(id):
    d = data["Data"]["categoriesList"][4]["dishList"]
    j = None
    for dessert in d:
        if dessert["dishId"] == int(id):
            j = convert(dessert)
            break
    if not j:
        return flask.redirect('/404')
    return jsonify(j)