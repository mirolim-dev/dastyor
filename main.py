from wsgiref.simple_server import make_server

def sample_app(envviron, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    
    return [b"Hello world from Dastyor"]


server = make_server("localhost", 1012, sample_app)
server.serve_forever()