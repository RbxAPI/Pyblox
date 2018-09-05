#
#  assets.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json


class Assets:

    def getPackageAssets(assetid):
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
        a = Http.sendRequest(
            "https://api.roblox.com/Ownership/HasAsset?userId=" + str(userid) + "&assetId=" + str(assetid))
        if a == "true" or True:
            return True
        else:
            return False

    # GET https://api.roblox.com/Marketplace/ProductInfo?assetId={assetId}
    # Returns Table/Array + Attributes
    def getAssetInfo(assetid):
        c = Http.sendRequest("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(assetid))
        b = c.decode("utf-8")
        a = json.loads(b)
        global Asset
        Asset = lambda: None
        Asset.Name = a["Name"]
        Asset.Id = a["AssetId"]
        Asset.ProductId = a["ProductId"]
        Asset.Description = a["Description"]
        Asset.AssetTypeId = a["AssetTypeId"]
        Asset.CreatorName = a["Creator"]["Name"]
        Asset.CreatorId = a["Creator"]["Id"]
        Asset.CreatorType = a["Creator"]["CreatorType"]
        Asset.CreatorTargetId = a["Creator"]["CreatorTargetId"]
        Asset.IconImageAssetId = a["IconImageAssetId"]
        Asset.Created = a["Created"]
        Asset.Updated = a["Updated"]
        Asset.PriceInRobux = a["PriceInRobux"]
        Asset.Sales = a["Sales"]
        Asset.IsNew = a["IsNew"]
        Asset.IsForSale = a["IsForSale"]
        Asset.IsPublicDomain = a["IsPublicDomain"]
        Asset.IsLimited = a["IsLimited"]
        Asset.IsLimitedUnique = a["IsLimitedUnique"]
        Asset.Remaining = a["Remaining"]
        Asset.MinimumMembershipLevel = a["MinimumMembershipLevel"]
        Asset.ContentRatingTypeId = a["ContentRatingTypeId"]
        return Asset

    # GET https://www.roblox.com/studio/plugins/info?assetId={assetId}
    # Returns Table/Array
    def getAssetVersions(assetid):
        a = Http.sendRequest("https://www.roblox.com/studio/plugins/info?assetId=" + str(assetid))
        result = []
        for part in a:
            i = a.index(part)
            b = part
            result.insert(i, part)
        return result
