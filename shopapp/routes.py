from flask import render_template, flash, url_for, redirect, request

from shopapp import app, db
from shopapp.forms import ShoppingListForm
from shopapp.models import ShoppingList, Product


@app.route("/")
def home():
    shoplists = ShoppingList.query.all()
    return render_template('home.html', shoplists=shoplists)


@app.route("/shoplist/new", methods=['GET', 'POST'])
def create_shoplist():
    form = ShoppingListForm()
    if form.validate_on_submit():
        shoplist = ShoppingList(name=form.shopping_list_name.data)
        if ShoppingList.query.filter_by(name=shoplist.name).first():
            flash('Shopping list already exists!', 'error')
            return redirect(url_for('home'))
        else:
            db.session.add(shoplist)
            db.session.commit()
            flash('Shopping list created!', 'success')
            return redirect(url_for('home'))
    return render_template('create_shoplist.html', form=form)


@app.route("/shoplist/<string:name>/product/add", methods=['POST'])
def add_product_to_list(name):
    shoplist = ShoppingList.query.filter_by(name=name).first()
    new_product_name = request.form.get('new_product')
    if len(new_product_name) < 1:
            flash('New product name is too short!', 'error')
            return redirect(url_for('home'))
    else:
        if Product.query.filter_by(name=new_product_name).first():
            product = Product.query.filter_by(name=new_product_name).first()
            if product in shoplist.products:
                flash('Product already on the list!', 'error')
                return redirect(url_for('home'))
            else:
                shoplist.products.append(product)
                db.session.commit()
                flash('Product added!', 'success')
                return redirect(url_for('home'))
        else:
            new_product = Product(name=new_product_name)
            shoplist.products.append(new_product)
            db.session.commit()
            flash('Product added!', 'success')
            return redirect(url_for('home'))
    

@app.route("/shoplist/<string:name>/product/<string:product_name>/delete")
def delete_product_from_list(name, product_name):
    shoplist = ShoppingList.query.filter_by(name=name).first()
    product = Product.query.filter_by(name=product_name).first()
    shoplist.products.remove(product)  
    db.session.commit()
    flash('Product deleted from the list!', 'success')
    return redirect(url_for('home'))


@app.route("/shoplist/<string:name>/delete")
def delete_shoplist(name):
    shoplist = ShoppingList.query.filter_by(name=name).first()
    db.session.delete(shoplist)
    db.session.commit()
    flash('Shopping list deleted!', 'success')
    return redirect(url_for('home'))






