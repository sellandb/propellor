from statusCodes import statusCodes

class Response:

	def __init__(self, request):
		self.request = request
		self.headers = []
		self.body = ""
		self.response = ""
		self.status = 200
		self.HTTPVersion = "HTTP/1.1"
		self.statusCodes = statusCodes()


	def output(self):
		out = "{0} {1} {2}\r\n".format(self.HTTPVersion, self.status, self.statusCodes.Code[self.status])
		for name in self.headers.keys():
			out += name + ": " + self.headers[name] + "\r\n"

		out += self.body
		self.response = out
