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

class GamePersistence_NoOpt:
    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies

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