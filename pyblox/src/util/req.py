#
#  util -> req.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

import requests
import json
import browser_cookie3
from .strings import Strings

cookies = list(browser_cookie3.chrome())

class Req:

	def getAllCookies():
		#return cookies
		session = requests.Session()
		response = session.get("https://www.roblox.com/home")
		print(session.cookies.get_dict())


	'''
	@method 
		request(t=String,url=String,*args,**kwargs)

	@params 
		t = Type of Request(GET or POST)
		url = URL

	@optionals 

		payload = Dictionary Payload
		header = Request Headers
		cookies = cookie

	@result 
		Returns request response wholesale as a tuple

	@example 1:

		# GET Request
		response = Req.request(t="GET",url="http://httpbin.org/get")

		# You can get the status of the request by doing:
		response[0]

		# And so on... its a tuple so this also works as a shorthand:
		response = Req.request(t="GET",url="http://httpbin.org/get")[0]


	@example 2:

		# POST Request
		data = {"Username":"JohnDoe","Password":"JaneDoe"}

		# Data you want to send as a payload
		response = Req.request(t="POST",url="http//httpbin.org/post",payload=data)

		# Again, all data is returned wholesale as a tuple so this works:
		response[0] # Gets you the status of the request

		# Once again, this works as a shorthand:
		response = Req.request(t="POST",url"http://httpbin.org/post",payload=data)[0]
	'''
	def request(t=str,url=str,*args,**kwargs):
		payload = kwargs.get('payload',None)
		header = kwargs.get('header',None)
		cookies = kwargs.get('cookies',None)
		
		if t == "GET" and url:
			request = requests.get(str(url))
			statusCode = request.status_code
			content = request.content
			headers = request.headers
			encoding = request.encoding
			json = request.json()
			return statusCode,content,headers,encoding,json

		elif t == "POST" and url and payload:
			request = None
			if header and not cookies:
				request = requests.post(str(url),data=payload,headers=header)
			elif not header and not cookies:
				request = requests.post(str(url),data=payload)
			elif header and cookies:
				request = requests.post(str(url),data=payload,headers=header,cookies=cookies)

			statusCode = request.status_code
			content = request.content
			headers = request.headers
			encoding = request.encoding
			json = request.json()
			return statusCode,content,headers,encoding,json

		elif t == "BLANK_POST":
			request = requests.post(str(url),headers=header)
			statusCode = request.status_code
			content = request.content
			headers = request.headers
			encoding = request.encoding
			json = request.json()
			return statusCode,content,headers,encoding,json

		elif t == "DOUBLE_POST":
			pass

		elif t == "PATCH" and url and payload:
			request = requests.patch(str(url),data=payload)
			statusCode = request.status_code
			content = request.content
			headers = request.headers
			encoding = request.encoding
			json = request.json()
			return statusCode,content,headers,encoding,json


		#request2 = requests.post('https://groups.roblox.com/v1/groups/4658962/wall/posts',data={"body":"Final2"},headers=cache2,cookies=cookies)