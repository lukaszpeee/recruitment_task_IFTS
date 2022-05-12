from flask import render_template, flash, url_for, redirect, request

from .forms import ShoppingListForm
from shopapp.models import Product
from . import users_blueprint
from .crud import (find_shoplist_by_name, 
                    find_product_by_name, 
                    add_shoplist, 
                    remove_shoplist, 
                    append_product_to_list, 
                    remove_product_from_list)


@users_blueprint.route("/shoplist/new", methods=['GET', 'POST'])
def create_shoplist():
    form = ShoppingListForm()
    if request.method == 'POST' and form.validate_on_submit():
        if find_shoplist_by_name(form.shopping_list_name.data): 
            flash('Shopping list already exists!', 'error')
            return redirect(url_for('recipes.home'))
        else:
            add_shoplist(form.shopping_list_name.data)
            flash('Shopping list created!', 'success')
            return redirect(url_for('recipes.home'))
    return render_template('users/create_shoplist.html', form=form)


@users_blueprint.route("/shoplist/<string:name>/product/add", methods=['POST'])
def add_product_to_list(name):
    shoplist = find_shoplist_by_name(name)
    new_product_name = request.form.get('new_product')
    if len(new_product_name) < 1:
            flash('New product name is too short!', 'error')
            return redirect(url_for('recipes.home'))
    else:
        if find_product_by_name(new_product_name):
            product = find_product_by_name(new_product_name)
            if product in shoplist.products:
                flash('Product already on the list!', 'error')
                return redirect(url_for('recipes.home'))
            else:
                append_product_to_list(shoplist, product)
                flash('Product added!', 'success')
                return redirect(url_for('recipes.home'))
        else:
            new_product = Product(new_product_name)
            append_product_to_list(shoplist, new_product)
            flash('Product added!', 'success')
            return redirect(url_for('recipes.home'))


@users_blueprint.route("/shoplist/<string:name>/product/<string:product_name>/delete")
def delete_product_from_list(name, product_name):
    shoplist = find_shoplist_by_name(name)
    product = find_product_by_name(product_name)
    remove_product_from_list(shoplist, product)
    flash('Product deleted from the list!', 'success')
    return redirect(url_for('recipes.home'))


@users_blueprint.route("/shoplist/<string:name>/delete")
def delete_shoplist(name):
    shoplist = find_shoplist_by_name(name)
    remove_shoplist(shoplist)
    flash('Shopping list deleted!', 'success')
    return redirect(url_for('recipes.home'))