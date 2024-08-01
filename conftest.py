import pytest
from dastyor.wsgi import DastyorApp

@pytest.fixture 
def app():
    return DastyorApp()

@pytest.fixture
def test_client(app):
    return app.test_session()

