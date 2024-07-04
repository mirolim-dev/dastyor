from app import DastyorApp

app = DastyorApp()

@app.route("/")
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
