# serve.py 1-versiyasi
import sys
import platform
from waitress import serve as waitress_serve

from main import app
def runserver():
    if platform.system() == 'Windows':
        print("Running with Waitress on Windows")
        waitress_serve(app, host='localhost', port=8000)
    else:
        try:
            from gunicorn.app.wsgiapp import WSGIApplication
            print("Running with Gunicorn on Unix-based system")
            sys.argv = ["gunicorn", "your_framework.dastyor_app:app"]
            WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
        except ImportError:
            print("Gunicorn is not installed. Please install it on Unix-based systems.")
            sys.exit(1)

if __name__ == '__main__':
    runserver()
