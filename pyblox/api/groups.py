#
#  group.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
from bs4 import *
import html5lib
import urllib.request
import json


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
        global Group
        Group = lambda: None
        Group.Name = c["Name"]
        Group.Id = c["Id"]
        Group.Owner = c["Owner"]
        Group.Owner.Name = c["Owner"]["Name"]
        Group.Owner.Id = c["Owner"]["Id"]
        Group.EmblemUrl = c["EmblemUrl"]
        Group.Description = c["Description"]
        Group.Roles = c["Roles"]

    # GET /groups/{groupId}/allies
    # Returns Table/Array with each ally's attributes
    def getGroupAllies(groupid):
        a = Http.sendRequest("https://api.roblox.com/groups/" + str(groupid) + "allies")
        return a

    # GET /groups/{groupId}/enemies
    # Returns Table/Array with each enemy's attributes
    def getGroupEnemies(groupid):
        a = Http.sendRequest("https://api.roblox.com/groups/" + str(groupid) + "enemies")
        return a
