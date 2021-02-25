<p align="center">
  <img width="40%" height="30%" src="https://cdn.discordapp.com/attachments/803768815400779776/803768832236847155/image.png">
</p>

<div align="center">
    <p>
        <a href="https://discord.gg/EDXNdAT">
            <img src="https://img.shields.io/badge/Discord-Roblox%20Api%20-blue.svg" alt="Roblox API Discord">
        </a>
        <a href="https://discord.gg/EDXNdAT">
            <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="GitHub license">
        </a>
    </p>
</div>

#

An API wrapper for Roblox written in Python.

The purpose of this API wrapper is to expose Roblox's API for third party use and/or for individual standalone projects. This is the first stable Python API wrapper for the Roblox API. Documentation can be found within each module. I encourage developers to look into the codebase to better understand this wrapper and what it can truly offer. 

This branch is incredibly unstable but will replace ``master`` once it's stable enough for full release. 
This is intended to be ``v3.x.x`` and beyond. Please be aware that there are breaking changes in design
and will not be compatible w/ any versions prior. 

If you would like to contribute, create a pull request with the changes you made. If you have a complaint, issue or problem, create an issue and I will try to answer as fast as I can.

> **Notice:** Traditional documentation does not exist due to the fact that developers should know what the code does and why it could benefit your project. Please take a look at the library's files for references. In almost all cases, you'll find that the class names match up with the documentation found in the following format: https://APINAME.roblox.com/#docs

# Requirements

- Python 3.6+ / 3.6-dev+ or PyPy3
- aiohttp
- asyncio
- requests_async
- pytest

> **Notice:** Requirements should be installed automatically via pip.

# Feature Addition
- Supports an unlimited amount of users
- Supports an unlimited amount of groups
- Supports authentication by cookie
- Supports wide coverage of the API
- Follows the official documentation that Roblox provides
- Handles token-managment for you

> **Notice:** This does not cover all that Pyblox has to offer just a subset.

# Compatibility
- Async Compatible (default)
- Supports MacOS, Windows, Linux, Raspbian
- Should be able to work on PyPy3
- Will not work on Python 2.x.x or any version below Python 3.6
- Works with Discord.py & other Python-based discord libraries
- Only works via cookie login; does not support username and password authentication

> **Disclaimer:** When using any of the authentication features, please do not risk your account. Instead, use an alt or a secondary account to protect your main account and assets that belong to it.
