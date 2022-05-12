import pytest
from shopapp import create_app, db
from shopapp.models import ShoppingList, Product


@pytest.fixture(scope='module')
def new_shoplist():
    shoplist = ShoppingList('Shoplist number 10')
    return shoplist


@pytest.fixture(scope='module')
def new_product():
    product = Product('Cheese')
    return product


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    shoplist1 = ShoppingList(name='Shoplist number 10')
    product1 = Product(name='Cheese')
    shoplist1.products.append(product1)
    db.session.add(shoplist1)
    db.session.add(product1)
    db.session.commit()
    yield
    db.drop_all()


