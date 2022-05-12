from shopapp.models import ShoppingList, Product


def test_new_shoppinglist():
    """
    GIVEN a ShoppingList model
    WHEN a new ShoppingList is created
    THEN check the name is defined correctly
    """
    shoplist = ShoppingList('Shoplist number 5')
    assert shoplist.name == 'Shoplist number 5'
    

def test_new_product():
    """
    GIVEN a Product model
    WHEN a new Product is created
    THEN check the name is defined correctly
    """
    product = Product('Flour')
    assert product.name == 'Flour'