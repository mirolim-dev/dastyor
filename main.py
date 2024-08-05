# from dastyor.cli import app
# from dastyor.middleware import Middleware

# @app.route("/", allowed_methods=['get'])
# def home(request, response):
#     response.text = "Hey from Home page"


# @app.route("/about")
# def about(request, response):
#     response.text = "Message from About page"

# @app.route("/welcome/{name}")
# def welcome(request, response, name):
#     response.text = f"Welcome {name}"

# @app.route('/books') 
# class Books:
#     def get(self, request, response):
#         response.text = "Books Page"

#     def post(self, request, response):
#         response.text = "Endpoint to create a book"

# def new_handler(request, response):
#     response.text = "From new handler"

# app.add_route("/new-handler", new_handler)


# @app.route("/template")
# def template_handler(request, response):
#     response.html = app.template(
#         "home.html",
#         context = {
#             'new_title': "Best title", 'new_body': "Best body"
#         }
#     )

# def on_exception(request, response, exception_class):
#     response.text = str(exception_class)

# app.add_exception_handler(on_exception)

# @app.route("/exception")
# def exception_throwing_handler(request, response):
#     raise AttributeError("Some Exception")


# class LoggingMiddleware(Middleware):
#     def process_request(self, request):
#         print("request is being called", request.url)
    
#     def process_response(self, request, response):
#         print("Response has been generated", request.url)

# app.add_middleware(LoggingMiddleware)


# @app.route("/json")
# def jsonn_response(request, response):
#     response.json = {"name": "Dastyor python web framework."}




from dastyor.app import DastyorApp
from dastyor.middleware import Middleware
app = DastyorApp()

@app.route("/", allowed_methods=['get'])
def home(request, response):
    response.text = "Hey from Home page"

@app.route("/about")
def about(request, response):
    response.text = "Message from About page"

@app.route("/welcome/{name}")
def welcome(request, response, name):
    response.text = f"Welcome {name}"

@app.route('/books') 
class Books:
    def get(self, request, response):
        response.text = "Books Page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"

def new_handler(request, response):
    response.text = "From new handler"

app.add_route("/new-handler", new_handler)

@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "home.html",
        context = {
            'new_title': "Best title", 'new_body': "Best body"
        }
    )

def on_exception(request, response, exception_class):
    response.text = str(exception_class)

app.add_exception_handler(on_exception)

@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AttributeError("Some Exception")

class LoggingMiddleware(Middleware):
    def process_request(self, request):
        print("request is being called", request.url)
    
    def process_response(self, request, response):
        print("Response has been generated", request.url)

app.add_middleware(LoggingMiddleware)

@app.route("/json")
def jsonn_response(request, response):
    response.json = {"name": "Dastyor python web framework."}


if __name__ == '__main__':
    app.runserver()
