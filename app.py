from webob import Request, Response
from parse import parse
import inspect

class DastyorApp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        handler, kwargs = self.find_handler(request)
        if handler is not None: 
            if inspect.isclass(handler):
                handler_method = getattr(handler(), request.method.lower(), None)
                if handler_method is None:
                    response.status_code = 405
                    response.text = "Method not allowed"
                    return response
                handler_method(request, response, **kwargs)
            else:
                handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response

    def find_handler(self, request):
        for path, handler in self.routes.items():
            parsed_result = parse(path, request.path)

            if parsed_result is not None:
                return handler, parsed_result.named
        return None, None

    def default_response(self, response):
        response.status_code = 404
        response.text = "Page not found."

    def route(self, path):
        if path in self.routes:
            raise AssertionError("Route is dublicated. Lets change the URL.")
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper