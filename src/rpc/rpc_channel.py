__author__ = 'rabbit1989'

import json

class rpc_channel(object):
	'''
		one rpc channel corresponds to one tcp connection
	'''
	def __init__(self, conn):
		self.conn = conn
		self.read_buff = ''
			
	def call_method(self, *args):
		data = json.dumps(args)
		self.conn.send(data + '#')

	def process_data(self, data):
		func_name, args = self.parse(data)
		func = getattr(self, func_name, None)
		if func:
			func(*args)

	def parse(self, data):
		self.read_buff += data
		if len(self.read_buff) > 0:
			index = self.read_buff.find('#')
			if index != -1:	
				data = self.read_buff[:index]
				self.read_buff = self.read_buff[index+1:]	
				request = json.loads(data)
				return request[0], request[1:]

	def add(self, a, b):
		print 'calculating %d + %d ...' % (a, b)
		self.call_method('on_add', a, b, a+b)

	def on_add(self, a, b, ret):
		print 'the result of %d + %d is %d' % (a, b, ret)

	def concat_str(self, str1, str2):
		print 'concatenate string %s and %s...' % (str1, str2)
		self.call_method('on_concat_str', str1+str2)

	def on_concat_str(self, str):
		print 'the concat result is %s' % str

	def concat_list(self, list1, list2):
		print 'concatenate list %s and %s' % (str(list1), str(list2))
		self.call_method('on_concat_list', list1+list2)

	def on_concat_list(self, list):
		print 'on_concat_list: result: %s' % (str(list))				