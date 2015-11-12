__author__='rabbit1989'

import src.base.tcp_server as tcp_server
import asyncore
import threading, sys, time

class test(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.server = tcp_server.tcp_server('127.0.0.1', 12345)
	
	def run(self):
		while True:
			time.sleep(1)
			for addr, conn in self.server.conn_list.iteritems():
				conn.recv(4096)

if __name__ == '__main__':
	t = test()
	t.start()
	asyncore.loop()