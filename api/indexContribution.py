from ast import Index
import json
# from test2 import lista

# from test2 import Ui_Form

def nandbprice(wm,wmListObj,swnpListObj,swbnpListObj):
    for i in wmListObj:
        if i.get('TK') == 26000:
            niftyP = i.get('PRICE')

        if i.get('TK') == 26009:
            bankniftyP = i.get('PRICE')
    
    indexContribution(wm,wmListObj,swnpListObj,swbnpListObj,niftyP,bankniftyP)

def indexContribution(ic,icListObj,swnpListObj,swbnpListObj,niftyP,bankniftyP):
    for i in icListObj:
        if i.get('WMN') is not None:
            for j in swnpListObj:
                if(i.get('TK') == j.get('TK')):
                    weightagetM = i.get('WMN')
                    indexContribution = weightagetM*niftyP
                    formatindexContribution = float("{:.3f}".format(indexContribution))
                    IC = {"ICN":formatindexContribution}
                    i.update(IC)

        if i.get('WMBN') is not None:
            for j in swbnpListObj:
                if(i.get('TK') == j.get('TK')):
                    weightagetM = i.get('WMBN')
                    indexContribution = weightagetM*bankniftyP
                    formatindexContribution = float("{:.3f}".format(indexContribution))
                    IC = {"ICB":formatindexContribution}
                    i.update(IC)

    # print("aaaaaaaaaaa")
    # lista()

    with open(ic, 'w') as json_file:
        json.dump(icListObj, json_file, indent=4, separators=(',',': '))