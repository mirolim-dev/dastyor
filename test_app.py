import pytest
from app import DastyorApp

@pytest.fixture 
def app():
    return DastyorApp()

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