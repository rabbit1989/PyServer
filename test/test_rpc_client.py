__author__ = 'rabbit1989'

import asyncore
from src.rpc.rpc_channel import rpc_channel
from src.rpc.rpc_manager import rpc_channel_manager
from src.base.tcp_client import tcp_client			
import time

if __name__ == '__main__':
	r_manager = rpc_channel_manager()
	client = tcp_client(r_manager)
	client.connect(('127.0.0.1', 12345))
	i = 0
	while True:
		asyncore.loop(0.1, True, None, 1)
		channel = r_manager.get_rpc_channel()
		i += 1
		channel.call_method('add', i, i*2)
		channel.call_method('concat_str', 'hello', '_world')	
		channel.call_method('concat_list', [i, i+1, i+2], [i+2, i+3, i+4])
		time.sleep(1)