import pytest

from dastyor.middleware import Middleware

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

def test_class_based_get(app, test_client):
    @app.route("/cars")
    class Cars:
        def get(self, req, resp):
            resp.text = "Cars Page"
    assert test_client.get("http://testserver/cars").text == "Cars Page"

def test_class_based_post(app, test_client):
    @app.route("/planes")
    class Planes:
        def post(self, req, resp):
            resp.text = "Our sky is under the controll by the planes"
    assert test_client.post("http://testserver/planes").text == "Our sky is under the controll by the planes"
    assert test_client.get("http://testserver/planes").text == "Method not allowed"
    assert test_client.get("http://testserver/planes").status_code == 405

def test_alternative_route_adding(app, test_client):
    def new_handler(request, response):
        response.text = "From new handler"

    app.add_route("/new-handler", new_handler)
    assert test_client.get("http://testserver/new-handler").text == "From new handler"

def test_dublicate_route(app, test_client):
    def new_handler(request, response):
        response.text = "From new handle"
    app.add_route("/new-handler", new_handler)
    with pytest.raises(AssertionError):
        def new_handler2(request, response):
            response.text = "From new handle2"
        app.add_route("/new-handler", new_handler)

def test_template_handler(app, test_client):
    @app.route("/test-template")
    def template_handler(request, response):
        response.body = app.template(
            "test.html",
            context = {
                'new_title': "Best title", 'new_body': "Best body"
            }
        )
    response = test_client.get("http://testserver/test-template")

    assert "Best titl" in response.text
    assert "Best body" in response.text
    assert "text/html" in response.headers["Content-Type"]

def test_custom_exception_handler(app, test_client):
    def on_exception(request, response, exception_class):
        response.text = str(exception_class)

    app.add_exception_handler(on_exception)

    @app.route("/exception")
    def exception_throwing_handler(request, response):
        raise AttributeError("Some Exception")
    
    response = test_client.get("http://testserver/exception")

    assert response.text == "Some Exception"
    

def test_non_existent_static_file(test_client):
    assert test_client.get("http://testserver/static/nonexist.css").status_code == 404

def test_serving_static_file(test_client):
    response = test_client.get("http://testserver/static/test.css")

    assert response.text == "body { background-color: chocolate; }"

def test_middleware_methods_are_called(app, test_client):
    process_request_called = False
    process_response_called = False

    class CustomMiddleware(Middleware):
        def __init__(self, app):
            return super().__init__(app)
        
        def process_request(self, request):
            nonlocal process_request_called
            process_request_called = True

        def process_response(self, request, response):
            nonlocal process_response_called
            process_response_called = True
    app.add_middleware(CustomMiddleware)

    @app.route("/home")
    def index(request, response):
        response.text = "from handler"
    
    test_client.get("http://testserver/home")

    assert process_response_called is True
    assert process_request_called is True

def test_allowed_methods_for_function_based_handlers(app, test_client):
    @app.route("/", allowed_methods=['post'])
    def home(req, resp):
        resp.text = "Hello from handler"

    resp = test_client.get("http://testserver/")
    assert resp.status_code == 405
    assert resp.text == "Method not allowed"


def test_json_response_helper(app, test_client):
    @app.route("/json")
    def jsonn_response(request, response):
        response.json = {"name": "Dastyor python web framework."}
    response = test_client.get("http://testserver/json")
    response_data = response.json()

    assert response.headers['Content-Type'] == "application/json"
    assert response_data['name'] == "Dastyor python web framework."


def test_text_response_helper(app, test_client):
    @app.route("/text")
    def text_response(request, response):
        response.text = "plain text"

    response = test_client.get("http://testserver/text")
    assert "text/plain" in response.headers['Content-Type']
    assert response.text == "plain text"


def test_html_response_helper(app, test_client):
    @app.route("/html")
    def html_response(request, response):
        response.html = app.template(
            "test.html",
            context = {
                'new_title': "Best title", 'new_body': "Best body"
            }
        )
    response = test_client.get("http://testserver/html")
    assert "text/html" in response.headers['Content-Type']
    assert "Best title" in response.text
    assert "Best body" in response.text