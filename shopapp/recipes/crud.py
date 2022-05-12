from shopapp.models import ShoppingList

def get_all_shoplists():
    shoplists = ShoppingList.query.all()
    return shoplists