class Request:

	def __init__(self, request):
		self.data = ""
		temp = request.recv(100)
		counter = 0

		#Identify the Method of the request
		self.method = temp.split()[0]
		if(self.method.lower() != "get"):
			raise UnknownMethodError(self.method)
		
		#pull the data off of the buffer, maximum 8K for a request
		while (len(temp) == 100 and counter < 82):
			self.data += temp            
			temp = request.recv(100)
			counter+=1

		#Parse out the headers
		#TODO: Pull out the first line and part path and HTTP version
		#Parse headers into a dictionary
		self.headers = self.data.splitlines()


class UnknownMethodError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
    