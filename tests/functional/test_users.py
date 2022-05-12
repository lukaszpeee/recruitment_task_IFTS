def test_create_shoplist_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shoplist/new' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/shoplist/new')
    assert response.status_code == 200
    assert b'create shopping list' in response.data
    assert b'Shopping list name' in response.data
    assert b'create' in response.data
  
   
def test_create_shoplist(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shoplist/new' page is requested (POST)
    THEN check the response is valid
    """
    response = test_client.post('/shoplist/new', data={"name": "Shoplist number 10"},
                               follow_redirects=True)
    assert response.status_code == 200
    assert b'create shopping list' in response.data
    assert b'Shopping list name' in response.data


def test_add_valid_product_to_list(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shoplist/<string:name>/product/add' page is requested (POST)
    THEN check the response is valid
    """
    response = test_client.post('/shoplist/Shoplist number 10/product/add', data={"new_product": "Fish"},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'shopping lists:' in response.data
    
    
def test_delete_product_from_list(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shoplist/<string:name>/product/<string:product_name>/delete' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/shoplist/Shoplist number 10/product/Cheese/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'shopping lists:' in response.data


def test_delete_shoplist(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/shoplist/<string:name>/delete' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/shoplist/Shoplist number 10/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'shopping lists:' in response.data