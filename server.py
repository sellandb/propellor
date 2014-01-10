import SocketServer
from request import Request
from response import Response
from statusCodes import StatusCodes

class Propellor(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        
        print "Connection recieved from {}".format(self.client_address[0])
        # just send back the same data, but upper-cased

        request = Request(self.request)
        response = Response(self.request)

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

        response.headers["Content-Type"] = "text/html"

        response.send()