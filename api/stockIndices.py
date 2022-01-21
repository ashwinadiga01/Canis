from operator import concat
from traceback import print_tb
from typing import ChainMap
import json

filename = 'stockData.json'
listObj = []

with open(filename) as fp:
  listObj = json.load(fp)

class stockIndices:
    def niftyAndBankNifty(nftAndBnkNftDict):
        # nftAndBnkNftDict = dict(ChainMap(*nftAndBnkNftList))

        if(nftAndBnkNftDict.get('tk') == '26000'):
            print("nifty: - ", nftAndBnkNftDict.get('c'))
            checkUpdateOrAdd(int(nftAndBnkNftDict.get('tk')),float(nftAndBnkNftDict.get('c')),float(nftAndBnkNftDict.get('cng')))

        if(nftAndBnkNftDict.get('tk') == '26009'):
            print("banknifty: -",nftAndBnkNftDict.get('c'))            
            checkUpdateOrAdd(int(nftAndBnkNftDict.get('tk')),float(nftAndBnkNftDict.get('c')),float(nftAndBnkNftDict.get('cng')))

    
    def otherStocks(otherStockDataDict):
        checkUpdateOrAdd(int(otherStockDataDict.get('tk')),float(otherStockDataDict.get('c')),float(otherStockDataDict.get('cng')))


def updateJSON(tk,price,nc):
    for i in listObj:
        if(tk == 26000 or tk ==26009):
            if(i['TK'] == tk or i['TK'] == tk):
                Price = {"PRICE" : price}
                i.update(Price)

        else:
            if(i['TK'] == tk or i['TK'] == tk):
                NetCng = {"NETCNG" : nc}
                i.update(NetCng)


def addToJSON(tk,price,nc):
    if(tk == 26000 or tk == 26009):
        listObj.append({
        "TK": tk,
        "PRICE" : price
        })

    else:
        listObj.append({
        "TK": tk,
        "NETCNG" : nc
        })

def checkUpdateOrAdd(tk,price,nc):
    count = 0
    for i in listObj:
        count+=1
        if(i.get('TK') == tk):
            updateJSON(tk,price,nc)
            break
        
        elif(i.get('TK') != tk):
            if(count == len(listObj)):
                addToJSON(tk,price,nc)
                break

# def getData(shareData):
#     niftylist = list(filter(lambda item: item['tk'] == '26000',shareData))
#     stockIndices.niftyAndBankNifty(niftylist)
    
#     bankniftylist = list(filter(lambda item: item['tk'] == '26009',shareData))
#     stockIndices.niftyAndBankNifty(bankniftylist)
    
#     removeIndices = [niftylist[0],bankniftylist[0]]
#     for i in removeIndices:
#         shareData.remove(i)
#     print(shareData)
        
#     stockIndices.otherStocks(shareData)


def getData(shareData):
    for i in shareData:
        if(i.get('tk') is not None and i.get('c') is not None and i.get('cng') is not None):
            if(i.get('tk') == '26000' or i.get('tk') == '26009'):
                print(i)
                stockIndices.niftyAndBankNifty(i)

            else:
                print(i)
                stockIndices.otherStocks(i)

# getData([{'c': '233' ,'cng': '-146','e': 'nse_cm', 'ltp': '1955.20', 'ltq': '2', 'ltt': 'NA', 'name': 'sf', 'tk': '11483'}, {'c': '233' ,'cng': '-146', 'e': 'nse_cm', 'ltp': '17610.15', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.827', 'tk': '26000'}, {'c': '37850.5', 'cng': '-313.65', 'e': 'nse_cm', 'ltp': '37537.20', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.8286', 'tk': '26009'}])



with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, indent=4, separators=(',',': '))
    