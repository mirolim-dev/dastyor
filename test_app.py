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

def test_parametrized_routing(app, test_client):
    @app.route("/welcome/{name}")
    def welcome(request, response, name):
        response.text = f"Welcome {name}"
    
    assert test_client.get("http://testserver/welcome/Mirolim").text == "Welcome Mirolim"
    assert test_client.get("http://testserver/welcome/Hadji").text == "Welcome Hadji"

def test_default_response(test_client):
    response = test_client.get("http://testserver/notexistent")
    assert response.text == "Page not found."
    assert response.status_code == 404
