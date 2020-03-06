#
#  groups.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class Groups_v1:

	def __init__(self,**kwargs):
		groupid = kwargs.get("groupid", None)
		auth = kwargs.get("auth", None)
		self.groupid = groupid
		self.auth = auth.auth_cookies
		self.Membership = self.Membership(self)
		self.Revenue = self.Revenue(self)
		self.Permissions = self.Permissions(self)
		self.socialLinks = self.socialLinks(self)
		self.Wall = self.Wall(self)
		self.Roles = self.Roles(self)
		self.primaryGroup = self.primaryGroup(self)
		self.roleSets = self.roleSets(self)
	
	# GET : "https://groups.roblox.com/v1/groups/{grouid}"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_groupId
	async def get(self):
		groupid = self.groupid
		response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}')
		return response[4]
	
	# GET : "https://groups.roblox.com/v1/groups/{groupid}/audit-log"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_groupId_audit_log
	async def auditLog(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		actionType = kwargs.get("ActionType", None) # not used
		sortOrder = kwargs.get("sortOrder", None) # not used
		limit = kwargs.get("limit", None) # not used
		cursor = kwargs.get("cursor", None) # not used
		userid = kwargs.get('userid', None) # not used
		response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/audit-log', cookies=auth)
		return response[4]
	
	# GET : "https://groups.roblox.com/v1/groups/{groupid}/settings"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_groupId_settings
	async def settings(self):
		groupid = self.groupid
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/settings', cookies=auth)
		return response[4]
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/settings"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_settings
	async def updateSettings(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		request = kwargs.get("request", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/settings', payload=request, cookies=auth)
		if response[0] == 200:
			return True
		else:
			return False, response[4]
	
	# GET : "https://groups.roblox.com/v1/groups/configuration/metadata"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_configuration_metadata
	async def configMetadata(self):
		response = await Req.request(t="GET", url='https://groups.roblox.com/v1/groups/configuration/metadata')
		return response[4]
	
	# GET : "https://groups.roblox.com/v1/groups/metadata"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_metadata
	async def metadata(self):
		response = await Req.request(t="GET", url='https://groups.roblox.com/v1/groups/metadata')
		return response[4]
	
	# POST : "https://groups.roblox.com/v1/groups/create"
	# Docs : https://groups.roblox.com/docs#!/Groups/post_v1_groups_create
	async def create(self,**kwargs):
		auth = self.auth
		request = kwargs.get("request")
		response = await Req.request(t="POST", url='https://groups.roblox.com/v1/groups/create', payload=request, cookies=auth)
		return response[4]
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/description"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_description
	async def updateDescription(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		request = kwargs.get("request", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/description', payload=request, cookies=auth)
		if response[0] == 200:
			return True
		else:
			return False, response[4]
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/status"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_status
	async def updateStatus(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		statusRequest = kwargs.get("statusRequest", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/status', payload=statusRequest, cookies=auth)
		if response[0] == 200:
			return True
		else:
			return False, response[4]
	
	# PATCH : "https://groups.roblox.com/v1/groups/icon"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_icon
	async def updateIcon(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		files = kwargs.get("files", None)
		response = await Req.request(t="PATCH", url='https://groups.roblox.com/v1/groups/icon', payload={"groupid": groupid,"files": files}, cookies=auth)
		if response[0] == 200:
			return True
		else:
			return False, response[4]

	class Membership:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/join-requests"
		# Docs : https://groups.roblox.com/docs#!/Membership/delete_v1_groups_groupId_join_requests
		async def denyJoinRequests(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/join-requests"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_join_requests
		async def getJoinRequests(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet			
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/join-requests"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_join_requests
		async def acceptJoinRequests(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/delete_v1_groups_groupId_join_requests_users_userId
		async def denyJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_join_requests_users_userId
		async def getJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_join_requests_users_userId
		async def acceptJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/membership"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_membership
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/membership', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_roles
		async def roles(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/users"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_roles_roleSetId_users
		async def rolesetIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			roleSetId = kwargs.get("roleSetId", None)	
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet	
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/users', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/users"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_users
		async def userIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/users', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/users"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_users
		async def join(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			joinGroupModel = kwargs.get("joinGroupModel", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/users', payload=joinGroupModel, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/user/groups/pending"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_user_groups_pending
		async def pendingIndex(self):
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/user/groups/pending', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/users/{userid}/group-membership-status"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_users_userId_group_membership_status
		async def status(self,**kwargs):
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/users/{userid}/group-membership-status', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/users/{userid}/group/roles"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_users_userId_groups_roles
		async def rolesIndex(self,**kwargs):
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/users/{userid}/group/roles', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/change-owner"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_change_owner
		async def newOwner(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			changeOwnserRequest = kwargs.get("changeOwnerRequest", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/change-owner', payload=changeOwnserRequest, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/claim-ownership"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_claim_ownership
		async def claimOwnership(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/claim-ownership', payload={}, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/delete_v1_groups_groupId_users_userId
		async def exile(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/users/{userid}', payload={}, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/patch_v1_groups_groupId_users_userId
		async def promote(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/users/{userid}', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]


	class Revenue:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth

		# GET : "https://groups.roblox.com/v1/groups/{groupid}/payouts"
		# Docs : https://groups.roblox.com/docs#!/Revenue/get_v1_groups_groupId_payouts
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/payouts', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/payouts"
		# Docs : https://groups.roblox.com/docs#!/Revenue/post_v1_groups_groupId_payouts
		async def pay(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/payouts', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupId}/payouts/recurring"
		# Docs : https://groups.roblox.com/docs#!/Revenue/post_v1_groups_groupId_payouts_recurring
		async def update(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/payouts/recurring', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		

	class Relationships:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# GET : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}"
		# Docs : https://groups.roblox.com/docs#!/Relationships/get_v1_groups_groupId_relationships_groupRelationshipType
		async def get(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}', cookies=auth)
			response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/delete_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchDecline(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="DELETE", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/get_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchGet(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			startRowIndex = kwargs.get("startRowIndex", None) # Not used yet
			maxRows = kwargs.get("maxRows", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', cookies=auth)
			response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/post_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchAccept(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/{relatedGroupId}"
		# Docs : https://groups.roblox.com/docs#!/Relationships/delete_v1_groups_groupId_relationships_groupRelationshipType_relatedGroupId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			relatedGroupId = kwargs.get("relatedGroupId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/{relatedGroupId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/{relatedGroupId}"
		# Docs : https://groups.roblox.com/docs#!/Relationships/post_v1_groups_groupId_relationships_groupRelationshipType_relatedGroupId
		async def create(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			relatedGroupId = kwargs.get("relatedGroupId", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/{relatedGroupId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]

		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests/{relatedGroupId}"
		# Docs : https://groups.roblox.com/docs#!/Relationships/delete_v1_groups_groupId_relationships_groupRelationshipType_requests_relatedGroupId
		async def decline(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			relatedGroupId = kwargs.get("relatedGroupId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests/{relatedGroupId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]

		# POST : "https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests/{relatedGroupId}"
		# Docs : https://groups.roblox.com/docs#!/Relationships/post_v1_groups_groupId_relationships_groupRelationshipType_requests_relatedGroupId
		async def accept(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			relatedGroupId = kwargs.get("relatedGroupId", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests/{relatedGroupId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]


	class Permissions:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth

		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/get_v1_groups_groupId_roles_roleSetId_permissions
		async def rolesetIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			roleSetId = kwargs.get("roleSetId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions', cookies=auth)
			return response[4]
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/patch_v1_groups_groupId_roles_roleSetId_permissions
		async def rolesetUpdate(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			roleSetId = kwargs.get("roleSetId", None)
			updatePermissionsRequest = kwargs.get("updatePermissionsRequest", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions', payload=updatePermissionsRequest, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/get_v1_groups_groupId_roles_guest_permissions
		async def guestIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			roleSetId = kwargs.get("roleSetId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions', cookies=auth)
			return response[4]
		
	
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/get_v1_groups_groupId_roles_permissions
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/permissions', cookies=auth)
			return response[4]


	class socialLinks:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/social-links"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/get_v1_groups_groupId_social_links
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/social-links"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/post_v1_groups_groupId_social_links
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/social-links', payload=request, cookies=auth)
			return response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/delete_v1_groups_groupId_social_links_socialLinkId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			socialLinkId = kwargs.get("", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/patch_v1_groups_groupId_social_links_socialLinkId
		async def update(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			socialLinkId = kwargs.get("socialLinkId", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]


	class Wall:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth

		# GET: "https://groups.roblox.com/v1/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/get_v1_groups_groupId_wall_posts
		async def get(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/posts', cookies=auth)
			return response[4]

		# POST : "https://groups.roblox.com/v1/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/post_v1_groups_groupId_wall_posts
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/posts', payload=request, cookies=auth)
			return response[0]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/wall/posts/{postId}"
		# Docs : https://groups.roblox.com/docs#!/Wall/delete_v1_groups_groupId_wall_posts_postId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			postId = kwargs.get("postId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/posts/{postId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/wall/users/{userId}/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/delete_v1_groups_groupId_wall_users_userId_posts
		async def deleteFromUserid(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/users/{userId}/posts', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
	

	class groupSearch:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.grouid
			self.auth = Groups_v1.auth
		
		# GET : "https://groups.roblox.com/v1/groups/search"
		# Docs : https://groups.roblox.com/docs#!/GroupSearch/get_v1_groups_search
		async def byKeyword(self,**kwargs):
			auth = self.auth
			keyword = kwargs.get("keyword", None) 
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/search?keyword={keyword}&limit=10', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/search/lookup"
		# Docs : https://groups.roblox.com/docs#!/GroupSearch/get_v1_groups_search_lookup
		async def byExactMatch(self,**kwargs):
			auth = self.auth
			groupName = kwargs.get("groupName", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/search/lookup?groupName={groupName}', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v1/groups/search/metadata"
		# Docs : https://groups.roblox.com/docs#!/GroupSearch/get_v1_groups_search_metadata
		async def metadata(self):
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/search/metadata', cookies=auth)
			return response[4]


	class Roles:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth

		# GET : "https://groups.roblox.com/v1/roles"
		# Docs : https://groups.roblox.com/docs#!/Roles/get_v1_roles
		async def get(self,**kwargs):
			auth = self.auth
			ids = kwargs.get("ids", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/roles?ids={ids}', cookies=auth)
			return response[4]
	
	class primaryGroup:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth

		# GET : "https://groups.roblox.com/v1/users/{userId}/groups/primary/role"
		# Docs : https://groups.roblox.com/docs#!/PrimaryGroup/get_v1_users_userId_groups_primary_role
		async def get(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/users/{userId}/groups/primary/role', cookies=auth)
			return response[0]
		
		# DELETE : "https://groups.roblox.com/v1/user/groups/primary"
		# Docs : https://groups.roblox.com/docs#!/PrimaryGroup/delete_v1_user_groups_primary
		async def remove(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/user/groups/primary', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# POST : "https://groups.roblox.com/v1/user/groups/primary"
		# Docs : https://groups.roblox.com/docs#!/PrimaryGroup/post_v1_user_groups_primary
		async def setTo(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/user/groups/primary', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
	
	class roleSets:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/rolesets/create"
		# Docs : https://groups.roblox.com/docs#!/RoleSets/post_v1_groups_groupId_rolesets_create
		async def create(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/rolesets/create', payload=request, cookies=auth)
			return response[4]
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}"
		# Docs : https://groups.roblox.com/docs#!/RoleSets/delete_v1_groups_groupId_rolesets_rolesetId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			rolesetId = kwargs.get("rolesetId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}', cookies=auth)
			if response[0] == 200:
				return True
			else:
				return False, response[4]
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}"
		# Docs : https://groups.roblox.com/docs#!/RoleSets/patch_v1_groups_groupId_rolesets_rolesetId
		async def update(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			rolesetId = kwargs.get("rolesetId", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}', payload=request, cookies=auth)
			return response[4]


class Groups_v2:

	def __init__(self,**kwargs):
		groupid = kwargs.get("groupid", None)
		auth = kwargs.get("auth", None)
		self.groupid = groupid
		self.auth = auth.auth_cookies
		self.Groups = self.Groups(self)
		self.Wall = self.Wall(self)
	
	class Groups:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# GET : "https://groups.roblox.com/v2/groups"
		# Docs : https://groups.roblox.com/docs#!/Groups/get_v2_groups
		async def multiGet(self,**kwargs):
			auth = self.auth
			groupIds = kwargs.get("groupIds", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v2/groups?groupIds={groupIds}', cookies=auth)
			return response[4]
		
		# GET : "https://groups.roblox.com/v2/users/{userId}/groups/roles"
		# Docs : https://groups.roblox.com/docs#!/Groups/get_v2_users_userId_groups_roles
		async def roleIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v2/users/{userId}/groups/roles', cookies=auth)
			return response[4]
	

	class Wall:

		def __init__(self,Groups_v1):
			self.Groups_v1 = Groups_v1
			self.groupid = Groups_v1.groupid
			self.auth = Groups_v1.auth
		
		# GET : "https://groups.roblox.com/v2/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/get_v2_groups_groupId_wall_posts
		async def get(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v2/groups/{groupid}/wall/posts?sortOrder=Asc&limit=10', cookies=auth)
			return response[4]
		
		# POST : "https://groups.roblox.com/v2/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/post_v2_groups_groupId_wall_posts
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v2/groups/{groupid}/wall/posts', payload=request, cookies=auth)
			return response[4]