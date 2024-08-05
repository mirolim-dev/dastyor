# Dastyor

![purpose](https://img.shields.io/badge/purpose-learning-green)![PyPI - Version](https://img.shields.io/pypi/v/dastyor)

Introduction

**Dastyor** is a lightweight Python web framework designed for learning purposes. It provides a minimalistic approach to web development, allowing you to build web applications quickly and with minimal boilerplate code.

### Features

- Simple and intuitive API
- Built-in support for routing and templating
- Integration with popular libraries

## Installation

To install Dastyor, use pip:

```bash
pip install dastyor
```

## CLI Commands[optional]

### `dastyor get_samlple.`

The `get_sample` command generates a default `main.py` file with example code for custom handlers if the file does not already exist. This command is useful for quickly setting up a basic structure for a Dastyor application.

#### **Usage:**

To use the `get_sample` command, run the following command in your terminal:

```terminal
dastyor get_sample
```

#### Behavior

* **File Check:** The command checks if `main.py` already exists in the current directory.
* **File Creation:** If `main.py` does not exist, the command creates the file with predefined content.
* **Content:** The generated `main.py` file includes:
  * Import statements for `DastyorApp`.
  * An example route handler for the home page.
  * A placeholder for adding custom code.
  * A section to run the server if the script is executed as the main module.

#### **Example.**

When you run `dastyor get_sample`, it will generate a `main.py` file with the following content:

```python
from dastyor.app import DastyorApp

app = DastyorApp()

# Example for custom handler
@app.route("/", allowed_methods=['get'])
def home(request, response):
    response.text = "Hey from Home page"

# Type your code here







if __name__ == '__main__':
    app.runserver()

```

If `main.py` already exists in the current directory, the command will output:

```terminal
File 'main.py' already exists.
```

If `main.py` does not exist, the command will create the file and output:

```terminal
Default main.py created in <current_directory>
```

## **Getting Start**

- **CLI command:** Use this command to get sample custom handler[optional]. `dastyor get_sample`
- **Basic Usage**: Show a simple example of setting up a basic application using your framework.
- **Configuration**: Explain any configuration options available.

---

#### It's important.

> The following code should be placed at the bottom of your main handler file:
>
> ```PYTHON
> if __name__ == '__main__':
>     app.runserver()
> ```
>
> use following command to run the server.
>
> ```
> python file_name.py
> ```
>
>  for instance I got handler file called `main.py` then I should type `python main.py` to run the server.

---



Here's a quick example to get you started with Dastyor:

### 1. Basic Routing.

**Define simple routes using decorators:**

```python
from dastyor.app import DastyorApp
app = DastyorApp()

@app.route("/", allowed_methods=['get'])
def home(request, response):
    response.text = "Hey from Home page"

@app.route("/about")
def about(request, response):
    response.text = "Message from About page"
```

`/` route responds with "Hey from Home page".

`/about` route responds with "Message from About page".

### 2. **Dynamic Routing.**

Handle dynamic URL parameters with route placeholders:

```python
@app.route("/welcome/{name}")
def welcome(request, response, name):
    response.text = f"Welcome {name}"
```

`/welcome/{name}` route responds with a personalized welcome message.

### 3. **Class-Based Views**

Define routes using classes for different HTTP methods:

```python
@app.route('/books')
class Books:
    def get(self, request, response):
        response.text = "Books Page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"
```

`/books` route responds with "Books Page" for GET requests and "Endpoint to create a book" for POST requests.

### 4. **Adding Routes Dynamically**

Add routes to your application dynamically:

```python
def new_handler(request, response):
    response.text = "From new handler"

app.add_route("/new-handler", new_handler)
```

`/new-handler` route responds with "From new handler".

### 5. **Rendering Templates**

Use templates to render HTML responses:

```python
@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "home.html",
        context = {
            'new_title': "Best title", 'new_body': "Best body"
        }
    )
```

`/template` route renders `home.html` with provided context.

### 6. **Exception Handling**

Handle exceptions globally:

```python
def on_exception(request, response, exception_class):
    response.text = str(exception_class)

app.add_exception_handler(on_exception)

@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AttributeError("Some Exception")
```

`/exception` route raises an exception, and `on_exception` handler will return the exception message.

### 7. **Middleware**

Create middleware to process requests and responses:

```python
from dastyor.middleware import Middleware

class LoggingMiddleware(Middleware):
    def process_request(self, request):
        print("Request is being called", request.url)
  
    def process_response(self, request, response):
        print("Response has been generated", request.url)

app.add_middleware(LoggingMiddleware)
```

`LoggingMiddleware` prints log messages for incoming requests and outgoing responses.

### 8. **JSON Responses**

Send JSON responses:

```python
@app.route("/json")
def json_response(request, response):
    response.json = {"name": "Dastyor python web framework."}
```

`/json` route returns a JSON response with framework information.

### **9. Serving Static Files.**

Dastyor supports serving static files, such as CSS, JavaScript, and images, which can be referenced in your HTML templates. This is useful for including stylesheets, scripts, and other static assets in your web application.

#### Serving Static Files.

To serve static files, you need to place them in a specific directory and configure your application to serve them. By default, static files are served from the `static` directory.

#### Example Directory Structure.

Here’s an example of how your project directory might be organized:

```
my_project/
│
├── static/
│   ├── home.css
│
├── templates/
│   ├── home.html
│
├── app.py
└── manage.py

```

* `static/`: Directory containing static files like CSS, JavaScript, and images.
* `templates/`: Directory containing HTML templates.

#### Example HTML Template.

In your HTML templates, you can reference static files using the `/static/` URL prefix. For example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ new_title }}</title>
    <link rel="stylesheet" href="/static/home.css">
