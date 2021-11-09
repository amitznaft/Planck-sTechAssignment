import flask
from DrinksAPI import drinks_api
from PizzasAPI import pizzas_api
from DessertsAPI import desesets_api
from OrderAPI import order_api

app = flask.Flask(__name__)
app.register_blueprint(drinks_api)
app.register_blueprint(pizzas_api)
app.register_blueprint(desesets_api)
app.register_blueprint(order_api)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    return "REQUEST NOT FOUND", 404

if __name__ == "__main__":
    app.run()