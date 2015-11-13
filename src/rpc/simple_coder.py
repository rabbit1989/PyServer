__author__ = 'rabbit1989'

class simple_coder(object):
	def encode(self, data):
		output = ''
		for ele in data:
			output += ' ' + str(ele)
		return output + '#'

	def decode(self, data):
		if data is None or len(data) < 1:
			return '', ()

		func_name = ''
		data = data.strip(' ')
		data_list = data.split(' ')
		func_name = data_list[0]
		args = tuple(map(lambda v: int(v), data_list[1:]))
		return func_name, args