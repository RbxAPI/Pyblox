#
# abtesting.py
# pyblox
#
# By Sanjay-B(Sanjay Bhadra)
# Copyright © 2019- Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .util import *
import json

class AbTesting_v1:

    def __init__(self,**kwargs):
        groupid = kwargs.get("groupid", None)
        auth = kwargs.get("auth", None)
        self.groupid = groupid
        self.auth = auth.auth_cookies
    
    def __str__(self):
        return "AbTesting_v1 class doesn't have any endpoints"