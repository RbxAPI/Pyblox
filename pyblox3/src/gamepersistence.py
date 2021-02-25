#
# gamepersistence.py
# pyblox
#
# By NSG (Nikita Petko) with Sanjay-B(Sanjay Bhadra)
# Copyright 2019-2021 Sanjay-B, All rights reserved.
# Copyright 2011-2021 Nikita Petko, All rights reserved.
# Copyright 2003-2021 ROBLOX Corporation, All Rights Reserved.
# Copyright 2002-2021 MFD Corporation, All Rights Reserved.
#

# rootFile C:\buildAgent\work\671a0da0ba061c9\Python\Pyblox\pyblox3\src\gamepersistence.py

from .util import *

g_ACC_NO_PROD = True;

root = "https://gamepersistence.roblox.com" if not g_ACC_NO_PROD else "https://gamepersistence.sitetest4.robloxlabs.com"
rootapi = "https://gamepersistence.api.sitetest4.robloxlabs.com"
apiKey = "90F4CB19-A650-45C0-82E6-F2EC82BA0050"

class GamePersistence_NoOpt:
    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.placeId = kwargs.get("placeId", None)
        self.auth = auth.auth_cookies

    # POST https://gamepersistence.roblox.com/persistence/getV2
    # Docs: n/a
    async def GetAsync(self, **kwargs):
        global root
        auth = self.auth
        placeId = self.placeId
        dataStoreName = kwargs.get("name")
        scopeName = kwargs.get("scope", "global")
        keyName = kwargs.get("key");
        isOrderedDatastore = kwargs.get("isSorted", False)
        response = await Req.request(t='POST',
                                     url=root+f'/persistence/getV2?type={"sorted" if isOrderedDatastore else "standard"}',
                                     cookies=auth,
                                     payload=f"qkeys[0].scope={scopeName}&qkeys[0].target={keyName}&qkeys[0].key={dataStoreName}",
                                     header={'Content-Type': 'application/x-www-form-urlencoded', 'Roblox-Place-Id': str(placeId)})
        
        """
        Expected format for responses that have keys:
        {
            "data": [
                {
                    "Key": {
                        "Scope": "SCOPE_NAME",
                        "Target": "KEY_NAME",
                        "Key": "DATA_STORE_NAME",
                    },
                    "Value": "VALUE"
                }
            ]
        }
        ###

        Expected format for responses that have no keys:
        {
            "data": []
        }
        """
        if response[0] == 200:
            if response[4]["data"] and len(response[4]["data"]) > 0:
                return response[4]["data"][1]["Value"] or None;
            else:
                return None;
        elif response[0] == 403:
            return False, "You do not have access to do that"
        else:
            return False, response[4];

# Deprecate this soon, v0 endpoints are being removed when DataStoreV2 is released for BetaTesters, currently only available for SoothSayer anyway
# - Jack Puickeikzi Daniels (Core Game Engine Systems Engineer - ROBLOX)
class GamePersistence_v0:
    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies

class GamePersistence_v1:
    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies

class GamePersistence_v2:
    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies