#
# ABTests.py
# pyblox
#
# By NSG (Nikita Petko) and IvanG (Ivan Gregrovnich)
# Copyright © 2015-2020 MFD. All rights reserved.
#

from pyblox3 import AbTesting_v1, Auth_v2
import json
import asyncio

user = Auth_v2(cookies={".ROBLOSECURITY": "Token"})
abtestapi = AbTesting_v1(auth=user)

# The SubjectTargetId when using SubjectType "User" is required to match the UserId of the cookie you supplied.
# And if a SINGLE Id doesn't match your UserId, it will throw a 403

browserTrackerABTests = [
    abtestapi.createGetEnrollmentType(ExperimentName="SomeABTestExperiment", SubjectType=2, SubjectTargetId=1234),
    # 2 represents BrowserTracker and is the same as below:
    abtestapi.createGetEnrollmentType(ExperimentName="SomeABTestExperiment",
                                      SubjectType="BrowserTracker",
                                      SubjectTargetId=1234),
]
userABTests = [
    abtestapi.createGetEnrollmentType(ExperimentName="SomeUserABTestExperiment", SubjectType=1, SubjectTargetId=1234),
    # 1 represents User and is the same as below:
    abtestapi.createGetEnrollmentType(ExperimentName="SomeABTestExperiment",
                                      SubjectType="User",
                                      SubjectTargetId=1234),
]


async def event_loop():
    browserTrackerResponse = await abtestapi.getEnrollments(request=json.dumps(browserTrackerABTests))
    userResponse = await abtestapi.getEnrollments(request=json.dumps(userABTests))
    print(browserTrackerResponse, userResponse)


loop = asyncio.get_event_loop()  # Get the event loop
loop.run_until_complete(event_loop())  # Bind the your event loop to the main one
