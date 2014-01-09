import SocketServer
from server import MyTCPHandler

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    print "listening on {0}:{1}".format(HOST,PORT)
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()