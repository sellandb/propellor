class StatusCodes:
	def __init__(self):
		self.Code = {}
		self.Code[200] = "OK"
		self.Code[301] = "Moved Permanently"
		self.Code[302] = "Found"
		self.Code[307] = "Temporary Redirect"
		self.Code[400] = "Bad Request"
		self.Code[401] = "Unauthorized"
		self.Code[403] = "Forbidden"
		self.Code[404] = "Not Found"
		self.Code[500] = "Internal Server Error"
		self.Code[503] = "Service Unavailable"
