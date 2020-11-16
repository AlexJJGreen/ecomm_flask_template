from flask import current_app as app
from flask import render_template, redirect, url_for
from application.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route("/login")
def login(methods=["GET", "POST"]):
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/products")
def products():
    return render_template("products.html")