#
#  util -> req.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

import httpx

class HttpError(Exception):
	"""
	Base class that represents an HTTP Error in the form of an exception.
	"""
	def __init__(self, kind="Generic", message="Generic Error", url="Somewhere"):
		"""
		Creates an exception with specified message.
		If not message is provided, it defaults to "Generic Error".

		@param kind: str. Represents the the kind of exception.
		@param message: str. Represents the error message of the exception.
		@param url: str. Represents the url the error occured at.
		"""
		self.kind = kind
		self.message = message
		self.url = url
		super().__init__(self.message)


class Req:
	"""
	Base class that holds HTTP request and response mechanisms.
	"""

	async def request(self, t: str, url: str, payload=None, header={}, cookies={}):
		"""
		Creates, executes and returns a request in the form of a response.
		Throws an exception if conditions are not met. 

		@param t: Str. Type of request. ie. GET, POST, PATCH, DELETE or DEL.
					   Can also be lowercase, snakecase, etc.
		@param url: Str. URL to send the request.
		@param payload: Dict or None. Represents the payload or data to send
						the request with.
		@param header: Dict. Represents the headers to send the request with.
		@param cookies: Dict. Represents the cookies to send the request with.

		@return: Tuple.
		
		@example:

		# GET Request
		response = Req.request(t="GET",url="http://httpbin.org/get")

		# You can get the status of the request by doing:
		response[0]

		# And so on... its a tuple so this also works as a shorthand:
		response = Req.request(t="GET",url="http://httpbin.org/get")[0]
		
		@example:

		# POST Request
		data = {"Username":"JohnDoe","Password":"JaneDoe"}

		# Data you want to send as a payload
		response = Req.request(t="POST",url="http//httpbin.org/post",payload=data)

		# Again, all data is returned wholesale as a tuple so this works:
		response[0] # Gets you the status of the request

		# Once again, this works as a shorthand:
		response = Req.request(t="POST",url"http://httpbin.org/post",payload=data)[0]
		"""
		async with httpx.AsyncClient(cookies=cookies) as client:

			# TODO: Backwards Compatibility (will be renamed to this later)
			kind = t.upper()
			headers = header
			
			# Obtain our initial token (fresh)
			response = await client.post(url="https://www.roblox.com/authentication/signoutfromallsessionsandreauthenticate", data=None, headers=headers)
			csrf_token = response.headers.get("X-CSRF-TOKEN")
			if not csrf_token:
				raise HttpError("POST Request", "Initial X-CSRF-TOKEN was not found in headers, aborted", url)
			
			# Perform actual request
			headers["X-CSRF-TOKEN"] = csrf_token
			if kind == "GET":
				response = await client.get(url, headers=headers)
			elif kind == "POST":
				if not cookies:
					raise HttpError("POST Request", "Endpoint requires account cookie / authentication", url)
				elif not payload:
					raise HttpError("POST Request", "Endpoint requires payload / request body", url)
				response = await client.post(url=url, data=payload, headers=headers)
			elif kind == "PATCH":
				if not cookies:
					raise HttpError("PATCH Request", "Endpoint requires account cookie / authentication", url)
				elif not payload:
					raise HttpError("PATCH Request", "Endpoint requires payload / request body", url)
				response = await client.patch(url=url, data=payload, headers=headers)
			elif kind == ("DEL" or "DELETE"):
				if not cookies:
					raise HttpError("DELETE Request", "Endpoint requires account cookie / authentication", url)
				response = await client.delete(url=url, payload=payload, headers=headers)
			return self.parse_response(response)
		
	def parse_response(self, response):
		"""
		Parses respone into expected tuple format. 

		@param response: Response. The response object from the request that has been performed.

		@return: tuple. If the status code is 200, the return is Tuple(status_code, content, headers, encoding, json).
						If the status code is not 200, the return is Tuple(status_code, content, headers, encoding, json["errors"][0]).
						Note that a status code of 200 means the request is successful. Otherwise, an error has occured.
		"""
		status_code = response.status_code
		content = response.content
		headers = response.headers
		encoding = response.encoding
		json = response.json()
		if status_code == 200:
			return status_code, content, headers, encoding, json
		return status_code, content, headers, encoding, json["errors"][0]