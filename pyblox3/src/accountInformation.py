#
# accountInformation.py
# pyblox
#
# By Sanjay-B(Sanjay Bhadra)
# Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class accountInformation_v1:

    def __init__(self,**kwargs):
        auth = kwargs.get("auth")
        self.auth = auth.auth_cookies
        self.Metadata = self.Metadata(self)
        self.phoneInformation = self.phoneInformation(self)
        self.promotionChannel = self.promotionChannel(self)
        self.starCodeAffiliate = self.starCodeAffiliate(self)
        self.robloxBadges = self.robloxBadges(self)
        self.emailInformation = self.emailInformation(self)
    
    # GET : https://accountinformation.roblox.com/v1/birthdate
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/get_v1_birthdate
    async def getBirthdate(self):
        auth = self.auth
        response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/birthdate', cookies=auth)
        return response[4]

    # POST : https://accountinformation.roblox.com/v1/birthdate
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/post_v1_birthdate
    async def updateBirthdate(self,**kwargs):
        auth = self.auth
        request = kwargs.get("request", None)
        response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/birthdate', payload=request, cookies=auth)
        if response[0] == 200:
            return True
        return False, response[4]

    # GET : https://accountinformation.roblox.com/v1/description
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/get_v1_description
    async def getDescription(self):
        auth = self.auth
        response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/description', cookies=auth)
        return response[4]

    # POST : https://accountinformation.roblox.com/v1/description
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/post_v1_description
    async def updateDescription(self,**kwargs):
        auth = self.auth
        request = kwargs.get("request", None)
        response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/description', payload=request, cookies=auth)
        if response[0] == 200:
            return True
        return False, response[4]

    # GET : https://accountinformation.roblox.com/v1/gender
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/get_v1_gender
    async def getGender(self):
        auth = self.auth
        response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/gender', cookies=auth)
        return response[4]


    # POST : https://accountinformation.roblox.com/v1/gender
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/post_v1_gender
    async def updateGender(self,**kwargs):
        auth = self.auth
        request = kwargs.get("request", None)
        response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/gender', payload=request, cookies=auth)
        if response[0] == 200:
            return True
        return False, response[4]

    # GET : https://accountinformation.roblox.com/v1/xbox-live/consecutive-login-days
    # Docs : https://accountinformation.roblox.com/docs#!/AccountInformation/get_v1_xbox_live_consecutive_login_days
    async def getConsecutiveXboxDays(self):
        auth = self.auth
        response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/xbox-live/consecutive-login-days', cookies=auth)
        return response[4]
    
    
    class Metadata:

        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth

        # GET : https://accountinformation.roblox.com/v1/metadata
        # Docs : https://accountinformation.roblox.com/docs#!/Metadata/get_v1_metadata
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/metadata', cookies=auth)
            return response[4]
    

    class phoneInformation:

        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth
        
        # GET : https://accountinformation.roblox.com/v1/phone
        # Docs : https://accountinformation.roblox.com/docs#!/PhoneInformation/get_v1_phone
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/phone', cookies=auth)
            response[4]

        # POST : https://accountinformation.roblox.com/v1/phone
        # Docs : https://accountinformation.roblox.com/docs#!/PhoneInformation/post_v1_phone
        async def update(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/phone', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]

        # POST : https://accountinformation.roblox.com/v1/phone/delete
        # Docs : https://accountinformation.roblox.com/docs#!/PhoneInformation/post_v1_phone_delete
        async def delete(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/phone/delete', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]

        # POST : https://accountinformation.roblox.com/v1/phone/resend
        # Docs : https://accountinformation.roblox.com/docs#!/PhoneInformation/post_v1_phone_resend
        async def resend(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/phone/resend', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]


        # POST : https://accountinformation.roblox.com/v1/verify
        # Docs : https://accountinformation.roblox.com/docs#!/PhoneInformation/post_v1_phone_verify
        async def verify(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/phone/verify', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]


    class promotionChannel:

        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth
        
        # GET : https://accountinformation.roblox.com/v1/promotion-channels
        # Docs : https://accountinformation.roblox.com/docs#!/PromotionChannel/get_v1_promotion_channels
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/promotion-channels', cookies=auth)
            response[4]


        # POST : https://accountinformation.roblox.com/v1/promotion-channels
        # Docs : https://accountinformation.roblox.com/docs#!/PromotionChannel/post_v1_promotion_channels
        async def update(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/promotion-channels', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]

        # GET : https://accountinformation.roblox.com/v1/users/{userid}/promotion-channels
        # Docs : https://accountinformation.roblox.com/docs#!/PromotionChannel/get_v1_users_userId_promotion_channels
        async def getFromUser(self,**kwargs):
            auth = self.auth
            userid = kwargs.get("userid", None)
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/user/{userid}/promotion-channels', cookies=auth)
            response[4]

    class starCodeAffiliate:

        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth

        # DELETE : https://accountinformation.roblox.com/v1/star-code-affiliates
        # Docs : https://accountinformation.roblox.com/docs#!/StarCodeAffiliate/delete_v1_star_code_affiliates
        async def remove(self,**kwargs):
            auth = self.auth
            response = await Req.request(t="DEL", url=f'https://accountinformation.roblox.com/v1/star-code-affiliates', cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]

        # GET : https://accountinformation.roblox.com/v1/star-code-affiliates
        # Docs : https://accountinformation.roblox.com/docs#!/StarCodeAffiliate/get_v1_star_code_affiliates
        async def get(self):
            auth = self.auth
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/star-code-affiliates', cookies=auth)
            response[4]

        # POST : https://accountinformation.roblox.com/v1/star-code-affiliates
        # Docs : https://accountinformation.roblox.com/docs#!/StarCodeAffiliate/post_v1_star_code_affiliates
        async def add(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/star-code-affiliates', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]
    

    class robloxBadges:
        
        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth
        
        # GET : https://accountinformation.roblox.com/v1/users/{userid}/roblox-badges
        # Docs : https://accountinformation.roblox.com/docs#!/RobloxBadges/get_v1_users_userId_roblox_badges
        async def getFromUser(self,**kwargs):
            auth = self.auth
            userid = kwargs.get("userid", None)
            response = await Req.request(t="GET", url=f'https://accountinformation.roblox.com/v1/user/{userid}/roblox-badges', cookies=auth)
            response[4]
    

    class emailInformation:
        
        def __init__(self,accountInformation_v1):
            self.accountInformation_v1 = accountInformation_v1
            self.auth = accountInformation_v1.auth
        
        # POST : https://accountinformation.roblox.com/v1/email/verify
        # Docs : https://accountinformation.roblox.com/docs#!/EmailInformation/post_v1_email_verify
        async def verify(self,**kwargs):
            auth = self.auth
            request = kwargs.get("request", None)
            response = await Req.request(t="POST", url=f'https://accountinformation.roblox.com/v1/email/verify', payload=request, cookies=auth)
            if response[0] == 200:
                return True
            return False, response[4]