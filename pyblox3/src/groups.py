#
#  groups.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

root = "https://groups.roblox.com"

class Groups_v1:

	def __init__(self,**kwargs):
		groupid = kwargs.get("groupid",None)
		self.groupid = groupid
		self.Membership = self.Membership(self)
		self.Revenue = self.Revenue(self)
		self.Permissions = self.Permissions(self)
		self.socialLinks = self.socialLinks(self)
		self.Wall = self.Wall(self)
		self.Roles = self.Roles(self)
		self.PrimaryGroup = self.PrimaryGroup(self)
		self.RoleSets = self.RoleSets(self)
	
	# GET : "https://groups.roblox.com/v1/groups/{grouid}
	async def get(self,**kwargs):
		groupid = self.groupid

	class Membership:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			
	class Revenue:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1

	class Relationships:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1


	class Permissions:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1


	class socialLinks:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1


	class Wall:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1


	class Roles:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
	
	class PrimaryGroup:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
	
	class RoleSets:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1

