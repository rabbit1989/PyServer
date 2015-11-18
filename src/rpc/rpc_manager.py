__author__ = 'rabbit1989'

import rpc_channel

class rpc_channel_manager(object):
	def __init__(self):
		self.channel_list = []

	def handle_new_connection(self, conn):
		channel = rpc_channel.rpc_channel(conn)
		conn.set_channel_obj(channel)
		self.channel_list.append(channel)

	def get_rpc_channel(self):
		return self.channel_list[0]	

