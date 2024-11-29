from flask import Flask, render_template, request, redirect

import datab
from weather import get_weather

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
# def menu():
#     weather = get_weather()
#     pizza_recomend = ""
#     if weather.get("temp") < 0:
#         pizza_recomend = "Зимня"
#     elif weather.get("temp") > 30:
#         pizza_recomend = "Гавайська"
#     elif 0 <= weather.get("temp") < 20:
#         pizza_recomend = "Маргарита"
#     else:
#         pizza_recomend = "Пепероні"

#     return render_template("menu.html", weather=weather, pizza_recomend=pizza_recomend)


def menu():
    weather = get_weather()
    pizzas_database = datab.get_pizzas()
    pizzas = []

    for pizza in pizzas_database:
        pizzas.append(
            {"name": pizza[1], "ingredients": pizza[2], "price": pizza[3]},
        )

    
    pizza_recomend = ""
    if weather.get("temp") < 0:
        pizza_recomend = "Зимня"
    elif weather.get("temp") > 30:
        pizza_recomend = "Гавайська"
    elif 0 <= weather.get("temp") < 20:
        pizza_recomend = "Маргарита"
    else:
        pizza_recomend = "Пепероні"


    return render_template("menu.html", pizzas=pizzas,  weather=weather, pizza_recomend=pizza_recomend)


@app.route("/add_pizza/", methods=["GET", "POST"])
def add_pizza():
    if request.method == "POST":
        name = request.form.get("name")
        ingredients = request.form.get("ingredients")
        price = request.form.get("price")

        if not name or not ingredients or not price:
            return "Будь ласка, заповніть всі поля форми", 400

        datab.add_pizzas(name, ingredients, price)
        return redirect("/menu/")

    return render_template("add_pizza.html")


if __name__ == "__main__":
    app.run(debug=True, port=80)