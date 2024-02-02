#
#  auth.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *

Req = Req()

root = "https://auth.roblox.com"

class Auth_v2:

	def __init__(self,**kwargs):
		auth_cookies = kwargs.get("cookies")
		self.auth_cookies = auth_cookies