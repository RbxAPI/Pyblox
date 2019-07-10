#
#  groups.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json
from bs4 import BeautifulSoup

root = "https://groups.roblox.com"

class Groups_v1:

	async def get(**kwargs):
		groupid = kwargs.get("groupid",None)
		fetchObject = kwargs.get("Object",None)
		response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid))
		
		if response[0] == 400:
			print("Group is invalid or does not exist")
		else:
			result = json.loads(response[1].decode('utf-8'))
			if result != None and fetchObject:
				group_instance = Groups(group)

			elif result != None and not fetchObject:
				return result

	async def payoutsInfo(**kwargs):
		groupid = kwargs.get("groupid",None)
		response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/payouts")
		if response[0] == 400:
			print("Group is invalid or does not exist")
		elif response[0] == 401:
			print("Authorization has been denied for this request")
		elif response[0] == 403:
			print("You don't have permission to view this group's payouts")
		else:
			return json.loads(response[1].decode('utf-8'))

	#def relationship(**kwargs): # Requires token validation
	#def relationshipRequests(): # Requires token validation
	#def create(): # Requires token validation
	
	async def metadata():
		response = await Req.request(t="GET",url=root+"/v1/groups/metadata")
		if response[0] == 200:
			return json.loads(response[1].decode('utf-8'))
		else:
			print("No access to the internet or website is down")
	
	#def status(**kwargs): # Requires token validation

	class Membership:

		async def get(**kwargs):
			groupid = kwargs.get("groupid",None)
			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/membership")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")


		async def roles(**kwargs):
			groupid = kwargs.get("groupid",None)
			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/roles")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The group is invalid or does not exist")

		#def role(**kwargs): # Doesn't work for some odd reason
		#def pending(**kwargs): # Requires token validation

		async def status(**kwargs):
			userid = kwargs.get("userid",None)
			response = await Req.request(t="GET",url=root+"/v1/users/"+str(userid)+"/group-membership-status")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The user is invalid or does not exist")

		async def allRoles(**kwargs):
			userid = kwargs.get("userid",None)
			response = await Req.request(t="GET",url=root+"/v1/users/"+str(userid)+"/groups/roles")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("The user is invalid or does not exist")

		async def getJoinRequests(**kwargs):
			groupid = kwargs.get('groupid', None)
			response = await Req.request(t='GET', url='https://www.roblox.com/groups/'+str(groupid)+'/joinrequests-html?pageNum=1')
			soup = BeautifulSoup(response[1], 'html.parser')
			tr = soup.find('tbody').find_all('tr')
			del tr[-1]
			requests = []
			for request in tr:
				requests.append({
					'JoinId': request.find('span', {"class": "btn-control btn-control-medium accept-join-request"})[
						'data-rbx-join-request'],
					'User': {
						'AvatarPicture': request.td.span.img['src'],
						'Username': request.find('a').text,
						'Id': re.findall(r'\b\d+\b', request.find('a')['href']),
						'ProfileLink': request.find('a')['href']
					}
				})
			return requests
		#def claimOwnership(): # Requires token validation
		#def join(): # Requires token validation
		#def exile(): # Requires token validation
		#def updateRole(): # Requires token validation
		#def declineJoinRequest(): # Requires token validation

	class Revenue:
		async def payoutPercentages(**kwargs): #Doesn't work for some reason
			groupid = kwargs.get("groupid",None)
			cache = kwargs.get("cache",None)
			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/payouts")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("You don't have permission to view this group's payouts")

		#def pay(): # Requires token validation
		#def updateReocurringPayout(): # Requires token validation

	class Relationships:

		async def get(**kwargs):
			groupid = kwargs.get("groupid",None)
			groupRelationshipType = kwargs.get("groupRelationshipType",None)
			startRowIndex = kwargs.get("startRowIndex",None)
			maxRows = kwargs.get("maxRows",None)

			if maxRows < 1:
				maxRows = 1

			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/relationships/"+str(groupRelationshipType)+"?model.startRowIndex="+str(startRowIndex)+"&model.maxRows="+str(maxRows))
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist; Group relationship type or request type is invalid; Invalid or missing pagination parameters")

		#def requests(): # Requires token validation
		#def delete(): # Requires token validation
		#def create(): # Requires token validation
		#def decline(): # Requires token validation
		#def accept(): # Requires token validation

	class Permissions:

		#def get(): # Doesn't work for some reason

		async def guest(**kwargs):
			groupid = kwargs.get("groupid",None)
			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/roles/guest/permissions")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")

	class socialLinks:

		async def get(**kwargs): # Authorization denied for this request
			groupid = kwargs.get("groupid",None)
			response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/social-links")
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization is denied for this request")
			elif response[0] == 403:
				print("Only users who are over thirteen years of age may edit social links")
			elif response[0] == 404:
				print("Social links cannot be processed at this time")

		#def post(): # Requires token validation
		#def delete(): # Requires token validation
		#def update(): # Requires token validation

	class Wall:

		async def getNextCursor(**kwargs):
			groupid = kwargs.get("groupid",None)
			cursor = kwargs.get("cursor",None)
			if not cursor:
				response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/wall/posts?sortOrder=Asc&limit=10")
				if response[0] == 200:
					return json.loads(response[1].decode('utf-8')["nextPageCursor"])
				else:
					return None

		async def get(**kwargs):
			groupid = kwargs.get("groupid",None)
			cursor = kwargs.get("cursor",None)
			if not cursor:
				response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/wall/posts?sortOrder=Asc&limit=10")
				if response[0] == 200:
					return json.loads(response[1].decode('utf-8'))
				elif response[0] == 400:
					print("The group is invalid or does not exist")
				elif response[0] == 403:
					print("You do not have permission to access this group wall")
			elif cursor:
				response = await Req.request(t="GET",url=root+"/v1/groups/"+str(groupid)+"/wall/posts?sortOrder=Asc&limit=10&cursor="+str(cursor))
				if response[0] == 200:
					return json.loads(response[1].decode('utf-8'))
				elif response[0] == 400:
					print("The group is invalid or does not exist")
				elif response[0] == 403:
					print("You do not have permission to access this group wall")

		async def post(**kwargs):
			groupid = kwargs.get("groupid",None)
			body = kwargs.get("body",None)
			response = await Req.request(t="POST",url=root+"/v1/groups/"+str(groupid)+"/wall/posts",payload={"body":str(body)},header=Cached.cache,cookies={'.ROBLOSECURITY': Cached.file_cache[".ROBLOSECURITY"]})
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has been denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed")
			elif response[0] == 429:
				print("You are posting too fast, please try again in a few minutes")

		async def delete(**kwargs):
			groupid = kwargs.get("groupid",None)
			postid = kwargs.get("postid",None)
			response = await Req.request(t="DEL",url=root+"/v1/groups/"+str(groupid)+"/wall/posts/"+str(postid),header=Cached.cache,cookies={'.ROBLOSECURITY': Cached.file_cache[".ROBLOSECURITY"]})
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group or post id is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has beed denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to access this group wall")

		async def purgeDelete(**kwargs):
			groupid = kwargs.get("groupid",None)
			userid = kwargs.get("userid",None)
			response = await Req.request(t="DEL",url=root+"/v1/groups/"+str(groupid)+"/wall/users/"+str(userid)+"/posts",header=Cached.cache,cookies={'.ROBLOSECURITY': Cached.file_cache[".ROBLOSECURITY"]})
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Group or user id is invalid or does not exist")
			elif response[0] == 401:
				print("Authorization has beed denied for this request")
			elif response[0] == 403:
				print("Token Validation Failed or you do not have permission to access this group wall")

	class Roles:

		async def roles(**kwargs):
			roleid = kwargs.get("roleid",None)
			response = await Req.request(t="GET",url=root+"/v1/roles/?ids="+str(roleid))
			if response[0] == 200:
				return json.loads(response[1].decode('utf-8'))
			elif response[0] == 400:
				print("Ids could not be parsed from request or too many ids in request")

	#class PrimaryGroup:
		
		'''

			class primaryGroup:

				def getRole():
				def remove():
				def set():


		class Groups_v2:

			def get():

			class Wall:

				def get():
				def post():
		'''


