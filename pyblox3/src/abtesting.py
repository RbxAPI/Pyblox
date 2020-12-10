#
# abtesting.py
# pyblox
#
# By Sanjay-B(Sanjay Bhadra)
# Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#


# Info for sanjay, v1/enrollments is v1/get-enrollments, but the only difference is, is that SubjectType is a string
# not an integer, but v1/enrollments can take an integer for SubjectType, as you can tell, this has enforced suffering
# upon me. Also v1/get-enrollments can take strings for SubjectType, I believe 2 different engineers worked on these
# endpoints, therefore they do the exact same thing, ABTestService didn't exist until 2018, so I can't see internal
# code for it, my head hurts.

# TODO Consider removing my existence
# FIXME The awful code below.

from .util import *

root = "https://abtesting.roblox.com"


# TODO Make this less verbose and use kwargs
def createGetEnrollmentType(ExperimentName: str, SubjectType: str or int, SubjectTargetId: int) -> dict:
    """
    OK, SubjectType can only be 2, 1 throws a 403 (I assume it requires some authorization)
    -> when looking into it more, it appears that nsg has no clue what SubjectType 1 means and/or how to use it ;)
    -> OK nsg, you definitely didn't look into it more, SubjectType 1 is user, and requires a valid userId,
        basically the one of the currently authenticated user:
        1 is User
    """
    if len(ExperimentName) == 0:
        raise SyntaxError("The ExperimentName shouldn't be empty.")
    if len(ExperimentName) > 50:
        raise SyntaxError("The ExperimentName shouldn't be longer than 50 characters.")
    if SubjectTargetId < 1:
        raise SyntaxError("In order to satisfy the request, the SubjectTargetId is required to be greater than 0.")
    if (type(SubjectType) == int and SubjectType > 2) \
            or (type(SubjectType) == int and SubjectType < 1) \
            or (type(SubjectType) == str and len(SubjectType) == 0):
        raise SyntaxError("In order to satisfy the request, the SubjectType is required to 1 or 2 "
                          "or User or BrowserTracker")
    return {'ExperimentName': ExperimentName, 'SubjectType': SubjectType, 'SubjectTargetId': SubjectTargetId}


class AbTesting_v1:

    def __init__(self, **kwargs):
        groupid = kwargs.get("groupid", None)
        auth = kwargs.get("auth", None)
        self.groupid = groupid
        self.auth = auth.auth_cookies

    # POST https://abtesting.roblox.com/v1/get-enrollments
    async def getEnrollments(self,
                             **kwargs):
        """
        OK, it should consist of an array of these:
        {
            "ExperimentName": "SomeABTest",
            "SubjectType": int,
            "SubjectTargetId": int64,
        }
        you should use createGetEnrollmentType as a helper
        """
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
            raise RuntimeError("You are unauthorised to create this request with the credentials you supplied!")
        else:
            raise RuntimeError(f'{response[0]} {response[4]["message"]}')
