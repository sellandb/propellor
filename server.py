import SocketServer

class Request:
    data = ""
    headers = []
    body = ""

class Response:
    status = ""
    headers = {}
    body = ""

    def output(self):
        out = self.status + "\r\n"
        for name in self.headers.keys():
            out += name + ": " + self.headers[name] + "\r\n"

        out += self.body
        return out


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        
        print "Connection recieved from {}".format(self.client_address[0])
        # just send back the same data, but upper-cased

        request = Request()
        response = Response()

        request.data = self.request.recv(8192).strip()
        request.headers = request.data.splitlines()
        print request.headers



        response.body = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>Page Body</h1>
        </body>
        </html>
        """
        response.status = "HTTP/1.1 200 OK"
        response.headers["Content-Type"] = "text/html"
        response.headers["Content-Length"] = str(len(response.body) - 1)

        
        
        self.request.sendall(response.output())