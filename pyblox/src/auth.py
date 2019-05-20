#
#  auth.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json
import requests

root = "https://auth.roblox.com"

class Auth_v2:

	def getPrimaryCookie(**kwargs):
		token = kwargs.get("token",None)
		response = Req.request(t="BLANK_POST",url="https://www.roblox.com/authentication/signoutfromallsessionsandreauthenticate",headers=Cached.cache)
		Cached.cache["X-CSRF-TOKEN"] = response[2]["X-CSRF-TOKEN"]
		Cached.cache["Cookie"] = response[2]["set-cookie"]
		return Cached.cache["Cookie"]




	async def getToken(**kwargs):
		data = kwargs.get("data",None)
		#cookie = kwargs.get("cookie",None)
		try:
			#if cookie:
				#cache["Cookie"] = ".ROBLOSECURITY={}".format(cookie)
			return Cached.cache["X-CSRF-TOKEN"]
		except KeyError:
			response = await Req.request(t="POST",url="https://api.roblox.com/sign-out/v1",payload=data)
			Cached.auth[0] = data
			Cached.cache["X-CSRF-TOKEN"] = response[2]["X-CSRF-TOKEN"]
			return response[2]["X-CSRF-TOKEN"]

	def getCache():
		return Cached.cache

	def getCookie():
		tok = Auth_v2.getToken(data=Cached.auth[0])
		return Auth_v2.getPrimaryCookie(token=tok)


	async def login(**kwargs):
		cookie = kwargs.get("cookie",None)
		token = kwargs.get("token",None)
		request = requests.post('https://groups.roblox.com/v1/groups/4658962/wall/posts',data={"body":"Hey!"},headers=token,cookies=cookie)
		statusCode = request.status_code
		print(token)
		if statusCode == 403:
			if Cached.cache["X-CSRF-TOKEN"] == request.headers["X-CSRF-TOKEN"]:
				print("Failed to login!")
			elif Cached.cache["X-CSRF-TOKEN"] != request.headers["X-CSRF-TOKEN"]:
				Cached.cache["X-CSRF-TOKEN"] = request.headers["X-CSRF-TOKEN"]
				print("Logged in successfully!")
				print(Cached.cache)


	async def client(**kwargs):
		file = kwargs.get("file",None)
		read_data = Jsoni.read(file=file)
		Cached.file_cache = read_data
		await Auth_v2.getToken(data={"ctype": read_data["ctype"],"cvalue": read_data["cvalue"], "password": read_data["password"]})
		await Auth_v2.login(cookie={'.ROBLOSECURITY': read_data[".ROBLOSECURITY"]},token=Cached.cache)


		


