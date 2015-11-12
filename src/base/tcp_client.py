__author__ = 'rabbit1989'

import tcp_connection

class tcp_client(object):
	def __init__(self, ip, port):
		self.conn = tcp_connection.tcp_connection(addr = (ip, port))

	def send(self, data):
		self.conn.send(data)

	def recv(self, size):
		return self.conn.recv(size)

	def get_data_size(self):
		return len(self.conn.read_buff)