from shopapp import db


shoppinglists_products = db.Table("shoppinglists_products",
                                db.Column("shoppinglist_id", db.Integer, db.ForeignKey("shoppinglist.id")),
                                db.Column("product_id", db.Integer, db.ForeignKey("product.id"))
                                )


class ShoppingList(db.Model):
    __tablename__ = 'shoppinglist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    products = db.relationship('Product', secondary=shoppinglists_products, backref='products')
 

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)