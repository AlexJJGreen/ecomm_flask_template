from flask import current_app as app
from flask import render_template, redirect, url_for
from application.forms import LoginForm, AddProductForm, RegistrationForm
from flask_login import current_user, login_user, login_required, login_manager
from application.models import User
from . import db

## Shop Routes ##

@app.route("/")
@app.route("/index")
def index():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/products")
def products():
    title = "Products"
    return render_template("products.html", title=title)

## admin routes ##

@app.route("/login")
def login(methods=["GET", "POST"]):
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("add_product"))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
    return render_template("login.html", form=form)

@app.route("/add_product")
@login_required
def add_product(methods=["GET", "POST"]):
    form = AddProductForm()
    title = "Add Product"
    if form.validate_on_submit():
        product = form(id = form.name, tags = form.tags, description = form.description, colour = form.colour, primary_image = form.primary_image, secondary_image = form.secondary_image,tertiary_image = form.tertiary_image.label, ean = form.ean, price = form.price, currency = form.currency, inventory = form.inventory, units_sold = form.units_sold)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for(""))
    return render_template("add_product.html", form=form, title=title)



@app.route('/new_user', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=user.set_password(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('new_user.html', title='Register', form=form)