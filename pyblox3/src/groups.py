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
		if response[0] == 200:
			return json.loads(response[1].decode('utf-8'))
		elif response[0] == 400:
			print("Group is invalid or does not exist")
		return None
	
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
		if response[0] == 200:
			return json.loads(response[1].decode('utf-8'))
		elif response[0] == 400:
			print("Group is invalid or does not exist")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Insufficient permissions to complete the request")
		return None
	
	# GET : "https://groups.roblox.com/v1/groups/{groupid}/settings"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_groupId_settings
	async def settings(self):
		groupid = self.groupid
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/settings', cookies=auth)
		if response[0] == 200:
			return json.loads(response[1].decode('utf-8'))
		elif response[0] == 400:
			print("Group is invalid or does not exist")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Insufficient permissions to complete the request")
		return None
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/settings"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_settings
	async def updateSettings(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		request = kwargs.get("request", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/settings', payload=request, cookies=auth)
		if response[0] == 200:
			return True
		elif response[0] == 400:
			print("Group is inavlid or does not exist")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Token validation failed or Insufficient permissions to complete the request")
		elif response[0] == 503:
			print("Service is currently unavilable")
		return False
	
	# GET : "https://groups.roblox.com/v1/groups/configuration/metadata"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_configuration_metadata
	async def configMetadata(self):
		response = await Req.request(t="GET", url='https://groups.roblox.com/v1/groups/configuration/metadata')
		return json.loads(response[1].decode('utf-8'))
	
	# GET : "https://groups.roblox.com/v1/groups/metadata"
	# Docs : https://groups.roblox.com/docs#!/Groups/get_v1_groups_metadata
	async def metadata(self):
		response = await Req.request(t="GET", url='https://groups.roblox.com/v1/groups/metadata')
		return json.loads(response[1].decode('utf-8'))
	
	# POST : "https://groups.roblox.com/v1/groups/create"
	# Docs : https://groups.roblox.com/docs#!/Groups/post_v1_groups_create
	async def create(self,**kwargs):
		auth = self.auth
		request = kwargs.get("request")
		response = await Req.request(t="POST", url='https://groups.roblox.com/v1/groups/create', payload=request, cookies=auth)
		if response[0] == 200:
			return json.loads(response[1].decode('utf-8'))
		elif response[0] == 400:
			print("The name is invalid, group icon is invalid, group icon is missing from request, the description is too long, the name is too long or the name has been taken")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Token validation failed, user must have builders club membership, user is in maximum number of groups, insufficient robux funds or the name is moderated")
		elif response[0] == 413:
			print("The group icon file size is too large")
		elif response[0] == 429:
			print("Too many requests")
		elif response[0] == 503:
			print("Group creation is currently disabled")
		return None
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/description"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_description
	async def updateDescription(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		request = kwargs.get("request", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/description', payload=request, cookies=auth)
		if response[0] == 200:
			return True
		elif response[0] == 400:
			print("Group is invalid, does not exist or your group description was empty")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Token validation failed, the description is too long or insufficient permissions to complete the request")
		return False
	
	# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/status"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_groupId_status
	async def updateStatus(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		statusRequest = kwargs.get("statusRequest", None)
		response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/status', payload=statusRequest, cookies=auth)
		if response[0] == 200:
			return True
		elif response[0] == 400:
			print("Group is invalid, does not exist, you're not authorized to set the status of this group or missing group status content")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Token Validation Failed")
		return False
	
	# PATCH : "https://groups.roblox.com/v1/groups/icon"
	# Docs : https://groups.roblox.com/docs#!/Groups/patch_v1_groups_icon
	async def updateIcon(self,**kwargs):
		groupid = self.groupid
		auth = self.auth
		files = kwargs.get("files", None)
		response = await Req.request(t="PATCH", url='https://groups.roblox.com/v1/groups/icon', payload={"groupid": groupid,"files": files}, cookies=auth)
		if response[0] == 200:
			return True
		elif response[0] == 400:
			print("Group is inavlid, does not exist, the group icon is missing from the request, too many requests or invalid file type for group icon")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("Token Validation Failed or insufficient permission to complete the request")
		elif response[0] == 413:
			print("Unknown Error")
		return False

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
			elif response[0] == 400:
				print("Group is invalid, does not exist or the user is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed")
			return False
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/join-requests"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_join_requests
		async def getJoinRequests(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet			
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You have insufficient permissions for this request")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/join-requests"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_join_requests
		async def acceptJoinRequests(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("Group is invalid, does not exist, the user is invalid or does not exist or the group join request is invalid")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you're already in the maximum number of groups or you have insufficient permissions for this request")
			elif response[0] == 500:
				print("Something went wrong")
			elif response[0] == 503:
				print("The operation is temporarily unavailable")
			return False
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/delete_v1_groups_groupId_join_requests_users_userId
		async def denyJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The user is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to manage this member")
			return False
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_join_requests_users_userId
		async def getJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You have insufficient permissions for this request")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_join_requests_users_userId
		async def acceptJoinRequest(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/join-requests/users/{userid}', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The group is invalid or does not exist, the user is invalid or does not exist or the group join request is invalid")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you're already in the maximum number of groups or you have insufficient permissions for this request")
			elif response[0] == 503:
				print("The operation is temporarily unavailable")
			return False
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/membership"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_membership
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/membership', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			return None
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_roles
		async def roles(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			return None
		
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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 403:
				print("The roleset is invalid or does not exist")
			return None
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/users"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_groups_groupId_users
		async def userIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			sortOrder = kwargs.get("sortOrder", None) # Not used yet
			limit = kwargs.get("limit", None) # Not used yet
			cursor = kwargs.get("cursor", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/users', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/users"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_users
		async def join(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			joinGroupModel = kwargs.get("joinGroupModel", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/users', payload=joinGroupModel, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you must pass the captcha test before joining this group, you are already in the maximum number of groups, you do not have the builders club membership necessary to join this group or you cannot join a closed group")
			elif response[0] == 409:
				print("You have already requested to join this group or you are already a member of this group")
			elif response[0] == 429:
				print("Too many attempts to join the groups")
			elif response[0] == 503:
				print("The operation is temporarily unavailable")
			return False
		
		# GET : "https://groups.roblox.com/v1/user/groups/pending"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_user_groups_pending
		async def pendingIndex(self):
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/user/groups/pending', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			return None
		
		# GET : "https://groups.roblox.com/v1/users/{userid}/group-membership-status"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_users_userId_group_membership_status
		async def status(self,**kwargs):
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/users/{userid}/group-membership-status', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The user is invalid or does not exist")
			return None
		
		# GET : "https://groups.roblox.com/v1/users/{userid}/group/roles"
		# Docs : https://groups.roblox.com/docs#!/Membership/get_v1_users_userId_groups_roles
		async def rolesIndex(self,**kwargs):
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/users/{userid}/group/roles', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The user is invalid or does not exist")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/change-owner"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_change_owner
		async def newOwner(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			changeOwnserRequest = kwargs.get("changeOwnerRequest", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/change-owner', payload=changeOwnserRequest, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The group is invalid or does not exist, the user is invalid or does not exist, the user is not a member of the group or the user does not have the necessary level of premium membership")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you are not authorized to change the owner of this group")
			return False
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/claim-ownership"
		# Docs : https://groups.roblox.com/docs#!/Membership/post_v1_groups_groupId_claim_ownership
		async def claimOwnership(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/claim-ownership', payload={}, cookies=auth)
			if reponse[0] == 200:
				return True
			elif reponse[0] == 400:
				print("The group is invalid or does not exist")
			elif reponse[0] == 401:
				print("Authorization has been denied for this request")
			elif reponse[0] == 403:
				print("Token Validation Failed, you are not authorized to claim this group, this group already has an owner or too many attempts to claim groups")
			elif reponse[0] == 503:
				print("The operation is temporarily unavailable")
			return False
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/delete_v1_groups_groupId_users_userId
		async def exile(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/users/{userid}', payload={}, cookies=auth)
			if reponse[0] == 200:
				return True
			elif reponse[0] == 400:
				print("The group is invalid, the group does not exist, the user is invalid or the user does not exist")
			elif reponse[0] == 401:
				print("Authorization has been denied for this request")
			elif reponse[0] == 403:
				print("Token Validation Failed or you do not have permission to manage this member")
			elif reponse[0] == 503:
				print("The operation is temporarily unavailable")
			return False
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/users/{userid}"
		# Docs : https://groups.roblox.com/docs#!/Membership/patch_v1_groups_groupId_users_userId
		async def promote(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userid = kwargs.get("userid", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/users/{userid}', payload=request, cookies=auth)
			if reponse[0] == 200:
				return True
			elif reponse[0] == 200:
				print("The group is invalid, the group does not exist, the rolset is invalid, the roleset does not exist, the user is invalid or the user does not exist or you cannot change your role")
			elif reponse[0] == 200:
				print("Authorization has been denied for this request")
			elif reponse[0] == 200:
				print("Token Validation Failed or you do not have permission to manage this member")
			elif reponse[0] == 200:
				print("The operation is temporarily unavailable")
			return False


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You don't have permission to view this group's payouts")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/payouts"
		# Docs : https://groups.roblox.com/docs#!/Revenue/post_v1_groups_groupId_payouts
		async def pay(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/payouts', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("Group is invalid, the group does not exist, insufficent Robux funds, invalid payout type, the amount is invalid or too many recipients")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or insufficient permissions to complete the request")
			elif response[0] == 503:
				print("The feature is disabled")
			return False
		
		# POST : "https://groups.roblox.com/v1/groups/{groupId}/payouts/recurring"
		# Docs : https://groups.roblox.com/docs#!/Revenue/post_v1_groups_groupId_payouts_recurring
		async def update(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/payouts/recurring', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("Group is invalid, the group does not exist, insufficent Robux funds, invalid payout type, the amount is invalid or too many recipients")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or insufficient permissions to complete the request")
			elif response[0] == 503:
				print("The feature is disabled")
			return False
		

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
			if reponse[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid, group does not exist, group relationship type, the request type is invalid or the request is invalid or the request is missing pagination parameters")
			return None
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/delete_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchDecline(self,**kwarg):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="DELETE", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', payload=request, cookies=auth)
			if reponse[0] == 200:
				return True
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed")
			return False
		
		# GET : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/get_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchGet(self,**kwarg):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			startRowIndex = kwargs.get("startRowIndex", None) # Not used yet
			maxRows = kwargs.get("maxRows", None) # Not used yet
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', cookies=auth)
			if reponse[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid, group does not exist, group relationship type, request type is invalid, invalid or missing pagination parameters")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You don't have permission to manage this group's relationships")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupId}/relationships/{groupRelationshipType}/requests"
		# Docs : https://groups.roblox.com/docs#!/Relationships/post_v1_groups_groupId_relationships_groupRelationshipType_requests
		async def batchAccept(self,**kwarg):
			groupid = self.groupid
			auth = self.auth
			groupRelationshipType = kwargs.get("groupRelationshipType", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/relationships/{groupRelationshipType}/requests', payload=request, cookies=auth)
			if reponse[0] == 200:
				return True
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed")
			return False
		
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
			elif response[0] == 400:
				print("Invalid group, target group is invalid, target group does not exist or relationship does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you are blocked from communicating with this user")
			return False
		
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
			elif response[0] == 400:
				print("Group relationship type, request type is invalid, invalid group, target group is invalid, group does not exist or your group cannot establish a relationship with itself")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, your group does not allow enemy declarations, other group does not allow enemy declarations, your group already has a relationship with the target group, you are blocked from communicating with this user or insufficient permissions")
			return False

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
			elif response[0] == 400:
				print("Group relationship type or request type is invalid")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or insufficient permissions")
			return False

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
			elif response[0] == 400:
				print("Group relationship type or request type is invalid")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or insufficient permissions")
			return False


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is valid, group does not exist, the rolset is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You are not authorized to view/edit permissions for this role")
			return None
		
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
			elif response[0] == 400:
				print("Group is valid, group does not exist, the rolset is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you are not authorized to view/edit permissions for this role or this role's permissions can not be modified")
			return False
		
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/get_v1_groups_groupId_roles_guest_permissions
		async def guestIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			roleSetId = kwargs.get("roleSetId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/{roleSetId}/permissions', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			return None
		
	
		# GET : "https://groups.roblox.com/v1/groups/{groupid}/roles/permissions"
		# Docs : https://groups.roblox.com/docs#!/Permissions/get_v1_groups_groupId_roles_permissions
		async def get(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/{groupid}/roles/permissions', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			return None


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Only users who are over thirteen years of age may edit social links")
			elif response[0] == 404:
				print("Social link cannot be processed at this time")
			return None
		
		# POST : "https://groups.roblox.com/v1/groups/{groupid}/social-links"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/post_v1_groups_groupId_social_links
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/social-links', payload=request, cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The social link title is too long, the social link title cannot be empty, the social link url cannot be empty, the request was null, the social link type is invalid or the social link title was moderated")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to configure this social link")
			elif response[0] == 404:
				print("The requested group or social link was not found")
			elif response[0] == 503:
				print("Social links cannot be processed at this time")
			return None
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}"
		# Docs : https://groups.roblox.com/docs#!/SocialLinks/delete_v1_groups_groupId_social_links_socialLinkId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			socialLinkId = kwargs.get("", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/social-links/{socialLinkId}', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("Group is invalid, group does not exist, the social link is not for a group or the social link id doesn't match the group id")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you do not have permission to configure this social link or only users who are over thirteen years of age may edit social links")
			elif response[0] == 404:
				print("Social links cannot be processed at this time")
			return False
		
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
			elif response[0] == 400:
				print("Group is invalid or does not exist, the social link title is too long, the social link title cannot be empty, the social link url cannot be empty, the social link url was improperly formatted, the request was null, the requested group or social link was not found, the social link is not for a group, the social link title was moderated or a social link with this type already exists on this group")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to configure this social link")
			elif response[0] == 404:
				print("Social links cannot be processed at this time")
			elif response[0] == 503:
				print("Social links cannot be processed at this time")
			return False


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 403:
				print("You do not have permission to access this group wall")
			return None

		# POST : "https://groups.roblox.com/v1/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/post_v1_groups_groupId_wall_posts
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/posts', payload=request, cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid, group does not exist, your post was empty, your post was white space or your post is more than 500 characters")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you do not have permission to access this group wall or captcha must be solved")
			elif response[0] == 429:
				print("You are posting too fast, please try again in a few minutes")
			return None
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/wall/posts/{postId}"
		# Docs : https://groups.roblox.com/docs#!/Wall/delete_v1_groups_groupId_wall_posts_postId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			postId = kwargs.get("postId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/posts/{postId}', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The group is invalid, group does not exist, the group wall post id is invalid or the group wall post id is invalid")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to access this group wall")
			return False
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/wall/users/{userId}/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/delete_v1_groups_groupId_wall_users_userId_posts
		async def deleteFromUserid(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/wall/users/{userId}/posts', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("The group is invalid, group does not exist, the user specified is invalid or the user specified does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to access this group wall")
			return False
	

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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Search term not appropriate for Roblox, search term as left empty or the search term can be only 2 to 50 characters long")
			return None
		
		# GET : "https://groups.roblox.com/v1/groups/search/lookup"
		# Docs : https://groups.roblox.com/docs#!/GroupSearch/get_v1_groups_search_lookup
		async def byExactMatch(self,**kwargs):
			auth = self.auth
			groupName = kwargs.get("groupName", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/search/lookup?groupName={groupName}', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Name is missing or has invalid characters")
			return None
		
		# GET : "https://groups.roblox.com/v1/groups/search/metadata"
		# Docs : https://groups.roblox.com/docs#!/GroupSearch/get_v1_groups_search_metadata
		async def metadata(self):
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v1/groups/search/metadata', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 404:
				print("No Localized Version of group search category exists")
			return None


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Ids could not be parsed from request or too many ids in request")
			return None
	
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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("User is invalid or does not exist")
			elif response[0] == 404:
				print("The user specified does not have a primary group")
			return None
		
		# DELETE : "https://groups.roblox.com/v1/user/groups/primary"
		# Docs : https://groups.roblox.com/docs#!/PrimaryGroup/delete_v1_user_groups_primary
		async def remove(self):
			groupid = self.groupid
			auth = self.auth
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/user/groups/primary', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed")
			return False
		
		# POST : "https://groups.roblox.com/v1/user/groups/primary"
		# Docs : https://groups.roblox.com/docs#!/PrimaryGroup/post_v1_user_groups_primary
		async def setTo(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v1/user/groups/primary', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you aren't a member of the group specified")
			return False
		
	
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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Check line 1071 of groups.py in the Pyblox3 library")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permissions to perform this action")
			return None
		
		# DELETE : "https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}"
		# Docs : https://groups.roblox.com/docs#!/RoleSets/delete_v1_groups_groupId_rolesets_rolesetId
		async def delete(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			rolesetId = kwargs.get("rolesetId", None)
			response = await Req.request(t="DEL", url=f'https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}', cookies=auth)
			if response[0] == 200:
				return True
			elif response[0] == 400:
				print("This group does not exist, this role does not exist, cannot remove any more roles or cannot delete this role")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you do not have permissions to perform this action or there are users in this role")
			return False
		
		# PATCH : "https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}"
		# Docs : https://groups.roblox.com/docs#!/RoleSets/patch_v1_groups_groupId_rolesets_rolesetId
		async def update(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			rolesetId = kwargs.get("rolesetId", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://groups.roblox.com/v1/groups/{groupid}/rolesets/{rolesetId}', payload=request, cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Check line 1105 of groups.py in the Pyblox3 library")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permissions to perform this action")
			return None


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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Too mnay ids in request or ids could not be parsed from request")
			return None
		
		# GET : "https://groups.roblox.com/v2/users/{userId}/groups/roles"
		# Docs : https://groups.roblox.com/docs#!/Groups/get_v2_users_userId_groups_roles
		async def roleIndex(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="GET", url=f'https://groups.roblox.com/v2/users/{userId}/groups/roles', cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The user is invalid or does not exist")
			return None
	

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
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")
			elif response[0] == 403:
				print("You do not have permission to access this group wall")
			return None
		
		# POST : "https://groups.roblox.com/v2/groups/{groupid}/wall/posts"
		# Docs : https://groups.roblox.com/docs#!/Wall/post_v2_groups_groupId_wall_posts
		async def post(self,**kwargs):
			groupid = self.groupid
			auth = self.auth
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://groups.roblox.com/v2/groups/{groupid}/wall/posts', payload=request, cookies=auth)
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid, does not exist, your post was empty, white space, or more than 500 characters")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed, you do not have permission to access this group wall or captcha must be solved")
			elif response[0] == 429:
				print("You are posting too fast, please try again in a few minutes")
			return None