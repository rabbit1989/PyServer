__author__ = 'rabbit1989'

import asyncore, socket

class tcp_connection(asyncore.dispatcher):
	buff_size = 4096
	def __init__(self, sock = None):
		'''
			tcp_connection is a simple wrapper of asyncore.dispatcher_with_send, it holds a channel object passed
			from upper level. Whenever it receives data, the data is processed by channel object
		'''
		if sock is None:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		asyncore.dispatcher.__init__(self, sock)
		self.write_buff = ''

	def set_channel_obj(self, channel_obj):
		self.channel_obj = channel_obj

	def get_channel_obj(self):	
		return self.channel_obj	

	def handle_read(self):	
		data = asyncore.dispatcher.recv(self, self.buff_size) 
		self.channel_obj.process_data(data)

	def handle_write(self):
		sent_data = self.write_buff[:self.buff_size]
		self.write_buff = self.write_buff[len(sent_data):]
		asyncore.dispatcher.send(self, sent_data)

	def send(self, data):
		self.write_buff += data