from flask import Flask, render_template, request, redirect

import datab


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas_database = datab.get_pizzas()
    pizzas = []

    for pizza in pizzas_database:
        pizzas.append(
            {"name": pizza[1], "ingredients": pizza[2], "price": pizza[3]},
        )
    return render_template("menu.html", pizzas=pizzas)


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