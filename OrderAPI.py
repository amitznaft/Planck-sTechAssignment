import flask
from flask import Blueprint, request
from fetch_api import fetch_api

order_api = Blueprint('order_api', __name__)
data = fetch_api()


@order_api.route('/order' , methods=['POST'])
def order():
    totalPrice = 0
    order = request.get_json()
    for key in order:
        if key == "pizzas":
            index = 3
        elif key == "desserts":
            index = 4
        elif key == "drinks":
            index = 5
        else: 
            return 'BAD REQUEST' , 400
        for id in order[key]:
            flag = False
            for item in data["Data"]["categoriesList"][index]["dishList"]:
                if item["dishId"] == int(id):
                    flag = True
                    totalPrice += int(item["dishPrice"])
            if not flag:
                return 'BAD REQUEST - ITEM WITH ID '+  str(id) + ' DOES NOT EXIST', 400
    return {"price": totalPrice}