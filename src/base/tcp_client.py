__author__ = 'rabbit1989'

import tcp_connection

class tcp_client(tcp_connection.tcp_connection):
	
	def __init__(self, con_handler):
		tcp_connection.tcp_connection.__init__(self)
		self.con_handler = con_handler

	def handle_connect(self):
		self.con_handler.handle_new_connection(self)