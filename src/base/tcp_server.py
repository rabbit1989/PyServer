__author__ = 'rabbit1989'

import tcp_connection
import asyncore, socket

class tcp_server(asyncore.dispatcher):
	def __init__(self, ip, port, con_handler):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((ip, port))
		self.listen(50)
		self.con_handler = con_handler

	def handle_accept(self):
		sock, addr = self.accept()
		conn = tcp_connection.tcp_connection(sock)
		self.con_handler.handle_new_connection(conn)

		
		