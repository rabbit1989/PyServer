import asyncore, socket

class client(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, port))
	
	def handle_write(self):
		self.send('hello, i am client')

	def handle_read(self):
		data = self.recv(8192)
		if len(data) > 0:
			print data
		
c = client("127.0.0.1", 12345)
asyncore.loop(1000)	