#
#  http.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#
import logging
import requests


class Http:

    # GET Request
    # Params: "url" // target url
    def sendRequest(url):
        payload = requests.get(str(url))
        statusCode = payload.status_code
        content = payload.content
        if statusCode is not 200:
            return logging.error(f"[Pyblox][GET] Something went wrong. Error: {statusCode}")
        return content

    # POST Request
    # Params: "url" // target url, payload // {JSON key-value pairs}
    def postRequest(url, payload):
        payload = requests.post(str(url), data=payload)
        statusCode = payload.status_code
        content = payload.content
        if statusCode is not 200:
            return logging.error(f"[Pyblox][POST] Something went wrong. Error: {statusCode}")
        return content
