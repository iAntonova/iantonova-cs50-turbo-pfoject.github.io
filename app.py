from flask import Flask, render_template, flash

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# FILTERS
# safe
# capitalize
# lower
# upper
# title
# trim 
# striptags

def index():
    firt_name = "Victory"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", firt_name=firt_name, stuff=stuff, favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500