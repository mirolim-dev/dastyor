import pytest

def test_basic_route_adding(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hey from Home page"

def test_dublicate_routes(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hey from Home page"
    
    with pytest.raises(AssertionError):
        @app.route("/home")
        def home2(req, resp):
            resp.text = "Hey from Home page2"

def test_requests_can_be_sent_by_test_client(app, test_client):
    @app.route('/home')
    def home(req, resp):
        resp.text = "Hey from Home page"  

    response = test_client.get("http://testserver/home")
    assert response.text == "Hey from Home page"