import json
from operator import concat
from typing import ChainMap
from urllib.request import urlopen

shareDataURL = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
responseURL = urlopen(shareDataURL)

sd = "SWnifty.json"
sdList = []

data = json.loads(responseURL.read())

with open(sd) as fp:
  sdList = json.load(fp)

def shareName(sdList):
    for i in sdList:
        if i.get('TK') is not None:
            stockName = list(filter(lambda item: item['token'] == str(i.get('TK')),data))         
            nameDict = dict(ChainMap(*stockName))
            name = {"STOCKNAME" : nameDict.get('name')}
            i.update(name)

    with open(sd, 'w') as json_file:
        json.dump(sdList, json_file, indent=4, separators=(',',': '))

shareName(sdList)

def shareData(shareName):
    shareSymbol = concat(shareName,'-EQ')
    print(shareSymbol)
    aboutShare = list(filter(lambda item: item['symbol'] == shareSymbol,data))
    dictAboutShare = dict(ChainMap(*aboutShare))
    print(dictAboutShare['token'])

shareName = input("Enter share name : ")
shareData(shareName)