</head>
<body>
    {{ new_body }}
</body>
</html>
```

In this example, `home.css` is a CSS file located in the `static/` directory. The `href` attribute in the `<link>` tag points to `/static/home.css`, which will serve the stylesheet to the browser.

#### Serving Static Files in Your Application.

Ensure that your application is configured to serve static files from the `static` directory. In Dastyor, static files are automatically served from the `static` directory by default. No additional configuration is required.

#### Customizing Static File Handling.

If you need to customize how static files are served or change the directory, you can adjust the configuration in your application setup. Check the documentation or configuration options available in your framework for more details.

## Product Level Testing.

Product level testing focuses on ensuring that your web application built with Dastyor performs as expected in real-world scenarios. Below are examples of how to write and organize tests for a web application using Dastyor.

### Example Tests.

#### * Basic Functionality.

Test basic routes and responses:

`test_app.py`  (you may call this filename whatever you want)

```python
import pytest
from dastyor.wsgi import DastyorApp

@pytest.fixture
def app():
    """Fixture to provide a DastyorApp instance for testing."""
    app = DastyorApp()
  
    # Optionally, you can configure the app here, add routes, etc.
    # For example, you can add routes or middleware specific to your tests.
  
    return app

@pytest.fixture
def test_client(app):
    """Fixture to provide a test client session for making requests."""
    return app.test_session()

def test_home_page(test_client):
    response = test_client.get('http://testserver/')
    assert response.status_code == 200
    assert response.text == "Hey from Home page"

def test_about_page(test_client):
    response = test_client.get('http://testserver/about')
    assert response.status_code == 200
    assert response.text == "Message from About page"
```

#### * Dynamic Routing.

Test dynamic routes with parameters:

```python
def test_welcome_page(test_client):
    response = test_client.get('http://testserver/welcome/Mirolim')
    assert response.status_code == 200
    assert response.text == "Welcome Mirolim"

```

#### * Static Files.

Test serving static files:

```python
def test_serving_static_files(test_client):
    response = test_client.get('http://testserver/static/home.css')
    assert response.status_code == 200
    assert "body { background-color: chocolate; }" in response.text

def test_non_existent_static_file(test_client):
    response = test_client.get('http://testserver/static/nonexistent.css')
    assert response.status_code == 404
```

#### * Template Rendering.

Test rendering of HTML templates:

```python
def test_template_rendering(test_client):
    response = test_client.get('http://testserver/template')
    assert response.status_code == 200
    assert "Best title" in response.text
    assert "Best body" in response.text
```

#### * Error Handling.

Test custom error handling:

```python
def test_custom_exception_handling(test_client):
    response = test_client.get('http://testserver/exception')
    assert response.status_code == 500
    assert "Some Exception" in response.text
```

#### * Middleware.

Test middleware functionality:

```python
def test_middleware_processing(test_client):
    response = test_client.get('http://testserver/home')
    assert response.status_code == 200
    # Check middleware side-effects or logging here
```

#### * JSON Responses.

* [ ] Test JSON response handling:

```python
def test_json_response(test_client):
    response = test_client.get('http://testserver/json')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()['name'] == 'Dastyor python web framework.'
```

#### * Running Your Tests.

To run your tests, execute the following command in your terminal:

```terminal
pytest
```
