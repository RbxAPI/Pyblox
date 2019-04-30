#
#  util -> strings.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

import re

class Strings:

	'''
	@method Strings.lowerCase(String)
	@params String, 1st
	'''
	def lowerCase(s):
		try:
			return str(s).lower()
		except TypeError:
			return None


	def upperCase(s):
		try:
			return str(s).upper()
		except TypeError:
			return None

	def titleCase(s):
		try:
			return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0)[0].upper()+mo.group(0)[1:].lower(),s)
		except TypeError:
			return None