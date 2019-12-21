#
#  group.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json

# Group Object
class Group:
    Name = None
    Id = None
    Owner = None
    OwnerName = None
    OwnerId = None
    EmblemUrl = None
    Description = None
    Roles = None
    
    def __init__(self,data):
        self.Name = data["Name"]
        self.Id = data["Id"]
        self.Owner = data["Owner"]
        self.OwnerName = data["Owner"]["Name"]
        self.OwnerId = data["EmblemUrl"]
        self.EmblemUrl = data["EmblemUrl"]
        self.Description = data["Description"]
        self.Roles = data["Roles"]

class Groups:

    # GET /users/{userId}/groups
    # returns table/array with groups + each group's attributes
    def groupList(userid):
        a = Http.sendRequest("https://api.roblox.com/users/" + str(userid) + "/groups")
        return a

    # GET /groups/{groupId}
    # Returns Table/Array + Attributes
    def getGroup(groupid):
        a = Http.sendRequest("https://api.roblox.com/groups/" + str(groupid))
        b = a.decode("utf-8")
        c = json.loads(b)
        return Group(c)

    # GET /groups/{groupId}/allies
    # Returns Table/Array with each ally's attributes
    def getGroupAllies(groupid):
        a = Http.sendRequest("https://api.roblox.com/groups/" + str(groupid) + "/allies")
        return a

    # GET /groups/{groupId}/enemies
    # Returns Table/Array with each enemy's attributes
    def getGroupEnemies(groupid):
        a = Http.sendRequest("https://api.roblox.com/groups/" + str(groupid) + "/enemies")
        return a

    # GET /groups/{groupId}/roles
    # Returns a Table/Array with each role.
    def getGroupRoles(groupid):
        a = Http.sendRequest("https://groups.roblox.com/v1/groups/" + str(groupid) + "/roles")
        return a
