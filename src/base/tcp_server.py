__author__ = 'rabbit1989'

import tcp_connection
import asyncore, socket

class tcp_server(asyncore.dispatcher):
	def __init__(self, ip, port, num_connection = 5):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((ip, port))
		self.listen(num_connection)
		self.conn_list = {}

	def handle_read(self):
		pass
	def handle_write(self):
		pass
	def handle_accept(self):
		conn, addr = self.accept()
		self.conn_list[addr] = tcp_connection.tcp_connection(sock=conn)

		
		