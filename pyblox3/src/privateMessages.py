#
#  privateMessages.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2021- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class privateMessages_v1:

    def __init__(self,**kwargs):
        auth = kwargs.get("auth", None)
        self.auth = auth.auth_cookies
        self.Announcements = self.Users(self)
        self.Messages = self.userSearch(self)
    
    class Announcements:
        def __init__(self, privateMessages_v1):
            self.privateMessages_v1 = privateMessages_v1
            self.auth = privateMessages_v1.auth
        
        # GET : "https://privatemessage.roblox.com/v1/announcements"
        # Docs : https://privatemessages.roblox.com/docs#!/Announcements/get_v1_announcements
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/announcements', cookies=auth)
            return response[4]
        
        # GET : "https://privatemessage.roblox.com/v1/metadata"
        # Docs : https://privatemessages.roblox.com/docs#!/Announcements/get_v1_announcements_metadata
        async def metadata(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/metadata', cookies=auth)
            return response[4]

    class Messages:

        def __init__(self, privateMessages_v1):
            self.privateMessages_v1 = privateMessages_v1
            self.auth = privateMessages_v1.auth
        
        # GET : "https://privatemessage.roblox.com/v1/messages"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/get_v1_messages
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/messages', cookies=auth)
            return response[4]
        
        # GET : "https://privatemessage.roblox.com/v1/messages/{messageId}"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/get_v1_messages_messageId
        async def getByMessageId(self, **kwargs):
            auth = self.auth
            messageId = kwargs.get("messageId", None)
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/messages/{messageId}', cookies=auth)
            return response[4]
        
        # GET : "https://privatemessage.roblox.com/v1/messages/{userId}/can-message"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/get_v1_messages_userId_can_message
        async def getByUserId(self, **kwargs):
            auth = self.auth
            userId = kwargs.get("userId", None)
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/messages/{userId}/can-message', cookies=auth)
            return response[4]
        
        # GET : "https://privatemessage.roblox.com/v1/messages/unread/count"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/get_v1_messages_unread_count
        async def getUnreadCount(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://privatemessage.roblox.com/v1/messages/unread/count', cookies=auth)
            return response[4]
        
        # POST : "https://privatemessage.roblox.com/v1/messages/archive"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/post_v1_messages_archive
        async def archive(self, **kwargs):
            auth = self.auth
            request = kwargs.get("batchMessagesRequest", None)
            response = await Req.request(t="POST", url=f'https://privatemessage.roblox.com/v1/messages/archive', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]
        
        # POST : "https://privatemessage.roblox.com/v1/messages/mark-read"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/post_v1_messages_mark_read
        async def markRead(self, **kwargs):
            auth = self.auth
            request = kwargs.get("batchMessagesRequest", None)
            response = await Req.request(t="POST", url=f'https://privatemessage.roblox.com/v1/messages/mark-read', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]
        
        # POST : "https://privatemessage.roblox.com/v1/messages/mark-unread"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/post_v1_messages_mark_unread
        async def markUnread(self, **kwargs):
            auth = self.auth
            request = kwargs.get("batchMessagesRequest", None)
            response = await Req.request(t="POST", url=f'https://privatemessage.roblox.com/v1/messages/mark-unread', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]
        
        # POST : "https://privatemessage.roblox.com/v1/messages/send"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/post_v1_messages_send
        async def send(self, **kwargs):
            auth = self.auth
            request = kwargs.get("sendMessagesRequest", None)
            response = await Req.request(t="POST", url=f'https://privatemessage.roblox.com/v1/messages/send', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]
        
        # POST : "https://privatemessage.roblox.com/v1/messages/unarchive"
        # Docs : https://privatemessages.roblox.com/docs#!/Messages/post_v1_messages_unarchive
        async def send(self, **kwargs):
            auth = self.auth
            request = kwargs.get("batchMessagesRequest", None)
            response = await Req.request(t="POST", url=f'https://privatemessage.roblox.com/v1/messages/unarchive', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]