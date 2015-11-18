__author__='rabbit1989'

from src.rpc.rpc_manager import rpc_channel_manager
from src.base.tcp_server import tcp_server
import asyncore

if __name__ == '__main__':
	r_manager = rpc_channel_manager()
	server = tcp_server('127.0.0.1', 12345, r_manager)
	asyncore.loop()