__author__ = 'rabbit1989'

import base.tcp_client as tcp_client
import simple_coder

class rpc_channel(object):
	def __init__(self, ip, port, coder = simple_coder):
		self.tcp_client = tcp_client.tcp_client(ip, port)	
		self.coder = coder()
		self.read_buff = ''

	def rpc_call(self, *args):
		data = self.coder.encode(args)
		self.tcp_client.send(data)

	def rpc_response(self):
		data_size = self.tcp_client.get_data_size()
		if data_size > 0:
			self.read_buff += self.tcp_client.recv(data_size)
			while True:
				index = self.read_buff.find('#')
				if index == -1:
					break

				data = self.read_buff[:index]
				self.read_buff = self.read_buff[index+1:]
				


