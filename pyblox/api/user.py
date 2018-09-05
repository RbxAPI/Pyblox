#
#  user.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json


class User:

    # GET https://www.roblox.com/UserCheck/DoesUsernameExist?username={username}
    # Returns Boolean
    def checkUsernameExists(username):
        a = Http.sendRequest("https://www.roblox.com/UserCheck/DoesUsernameExist?username=" + str(username))
        b = a.decode("utf-8")
        c = json.loads(b)
        if c["success"] == "True" or True:
            return True
        else:
            return False

    # GET https://api.roblox.com/users/get-by-username?username={username}
    # Returns Table/Array + Attributes
    def getUser(username):
        a = Http.sendRequest("https://api.roblox.com/users/get-by-username?username=" + str(username))
        b = a.decode("utf-8")
        c = json.loads(b)
        global User
        User = lambda: None
        User.Id = c["Id"]
        User.Username = c["Username"]
        User.AvatarUrl = c["AvatarUri"]
        User.AvatarFinal = c["AvatarFinal"]
        User.IsOnline = c["IsOnline"]
        return User

    # GET https://www.roblox.com/Asset/BodyColors.ashx?userId={userId}
    # Returns Table/Array
    def getUserBodyColors(id):
        a = Http.sendRequest("https://www.roblox.com/Asset/BodyColors.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId={userId}
    # Returns Table/Array
    def getAssetsWorn(id):
        a = Http.sendRequest("https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/Asset/CharacterFetch.ashx?userId={userId}&placeId={placeId}
    # Returns Table/Array
    def getAssetVersions(id, placeid):
        a = Http.sendRequest(
            "https://www.roblox.com/Asset/CharacterFetch.ashx?userId=" + str(id) + "&placeId=" + str(placeid))
        return a

    # GET https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId={userId}
    # Returns Table/Array
    def getUserPlaces(id):
        a = Http.sendRequest("https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/badges/roblox?userId={userId}&imgWidth=110&imgHeight=110&imgFormat=png
    # Return Table/Array
    def getUserBadges(id):
        a = Http.sendRequest(
            "https://www.roblox.com/badges/roblox?userId=" + str(id) + "&imgWidth=110&imgHeight=110&imgFormat=png")
        return a
