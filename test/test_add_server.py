__author__='rabbit1989'

import src.rpc.rpc_server as rpc_server
import asyncore
import threading, sys, time

class test(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.server = rpc_server.rpc_server('127.0.0.1', 12345)
	
	def run(self):
		i = 0
		while True:
			time.sleep(1)
			for addr, channel in self.server.channel_dict.iteritems():
				channel.rpc_response()

if __name__ == '__main__':
	t = test()
	t.start()
	asyncore.loop()