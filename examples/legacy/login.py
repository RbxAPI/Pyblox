#
#  examples -> login.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from pyblox3 import *
import asyncio


'''
A basic example of how to login via Pyblox. Yes, it finally supports async/await protocol. : )
This is what your 'config.json' should look like inside.

{
	"ctype": "username",
	"cvalue": "yourusername",
	"password": "yourpassword",
	".ROBLOSECURITY": "Full Cookie found in F12->Application->Left Menu Cookies tab->click the http://www.roblox.com->.ROBLOSECURITY row where it says, "Value" "
}
'''


# Generic Event Loop, put all code inside this method
async def event_loop():
	await Auth_v2.client(file="config.json") # Config file in the same directory as this file
	await Groups_v1.Wall.post(groupid=4658962,body="Async Test 1") # Post's "Async Test 1" to your group's wall

loop = asyncio.get_event_loop() # Get the event loop
loop.run_until_complete(event_loop()) # Bind the your event loop to the main one
loop.close() # Close process when task is finished
