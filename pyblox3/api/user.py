#
#  user.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json

# User Object
class User:
    Id = None
    Username = None
    AvatarUri = None
    AvatarFinal = None
    IsOnline = None
    
    def __init__(self,data):
        self.Id = data["Id"]
        self.Username = data["Username"]
        self.AvatarUri = data["AvatarUri"]
        self.AvatarFinal = data["AvatarFinal"]
        self.IsOnline = data["IsOnline"]

class Users:

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
    def User(username):
        a = Http.sendRequest("https://api.roblox.com/users/get-by-username?username=" + str(username))
        b = a.decode("utf-8")
        c = json.loads(b)
        return User(c)

    # GET https://www.roblox.com/Asset/BodyColors.ashx?userId={userId}
    # Returns Table/Array
    def BodyColors(id):
        a = Http.sendRequest("https://www.roblox.com/Asset/BodyColors.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId={userId}
    # Returns Table/Array
    def AssetsWorn(id):
        a = Http.sendRequest("https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/Asset/CharacterFetch.ashx?userId={userId}&placeId={placeId}
    # Returns Table/Array
    def AssetVersions(id, placeid):
        a = Http.sendRequest(
            "https://www.roblox.com/Asset/CharacterFetch.ashx?userId=" + str(id) + "&placeId=" + str(placeid))
        return a

    # GET https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId={userId}
    # Returns Table/Array
    def Places(id):
        a = Http.sendRequest("https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId=" + str(id))
        return a

    # GET https://www.roblox.com/badges/roblox?userId={userId}&imgWidth=110&imgHeight=110&imgFormat=png
    # Return Table/Array
    def Badges(id):
        a = Http.sendRequest(
            "https://www.roblox.com/badges/roblox?userId=" + str(id) + "&imgWidth=110&imgHeight=110&imgFormat=png")
        return a
