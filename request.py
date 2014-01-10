class Request:

	def __init__(self, request):
		self.data = ""
		temp = request.recv(100)
		counter = 0
		
		while (len(temp) == 100 and counter < 82):
			self.data += temp            
			temp = request.recv(100)
			counter+=1

		self.headers = self.data.splitlines()



    