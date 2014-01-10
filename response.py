from statusCodes import StatusCodes

class Response:

	def __init__(self, request):
		self.request = request
		self.headers = {}
		self.body = ""
		self.status = 200
		self.HTTPVersion = "HTTP/1.1"
		self.statusCodes = StatusCodes()


	def output(self):
		#Need to determine when we shouldn't add this header
		if True:
			self.headers["Content-Length"] = str(len(self.body) - 1)

		out = "{0} {1} {2}\r\n".format(self.HTTPVersion, self.status, self.statusCodes.Code[self.status])
		for name in self.headers.keys():
			out += name + ": " + self.headers[name] + "\r\n"

		out += self.body
		return out

	def send(self):
		self.request.sendall(self.output())
