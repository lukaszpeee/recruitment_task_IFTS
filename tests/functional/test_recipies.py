from shopapp import create_app


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"shopping lists:" in response.data
        assert b"no shopping lists" in response.data
        assert b"new list" in response.data
        assert b"products:" not in response.data
        assert b"no products" not in response.data
        assert b"delete list" not in response.data
        assert b"add product" not in response.data
        

def test_home_page_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405

