#
#  users.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2020- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class Users_v1:

    def __init__(self,**kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies
        self.Users = self.Users(self)
        self.userSearch = self.userSearch(self)

    class Users:

        def __init__(self,Users_v1):
            self.Users_v1 = Users_v1
            self.auth = Users_v1.auth
        
        # GET : "https://users.roblox.com/v1/users/{userId}"
        # Docs : https://users.roblox.com/docs#!/Users/get_v1_users_userId
        async def get(self,**kwargs):
            auth = self.auth
            userId = kwargs.get("userId", None)
            response = await Req.request(t="GET", url=f'https://users.roblox.com/v1/users/{userId}', cookies=auth)
            return response[4]
        
        # GET : "https://users.roblox.com/v1/users/authenticated"
        # Docs : https://users.roblox.com/docs#!/Users/get_v1_users_authenticated
        async def minAuth(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://users.roblox.com/v1/users/authenticated', cookies=auth)
            return response[4]

        # POST : "https://users.roblox.com/v1/usernames/users"
        # Docs : https://users.roblox.com/docs#!/Users/post_v1_usernames_users
        async def fromUsername(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://users.roblox.com/v1/usernames/users', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            else:
                return False, response[4]

        # POST : "https://users.roblox.com/v1/users"
        # Docs : https://users.roblox.com/docs#!/Users/post_v1_users
        async def fromId(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://users.roblox.com/v1/users', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            else:
                return False, response[4]

    class userSearch:

        def __init__(self,Users_v1):
            self.Users_v1 = Users_v1
            self.auth = Users_v1.auth
        
        # GET : "https://users.roblox.com/v1/users/search"
        # Docs : https://users.roblox.com/docs#!/UserSearch/get_v1_users_search
        async def fromKeyword(self,**kwargs):
            auth = self.auth
            keyword = kwargs.get("keyword", None)
            limit = kwargs.get("limit", None) # Not used yet
            keyword = kwargs.get("cursor", None) # Not used yet
            response = await Req.request(t="GET", url=f'https://users.roblox.com/v1/users/search?keyword={keyword}')
            return response[4]
            