#
# abtesting.py
# pyblox
#
# By Sanjay-B(Sanjay Bhadra)
# Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *


class AbTesting_v1:

    def __init__(self, **kwargs):
        groupid = kwargs.get("groupid", None)
        auth = kwargs.get("auth", None)
        self.groupid = groupid
        self.auth = auth.auth_cookies

    # POST https://abtesting.roblox.com/v1/get-enrollments
    async def getEnrollments(self,
                             **kwargs):
        auth = self.auth
        request = kwargs.get('request')
        response = await Req.request(t='POST',
                                     url='https://abtesting.roblox.com/v1/get-enrollments',
                                     auth=auth,
                                     payload=request)
        if response[0] == 200:
            return response[4]
        else:
            raise RuntimeError(response[4]['message'])
