from waitress import serve
from main import app  # Replace with your actual WSGI app

if __name__ == '__main__':
    serve(app, host='localhost', port=8000)
