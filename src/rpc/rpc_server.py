__author__ = 'rabbit1989'

import rpc_channel
import src.base.tcp_server as tcp_server

class rpc_server(tcp_server.tcp_server):
	def __init__(self, ip, port):
		tcp_server.tcp_server.__init__(self, ip, port)
		self.channel_dict = {}

	def handle_accept(self):
		sock, addr = self.accept()
		self.channel_dict[addr] = rpc_channel.rpc_channel(sock = sock)