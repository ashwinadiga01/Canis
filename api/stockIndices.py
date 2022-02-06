import json
from weightageMove import updateList

filename = 'stockData.json'
listObj = []

with open(filename) as fp:
    listObj = json.load(fp)

class stockIndices:
    def niftyAndBankNifty(nftAndBnkNftDict):
        if(nftAndBnkNftDict.get('tk') == '26000'):
            checkUpdateOrAdd(int(nftAndBnkNftDict.get('tk')),float(nftAndBnkNftDict.get('ltp')),float(nftAndBnkNftDict.get('nc')))

        if(nftAndBnkNftDict.get('tk') == '26009'):         
            checkUpdateOrAdd(int(nftAndBnkNftDict.get('tk')),float(nftAndBnkNftDict.get('ltp')),float(nftAndBnkNftDict.get('nc')))

    def otherStocks(otherStockDataDict):
        checkUpdateOrAdd(int(otherStockDataDict.get('tk')),float(otherStockDataDict.get('c')),float(otherStockDataDict.get('nc')))


def updateJSON(tk,price,nc):
    for i in listObj:
        if(tk == 26000 or tk ==26009):
            if(i['TK'] == tk or i['TK'] == tk):
                formatPrice = float("{:.1f}".format(price))
                Price = {"PRICE" : formatPrice}
                i.update(Price)

        else:
            if(i['TK'] == tk or i['TK'] == tk):
                formatNc = float("{:.1f}".format(nc))
                NetCng = {"NETCNG" : formatNc}
                i.update(NetCng)

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))
    updateList()

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

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))

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

def getData(shareData):
    for i in shareData:
        if(i.get('tk') is not None and i.get('c') is not None and i.get('cng') is not None):
            if(i.get('tk') == '26000' or i.get('tk') == '26009'):
                stockIndices.niftyAndBankNifty(i)

            else:
                stockIndices.otherStocks(i)

with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, indent=4, separators=(',',': '))
    