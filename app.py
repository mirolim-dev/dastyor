from webob import Request, Response


class DastyorApp:
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "User Agent Not Found")
        response = Response()
        response.text = f"Assalomu alaykum my friend with user agent {user_agent}"
        return response