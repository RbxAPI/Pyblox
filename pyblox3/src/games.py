#
#  games.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class Games_v1:

	def __init__(self, **kwargs):
		auth = kwargs.get("auth", None)
		self.auth = auth.auth_cookies
		self.Favorites = self.Favorites(self)
		self.GamePasses = self.GamePasses(self)
		self.Votes = self.Votes(self)
		self.VipServers = self.VipServers(self)

	# GET : "https://games.roblox.com/v1/games"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games
	async def get(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games', cookies=auth)
		return response[4]
    
    # GET : "https://games.roblox.com/v1/games/{placeId}/servers/{serverType}"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_placeId_servers_serverType
	async def getServers(self,**kwargs):
		auth = self.auth
		placeId = kwargs.get("placeId", None)
		serverType = kwargs.get("serverType", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/{placeId}/servers/{serverType}', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/games-product-info"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_games_product_info
	async def getProductInfoList(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/games-product-info', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/list"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_list
	async def getGamesList(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/list', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/list-spotlight"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_list_spotlight
	async def getGamesListSpotlight(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/list-spotlight', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/multiget-place-details"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_multiget_place_details
	async def getMuliPlaceDetails(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/multiget-place-details', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/multiget-playability-status"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_multiget_playability_status
	async def getMuliPlaceDetails(self):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/multiget-playability-status', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/recommendations/algorithm/{algorithmName}"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_recommendations_algorithm_algorithmName
	async def getGameRecommendations(self,**kwargs):
		auth = self.auth
		algorithmName = kwargs.get("algorithmName", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/recommendations/algorithm/{algorithmName}', cookies=auth)
		return response[4]

	# GET : "https://games.roblox.com/v1/games/recommendations/game/{universeId}"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_recommendations_game_universeId
	async def getGameRecommendationByUniverse(self,**kwargs):
		auth = self.auth
		universeId = kwargs.get("universeId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/recommendations/game/{universeId}', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v1/games/sorts"
	# Docs : https://games.roblox.com/docs#!/Games/get_v1_games_sorts
	async def getOrderedListSorts(self,**kwargs):
		auth = self.auth
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/sorts', cookies=auth)
		return response[4]
	

	class Favorites:

		def __init__(self,Games_v1):
			self.Games_v1 = Games_v1
			self.auth = Games_v1.auth
		
		# GET : "https://games.roblox.com/v1/games/{universeId}/favorites"
		# Docs : https://games.roblox.com/docs#!/Favorites/get_v1_games_universeId_favorites
		async def getbyUniverse(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/{universeId}/favorites', cookies=auth)
			return response[4]
		
		# POST : "https://games.roblox.com/v1/games/{universeId}/favorites"
		# Docs : https://games.roblox.com/docs#!/Favorites/post_v1_games_universeId_favorites
		async def mark(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="POST", url=f'https://games.roblox.com/v1/games/{universeId}/favorites', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
		
		# GET : "https://games.roblox.com/v1/games/{universeId}/favorites/count"
		# Docs : https://games.roblox.com/docs#!/Favorites/get_v1_games_universeId_favorites_count
		async def getCountbyUniverse(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/{universeId}/favorites/count', cookies=auth)
			return response[4]


	class GamePasses:

		def __init__(self,Games_v1):
			self.Games_v1 = Games_v1
			self.auth = Games_v1.auth
		
		# GET : "https://games.roblox.com/v1/games/{universeId}/game-passes"
		# Docs : https://games.roblox.com/docs#!/GamePasses/get_v1_games_universeId_game_passes
		async def getByUniverse(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/{universeId}/game-passes', cookies=auth)
			return response[4]
	
	class Votes:

		def __init__(self,Games_v1):
			self.Games_v1 = Games_v1
			self.auth = Games_v1.auth
		
		# GET : "https://games.roblox.com/v1/games/{universeId}/votes/user"
		# Docs : https://games.roblox.com/docs#!/Votes/get_v1_games_universeId_votes_user
		async def getByUniverse(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/{universeId}/votes/user', cookies=auth)
			return response[4]
		
		# GET : "https://games.roblox.com/v1/games/votes"
		# Docs : https://games.roblox.com/docs#!/Votes/get_v1_games_votes
		async def getVotes(self,**kwargs):
			auth = self.auth
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/games/votes', cookies=auth)
			return response[4]
		
		# PATCH : "https://games.roblox.com/v1/games/{universeId}/user-votes"
		# Docs : https://games.roblox.com/docs#!/Votes/patch_v1_games_universeId_user_votes
		async def cast(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			requestBody = kwargs.get("requestBody", None)
			response = await Req.request(t="PATCH", url=f'https://games.roblox.com/v1/games/{universeId}/user-votes', payload=requestBody, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
	
	class VipServers:

		def __init__(self,Games_v1):
			self.Games_v1 = Games_v1
			self.auth = Games_v1.auth
		
		# GET : "https://games.roblox.com/v1/vip-server/can-invite/{userId}"
		# Docs : https://games.roblox.com/docs#!/VipServers/get_v1_vip_server_can_invite_userId
		async def canJoin(self,**kwargs):
			auth = self.auth
			userId = kwargs.get("userId", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/vip-server/can-invite/{userId}', cookies=auth)
			return response[4]
		
		# GET : "https://games.roblox.com/v1/vip-servers/{id}"
		# Docs : https://games.roblox.com/docs#!/VipServers/get_v1_vip_servers_id
		async def get(self,**kwargs):
			auth = self.auth
			id = kwargs.get("id", None)
			response = await Req.request(t="GET", url=f'https://games.roblox.com/v1/vip-servers/{id}', cookies=auth)
			return response[4]
		
		# PATCH : "https://games.roblox.com/v1/vip-servers/{id}"
		# Docs : https://games.roblox.com/docs#!/VipServers/patch_v1_vip_servers_id
		async def update(self,**kwargs):
			auth = self.auth
			id = kwargs.get("id", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://games.roblox.com/v1/vip-servers/{id}', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
		
		# POST : "https://games.roblox.com/v1/games/vip-servers/{universeId}"
		# Docs : https://games.roblox.com/docs#!/VipServers/post_v1_games_vip_servers_universeId
		async def create(self,**kwargs):
			auth = self.auth
			universeId = kwargs.get("universeId", None)
			requestBody = kwargs.get("requestBody", None)
			response = await Req.request(t="POST", url=f'https://games.roblox.com/v1/games/vip-servers/{universeId}', payload=requestBody, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
		
		# PATCH : "https://games.roblox.com/v1/vip-servers/{id}/permissions"
		# Docs : https://games.roblox.com/docs#!/VipServers/patch_v1_vip_servers_id_permissions
		async def updatePermissions(self,**kwargs):
			auth = self.auth
			id = kwargs.get("id", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://games.roblox.com/v1/vip-servers/{id}/permissions', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
		
		# PATCH : "https://games.roblox.com/v1/vip-servers/{id}/subscription"
		# Docs : https://games.roblox.com/docs#!/VipServers/patch_v1_vip_servers_id_subscription
		async def updateSubscriptionStatus(self,**kwargs):
			auth = self.auth
			id = kwargs.get("id", None)
			request = kwargs.get("request", None)
			response = await Req.request(t="PATCH", url=f'https://games.roblox.com/v1/vip-servers/{id}/subscription', payload=request, cookies=auth)
			if response[0] == 200:
				return True
			return False, response[4]
		
class Games_v2:

	def __init__(self, **kwargs):
		auth = kwargs.get("auth", None)

	# GET : "https://games.roblox.com/v2/games/{universeId}/media"
	# Docs : https://games.roblox.com/docs#!/Games/get_v2_games_universeId_media
	async def getMediaData(self,**kwargs):
		auth = self.auth
		universeId = kwargs.get("universeId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v2/games/{universeId}/media', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v2/groups/{groupId}/games"
	# Docs : https://games.roblox.com/docs#!/Games/get_v2_groups_groupId_games
	async def getCreatedByGroup(self,**kwargs):
		auth = self.auth
		groupId = kwargs.get("groupId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v2/groups/{groupId}/games', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v2/groups/{groupId}/gamesV2"
	# Docs : https://games.roblox.com/docs#!/Games/get_v2_groups_groupId_gamesV2
	async def getCreatedByGroupV2(self,**kwargs):
		auth = self.auth
		groupId = kwargs.get("groupId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v2/groups/{groupId}/gamesV2', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v2/users/{userId}/favorite/games"
	# Docs : https://games.roblox.com/docs#!/Games/get_v2_users_userId_favorite_games
	async def getFavoriteByUser(self,**kwargs):
		auth = self.auth
		userId = kwargs.get("userId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v2/users/{userId}/favorite/games', cookies=auth)
		return response[4]
	
	# GET : "https://games.roblox.com/v2/users/{userId}/games"
	# Docs : https://games.roblox.com/docs#!/Games/get_v2_users_userId_games
	async def getCreatedByUser(self,**kwargs):
		auth = self.auth
		userId = kwargs.get("userId", None)
		response = await Req.request(t="GET", url=f'https://games.roblox.com/v2/users/{userId}/games', cookies=auth)
		return response[4]