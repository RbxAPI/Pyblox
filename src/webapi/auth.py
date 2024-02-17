#
#  auth.py
#  pyblox
#
#  By sbhadr (Sanjay Bhadra)
#  Copyright © 2024- sbhadr (Sanjay Bhadra). All rights reserved.
#

root = "https://auth.roblox.com"

class Auth_v2:

	def __init__(self,**kwargs):
		auth_cookies = kwargs.get("cookies")
		self.auth_cookies = auth_cookies