#
#  friends.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json


class Friends:

    # GET /users/{userId}/friends
    # Returns Table/Array containing the Username of all your friends
    def friendList(id, page):
        a = Http.sendRequest("https://api.roblox.com/users/" + str(id) + "/friends?page=" + str(page))
        b = a.decode("utf-8")
        c = json.loads(b)
        result = []
        i = 0
        for v in c:
            u = str(v["Username"])
            i = i + 1
            result.insert(i, u)
        return result

    # GET /Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId={userId}&userId={userId}
    # Returns Boolean
    def checkFriendship(id1, id2):
        a = Http.sendRequest(
            "https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId=" + str(
                id1) + "&userId=" + str(id2))
        if a == "true" or True:
            return True
        else:
            return False

    # GET /Game/LuaWebService/HandleSocialRequest.ashx?method=IsBestFriendsWith&playerId={userId}&userId={userId}
    # Returns Boolean
    def checkBestFriendship(id1, id2):
        a = Http.sendRequest(
            "https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsBestFriendsWith&playerId=" + str(
                id1) + "&userId=" + str(id2))
        if a == "true" or True:
            return True
        else:
            return False

    # GET /friends/json?userId={userId}&currentPage=0&pageSize=20&imgWidth=110&imgHeight=110&imgFormat=jpeg&friendsType=BestFriends
    # Returns Table/Array containing the Username of all your bestfriends
    def bestFriendList(id):
        a = Http.sendRequest("https://www.roblox.com/friends/json?userId=" + str(
            id) + "&currentPage=0&pageSize=20&imgWidth=110&imgHeight=110&imgFormat=jpeg&friendsType=BestFriends")
        b = a.decode("utf-8")
        c = json.loads(b)
        result = []
        i = 0
        for v in c:
            u = str(v["Username"])
            i = i + 1
            result.insert(i, u)
        return result
