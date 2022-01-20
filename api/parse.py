import json
from operator import concat
from typing import ChainMap
from urllib.request import urlopen

shareDataURL = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
responseURL = urlopen(shareDataURL)

data = json.loads(responseURL.read())
# print("idharse",data[100])

def shareData(shareName):
    shareSymbol = concat(shareName,'-EQ')
    print(shareSymbol)
    aboutShare = list(filter(lambda item: item['symbol'] == shareSymbol,data))
    dictAboutShare = dict(ChainMap(*aboutShare))
    print(dictAboutShare['token'])

shareName = input("Enter share name : ")
shareData(shareName)

# for i in data:
#     if (len(i)<10):
#         print("\n",data)
#     break


