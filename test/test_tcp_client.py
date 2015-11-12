__author__ = 'rabbit1989'

import asyncore
import src.base.tcp_client as tcp_client
import threading, time, sys

class test(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.client = tcp_client.tcp_client("127.0.0.1", 12345)
		
	def run(self):
		i = 0
		while True:
			time.sleep(1)
			self.client.send('hellow i am client' + str(i))
			i += 1
			

if __name__ == '__main__':
	t = test()
	t.start()
	asyncore.loop()
	