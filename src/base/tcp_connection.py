__author__ = 'rabbit1989'

import asyncore, socket

class tcp_connection(asyncore.dispatcher):
	buff_size = 4096
	def __init__(self, sock = None, addr = None):
		'''
			the __init__ method receives two kinds of parameter:
			
			#one is 'addr' which indicates (ip, host) pair, the method uses the pair to 
			create a new socket

			#the other is a socket which is ready to use 
		'''
		asyncore.dispatcher.__init__(self, sock)
		self.read_buff = ''
		self.write_buff = ''

		if addr:
			self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
			self.connect(addr)
		else:
			self.set_socket(sock)

		print 'connection buffer size: %d' % self.buff_size

	def handle_read(self):	
		self.read_buff += asyncore.dispatcher.recv(self, self.buff_size) 

	def handle_write(self):
		sent_data = self.write_buff[:self.buff_size]
		self.write_buff = self.write_buff[len(sent_data):]
		asyncore.dispatcher.send(self, sent_data)

	def send(self, data):
		self.write_buff += data

	def recv(self, size):
		recv_data = self.read_buff[:size]
		self.read_buff = self.read_buff[size:]
		return recv_data