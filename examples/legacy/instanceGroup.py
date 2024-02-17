import asyncio
from pyblox3 import Groups_v1

# Instance your group as a variable
base_group = Groups_v1(groupid="GROUPID")


# Standard Event Loop
async def event_loop():
    group_info = await base_group.Membership.get() # Uses the id specified in Base_Group
    print(group_info) # Prints group info to console

# Async stuff, woohoo
loop = asyncio.get_event_loop()
loop.run_until_complete(event_loop())
loop.close()