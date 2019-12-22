#
#  assets.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json

# Asset Object
class Asset:
    Name = None
    Id = None
    ProductId = None
    Description = None
    AssetTypeId = None
    CreatorName = None
    CreatorId = None
    CreatorTargetId = None
    IconImageAssetId = None
    Created = None
    Updated = None
    PriceInRobux = None
    Sales = None
    IsNew = None
    IsForSale = None
    IsPublicDomain = None
    IsLimited = None
    IsLimitedUnique = None
    Remaining = None
    MinimumMembershipLevel = None
    ContentRatingTypeId = None
    
    def __init__(self,data):
        self.Name = data["Name"]
        self.Id = data["AssetId"]
        self.ProductId = data["ProductId"]
        self.Description = data["Description"]
        self.AssetTypeId = data["AssetTypeId"]
        self.CreatorName = data["Creator"]["Name"]
        self.CreatorId = data["Creator"]["Id"]
        self.CreatorType = data["Creator"]["CreatorType"]
        self.CreatorTargetId = data["Creator"]["CreatorTargetId"]
        self.IconImageAssetId = data["IconImageAssetId"]
        self.Created = data["Created"]
        self.Updated = data["Updated"]
        self.PriceInRobux = data["PriceInRobux"]
        self.Sales = data["Sales"]
        self.IsNew = data["IsNew"]
        self.IsForSale = data["IsForSale"]
        self.IsPublicDomain = data["IsPublicDomain"]
        self.IsLimited = data["IsLimited"]
        self.IsLimitedUnique = data["IsLimitedUnique"]
        self.Remaining = data["Remaining"]
        self.MinimumMembershipLevel = data["MinimumMembershipLevel"]
        self.ContentRatingTypeId = data["ContentRatingTypeId"]

class Assets:

    def PackageAsset(assetid):
        a = Http.sendRequest("https://www.roblox.com/Game/GetAssetIdsForPackageId?packageId=" + str(assetid))
        result = []
        for part in a:
            i = a.index(part)
            b = part
            link = "https://www.roblox.com/library/" + str(b)
            result.insert(i, link)
        return result

    # GET https://api.roblox.com/Ownership/HasAsset?userId={userId}&assetId={assetId}
    # Returns Boolean
    def hasAsset(userid, assetid):
        a = Http.sendRequest("https://api.roblox.com/Ownership/HasAsset?userId=" + str(userid) + "&assetId=" + str(assetid))
        if a == "true" or True:
            return True
        else:
            return False

    # GET https://api.roblox.com/Marketplace/ProductInfo?assetId={assetId}
    # Returns Table/Array + Attributes
    def Asset(assetid):
        c = Http.sendRequest("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(assetid))
        b = c.decode("utf-8")
        a = json.loads(b)
        return Asset(a)

    # GET https://www.roblox.com/studio/plugins/info?assetId={assetId}
    # Returns Table/Array
    def AssetVersions(assetid):
        a = Http.sendRequest("https://www.roblox.com/studio/plugins/info?assetId=" + str(assetid))
        result = []
        for part in a:
            i = a.index(part)
            b = part
            result.insert(i, part)
        return result
