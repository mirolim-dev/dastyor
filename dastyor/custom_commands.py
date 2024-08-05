import os

def get_sample():
    content = {
"""
from dastyor.app import DastyorApp

app = DastyorApp()

# example for custom handler
@app.route("/", allowed_methods=['get'])
def home(request, response):
    response.text = "Hey from Home page"

# type your code here







if __name__ == '__main__':
    app.runserver()

"""        
    }
    filepath = "main.py"
    if os.path.exists(filepath):
        print(f"File '{filepath}' already exists.")
    else:
        with open('file_path', 'w') as manage_py_file:
            manage_py_file.write(content)
            print(f"Default main.py created in {os.getcwd()}")