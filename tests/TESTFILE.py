#
#  TESTFILE.py
#  pyblox
#
#  By sbhadr (Sanjay Bhadra)
#  Copyright © 2024- sbhadr (Sanjay Bhadra). All rights reserved.
#
# This file does can be deleted w/o any issues to source.
# 

import asyncio
from src import Auth_v2, Groups_v1

test_data = {
  "isApprovalRequired": False,
  "isBuildersClubRequired": False,
  "areEnemiesAllowed": False,
  "areGroupFundsVisible": True,
  "areGroupGamesVisible": True
}

# Instance your auth details
base_bot_user = Auth_v2(cookies={'.ROBLOSECURITY': "YourCookie"})
# Instance your group as a variable
base_group = Groups_v1(groupid=7,auth=base_bot_user)

# Standard Event Loop
async def event_loop():
    group_info = await base_group.Membership.get()
    print(group_info)

# Async stuff, woohoo
loop = asyncio.get_event_loop()
loop.run_until_complete(event_loop())
loop.close()

