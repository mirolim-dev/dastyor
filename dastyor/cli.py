import sys
import os
import click
import platform

from waitress import serve as waitress_serve
from .wsgi import app

# app = DastyorApp()

@click.group()
def cli():
    """Manage the Dastyor application."""
    pass

@cli.command()
@click.option('--host', default='127.0.0.1', help='The host to bind to.')
@click.option('--port', default=8000, help='The port to bind to.')
def runserver(host, port):
    """Run the Dastyor application."""
    if platform.system() == 'Windows':
        print("Running with Waitress on Windows")
        click.echo(f"Running on {host}:{port}")
        waitress_serve(app, host=host, port=port)
    else:
        try:
            from gunicorn.app.wsgiapp import WSGIApplication
            print("Running with Gunicorn on Unix-based system")
            sys.argv = ["gunicorn", "your_framework.dastyor_app:app"]
            WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
        except ImportError:
            print("Gunicorn is not installed. Please install it on Unix-based systems.")
            sys.exit(1)

def get_defaults():
    """Create default manage.py file."""
    manage_py_content = '''
    if __name__ == '__main__':
        from dastyor.serve import runserver
        runserver()
    '''
    with open('manage.py', 'w') as manage_py_file:
        manage_py_file.write(manage_py_content)
    click.echo(f"Default manage.py created in {os.getcwd()}")

if __name__ == '__main__':
    cli()

