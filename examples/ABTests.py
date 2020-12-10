#
#  ABTests.py
#  pyblox
#
#  By nsg-mfd(Nikita Pedko)
#  Copyright © 2020- Sanjay-B(Sanjay Bhadra) with MFD 2015-2020. All rights reserved.
#

from pyblox3 import AbTesting_v1, Auth_v2, createGetEnrollmentType
import json
import asyncio

user = Auth_v2(cookies={".ROBLOSECURITY": "Full Cookie found in F12->Application->Left Menu Cookies tab->click the "
                                          "http://www.roblox.com->.ROBLOSECURITY row where it says, \"Value\" "})
abtestapi = AbTesting_v1(auth=user)

abtests = [
    createGetEnrollmentType("SomeABTestExperiment", 2, 1345),  # 2 represents BrowserTracker
    createGetEnrollmentType("SomeABTestExperiment", "BrowserTracker", 1345)
]


async def event_loop():
    response = await abtestapi.getEnrollments(request=json.dumps(abtests))
    print(response)

loop = asyncio.get_event_loop()  # Get the event loop
loop.run_until_complete(event_loop())  # Bind the your event loop to the main one
