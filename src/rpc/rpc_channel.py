__author__ = 'rabbit1989'

import src.base.tcp_connection as tcp_connection
import simple_coder

class rpc_channel(object):
	def __init__(self, sock = None, addr = None, coder = simple_coder.simple_coder):
		self.tcp_conn = tcp_connection.tcp_connection(sock = sock, addr = addr)
		self.coder = coder()
		self.read_buff = ''

	def rpc_call(self, *args):
		data = self.coder.encode(args)
		self.tcp_conn.send(data)

	def rpc_response(self):
		self.read_buff += self.tcp_conn.recv(1024)
		if len(self.read_buff) > 0:
			while True:
				index = self.read_buff.find('#')
				if index == -1:
					break
				
				data = self.read_buff[:index]
				self.read_buff = self.read_buff[index+1:]	
				func_name, args = self.coder.decode(data)
				func = getattr(self, func_name, None)
				if func:
					func(*args)

	def add(self, a, b):
		print 'calculating %d + %d ...' % (a, b)
		self.rpc_call('on_add', a, b, a+b)

	def on_add(self, a, b, ret):
		print 'the result of %d + %d is %d' % (a, b, ret)				

