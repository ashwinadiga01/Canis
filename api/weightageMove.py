import json

sm = 'stockData.json'
swn = 'SWnifty.json'
swb = 'SWbnknifty.json'
smListObj = []
swnListObj = []
swbListObj = []

with open(sm) as fp:
  smListObj = json.load(fp)

with open(swn) as fp:
  swnListObj = json.load(fp)

with open(swb) as fp:
  swbListObj = json.load(fp)

def weightageMove():
    for i in smListObj:
        if i.get('NETCNG') is not None:
            for j in swnListObj:
                if i.get('TK') == j.get('TK'):
                    scriptW = j.get('SW')
                    scriptM = i.get('NETCNG')
                    weightageMN =  (scriptW * scriptM)/10000
                    WMN = {"WMN" : weightageMN}
                    i.update(WMN)
            
            for j in swbListObj:
                if i.get('TK') == j.get('TK'):
                    scriptW = j.get('SW')
                    scriptM = i.get('NETCNG')
                    weightageMBN =  (scriptW * scriptM)/10000
                    WMBN = {"WMBN" : weightageMBN}
                    i.update(WMBN)

weightageMove()

with open(sm, 'w') as json_file:
    json.dump(smListObj, json_file, indent=4, separators=(',',': '))


