import json
from indexContribution import nandbprice

def updateList():
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

  weightageMove(sm,smListObj,swnListObj,swbListObj)
  nandbprice(sm,smListObj,swnListObj,swbListObj)

def weightageMove(sm,smListObj,swnListObj,swbListObj):
    for i in smListObj:
        if i.get('NETCNG') is not None:
            for j in swnListObj:
                if i.get('TK') == j.get('TK'):
                    scriptW = j.get('SW')
                    scriptM = i.get('NETCNG')
                    weightageMN =  (scriptW * scriptM)/10000
                    formatweightageMN = float("{:.5f}".format(weightageMN))
                    WMN = {"WMN" : formatweightageMN}
                    i.update(WMN)
		
            for j in swbListObj:
                if i.get('TK') == j.get('TK'):
                    scriptW = j.get('SW')
                    scriptM = i.get('NETCNG')
                    weightageMBN =  (scriptW * scriptM)/10000
                    formatweightageMBN = float("{:.5f}".format(weightageMBN))
                    WMBN = {"WMBN" : formatweightageMBN}
                    i.update(WMBN)

    with open(sm, 'w') as json_file:
    	json.dump(smListObj, json_file, indent=4, separators=(',',': '))


