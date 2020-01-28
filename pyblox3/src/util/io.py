#
#  util -> jsoni.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

import json
import os
import inspect

class io:

	def read(**kwargs):
		file = kwargs.get("file",None)
		with open(str(file),"r",encoding="utf-8") as jfile:
			data = json.load(jfile)
			return data

	def write(**kwargs):
		file = kwargs.get("file",None)
		key = kwargs.get("key",None)
		value = kwargs.get("value",None)
		with open(str(file),"r",encoding="utf-8") as jfile:
			data = json.load(jfile)
			jfile.close()
			data[str(key)].append(value)
			with open(str(file),"w",encoding="utf-8") as jfile:
				json.dumps(data,jfile)
				jfile.close()

	def getPath():
		file_string = os.path.abspath(inspect.stack()[-1][1])
		print(file_string)
		print(file_string[:27])


