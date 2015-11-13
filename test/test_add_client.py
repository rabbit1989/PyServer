__author__ = 'rabbit1989'

import asyncore
import src.rpc.rpc_channel as rpc_channel
import threading, time, sys

class test(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.client = rpc_channel.rpc_channel(addr = ("127.0.0.1", 12345))
		
	def run(self):
		i = 0
		while True:
			time.sleep(1)
			self.client.rpc_call('add', i, i)
			self.client.rpc_response()
			i += 1
			

if __name__ == '__main__':
	t = test()
	t.start()
	asyncore.loop()