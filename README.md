# Pyblox

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()
[![ROBLOX API Discord](https://img.shields.io/badge/discord-roblox%20api%20chat-blue.svg)](https://discord.gg/EDXNdAT)
[![Downloads](http://pepy.tech/badge/pyblox3)](http://pepy.tech/project/pyblox3)

An API wrapper for Roblox written in Python.

The purpose of this API wrapper is to expose Roblox's API for third party use and/or for individual standalone projects.
This is the first stable Python API wrapper for the Roblox API. Documentation can be found within each module. I encourage
developers to look into the codebase to better understand this wrapper and what it can truly offer. 

If you would like to contribute, create a pull request with the changes you made. If you have a complaint, issue or problem, create an issue and I will try to answer as fast as I can. 

For users wanting a Python 2x-compatible version: https://github.com/RbxAPI/Pyblox/tree/python2

For users wanting a mid-stable, asynchronous-version: https://github.com/RbxAPI/Pyblox/tree/nightly_build
### Updating

The Roblox API updates whenever necessary and often the developers don't specify when or why these changes are taking place.
Due to this, this repo could break at anytime. If a break does occur, please open up an issue on this repo detailing the error.

``Master`` - This branch is at version ``2.4.4`` . Those with ``2.4.1`` may update to this branch without breaking changes. Addresses critical issues and is maintained. Will be uploaded to pip sometime soon.

``nightly_build`` - Starts at version ``3.x.x`` . Those with ``2.4.1`` or ``2.4.2`` may update to this branch with breaking changes. Features a more organized and powerful version of Pyblox that predicates itself on OOP (Object Orientated Programming) and async (non-blocking method calls / instances). Working towards 100% API coverage and will be marked as master once 80% coverage is completed. Will be uploaded to pip sometime soon.

## Installing
There's now two ways to install Pyblox. 
You may now do it through pip: 
``pip install pyblox3``
or do it manually below:
```
1. Download or Clone this repo
2. Place the "pyblox" folder into C:\Users\YOURUSERNAMEONWINDOWSMACHINE\AppData\Local\Programs\Python\Python35-32\Lib\site-packages
```
MacOS and Linux are supported but installation will vary.
This was developed on a windows-based machine and thus, it's recommended to use windows.

Please note that the "Clone" method is regulary updated. However, the pip-version is often behind.

## Quick Example

```py
from pyblox3 import Friends # Imports the Friends class from pyblox wrapper 

def GetAllFriends():
	CoolPeople = Friends.friendList(1) # Takes your userid
	print(CoolPeople) # Returns usernames and prints them in the console

GetAllFriends() # Calls "GetAllFriends" method
```

## Requirements

- Python 3+
- ``pip install requests``

*note: requests may have been already installed.*

## Related Projects
*https://github.com/iranathan/robloxapi*

*https://github.com/NoahCristino/robloxlib*

*https://github.com/sentanos/roblox-js*

*https://github.com/MartinRBX/bloxy*

*https://github.com/suufi/noblox.js*

*https://github.com/gamenew09/RobloxAPI*

*https://github.com/RbxAPI/Javablox*

*https://github.com/PizzaCrust/Roblox4j*

*https://github.com/PizzaCrust/KotlinRoblox*

*https://github.com/FreeLineTM/roblox.kt*

*https://github.com/NevermoreFramework/Nevermore*

*https://github.com/Meqolo/cblox*

*https://github.com/CrescentCode/RobloxCommunication*

*https://github.com/OliverHensworth/roblox.lua/*

*https://github.com/OliverHensworth/roblox.rb*
