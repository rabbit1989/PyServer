import asyncore, socket

class handler(asyncore.dispatcher):
	def handle_read(self):
		data = self.recv(1024)
		if len(data) > 0:
			print data
			self.send('hey i am server, i have received your msg')

class server(asyncore.dispatcher):

	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((host, port))
		self.listen(5)

	def handle_accept(self):
		conn, addr = self.accept()
		hd = handler(conn)


s = server("127.0.0.1", 12345)
asyncore.loop(1000)	