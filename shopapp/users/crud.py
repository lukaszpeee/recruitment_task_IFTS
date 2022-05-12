from shopapp.models import ShoppingList, Product
from shopapp import db


def find_shoplist_by_name(name):
    shoplist = ShoppingList.query.filter_by(name=name).first()
    return shoplist

def find_product_by_name(name):
    product = Product.query.filter_by(name=name).first()
    return product

def add_shoplist(name):
    shoplist = ShoppingList(name)
    db.session.add(shoplist)
    db.session.commit()

def remove_shoplist(shoplist):
    db.session.delete(shoplist)
    db.session.commit()

def append_product_to_list(shoplist, product):
    shoplist.products.append(product)
    db.session.commit()

def remove_product_from_list(shoplist, product):
    shoplist.products.remove(product)  
    db.session.commit()
