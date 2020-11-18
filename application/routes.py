from flask import current_app as app
from flask import render_template, redirect, url_for
from application.forms import LoginForm, AddProductForm

@app.route("/")
@app.route("/index")
def index():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/products")
def products():
    return render_template("products.html")

## Admin Routes ##

@app.route("/login")
def login(methods=["GET", "POST"]):
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/add_product")
def add_product(methods=["GET", "POST"]):
    form = AddProductForm()
    title = "Add Product"
    return render_template("add_product.html", form=form, title=title)