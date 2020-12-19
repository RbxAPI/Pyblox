#
# abtesting.py
# pyblox
#
# By NSG (Nikita Petko) and IvanG (Ivan Gregrovnich) with Sanjay-B(Sanjay Bhadra)
# Copyright © 2019- Sanjay-B with MFD. All rights reserved.
#

from .util import *

root = "https://abtesting.roblox.com"


class AbTesting_v1:

    def __init__(self, **kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies

    # POST : https://abtesting.roblox.com/v1/get-enrollments
    # Docs : n/a
    async def getEnrollments(self,
                             **kwargs):
        global root
        auth = self.auth
        request = kwargs.get('request')
        response = await Req.request(t='POST',
                                     url=root+'/v1/get-enrollments',
                                     cookies=auth,
                                     payload=request,
                                     header={'Content-Type': 'application/json'})
        if response[0] == 200:
            return response[4]['data']
        elif response[0] == 403:
            return False, "You are unauthorised to create this request with the credentials you supplied!"
        else:
            return False, response[4]

    @staticmethod
    def createGetEnrollmentType(**kwargs):
        ExperimentName = kwargs.get("ExperimentName", None)
        SubjectType = kwargs.get("SubjectType", None)
        SubjectTargetId = kwargs.get("SubjectTargetId", None)
        if len(ExperimentName) == 0 or len(ExperimentName) > 50:
            raise SyntaxError("The ExperimentName should not be empty or greater than 50 characters.")
        if SubjectTargetId < 1:
            raise SyntaxError("In order to satisfy the request, the SubjectTargetId is required to be greater than 0.")
        if (type(SubjectType) == int and SubjectType > 2) \
                or (type(SubjectType) == int and SubjectType < 1) \
                or (type(SubjectType) == str and len(SubjectType) == 0):
            raise SyntaxError("In order to satisfy the request, the SubjectType is required to 1 or 2 "
                              "or User or BrowserTracker")
        return {'ExperimentName': ExperimentName, 'SubjectType': SubjectType, 'SubjectTargetId': SubjectTargetId}
