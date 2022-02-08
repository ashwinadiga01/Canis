from PyQt5 import QtCore, QtGui
import json

class updateData:
    def __init__(self,shareData,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice):
        self.shareData = shareData
        self.niftyTable = niftyTable
        self.bankniftyTable = bankniftyTable
        self.niftyPrice = niftyPrice
        self.bankniftyPrice = bankniftyPrice
        self.rowPositionNifty = self.niftyTable.rowCount()
        self.rowPositionBNKnifty = self.bankniftyTable.rowCount()

        self.swn = 'SWnifty.json'
        self.swnListObj = []
        with open(self.swn) as fp:
            self.swnListObj = json.load(fp)
        
        self.swb = 'SWbnknifty.json'
        self.swbListObj = []
        with open(self.swb) as fp:
            self.swbListObj = json.load(fp)


        self.getData()

    def getData(self):
        for i in self.shareData:
            if(i.get('tk') is not None and i.get('c') is not None and i.get('cng') is not None):
                if(i.get('tk') == '26000' or i.get('tk') == '26009'):
                    self.niftyAndBankNifty(i)

            else:
                self.dataUpdate(i)

    def niftyAndBankNifty(self,nftAndBnkNftDict):
        _translate = QtCore.QCoreApplication.translate
        if(nftAndBnkNftDict.get('tk') == '26000'):
            formatPrice = float("{:.2f}".format(float(nftAndBnkNftDict.get('ltp'))))
            temp = float(self.niftyPrice.text())
            self.niftyPrice.setText(str(formatPrice))
            if temp > formatPrice:
                self.niftyPrice.setStyleSheet("color: #EF6B6B;")
            else:
                self.niftyPrice.setStyleSheet("color: rgb(107, 239, 129);")


        if(nftAndBnkNftDict.get('tk') == '26009'):         
            formatPrice = float("{:.2f}".format(float(nftAndBnkNftDict.get('ltp'))))
            temp = float(self.bankniftyPrice.text())
            self.bankniftyPrice.setText(str(formatPrice))
            if temp > formatPrice:
                self.bankniftyPrice.setStyleSheet("color: #EF6B6B;")
            else:
                self.bankniftyPrice.setStyleSheet("color: rgb(107, 239, 129);")

    def dataUpdate(self,shareInfo):
        for i in range(self.rowPositionNifty):
            if int(shareInfo.get('tk')) == int(self.niftyTable.item(i,0).text()):
                formatNc = float("{:.4f}".format(float(shareInfo.get('nc'))))
                netchange = self.niftyTable.item(i, 2)
                netchange.setData(QtCore.Qt.DisplayRole,formatNc)
                netchange.setForeground(self.colorchange(formatNc))

                for j in self.swnListObj:
                    if int(shareInfo.get('tk')) == j.get('TK'):
                        scriptW = j.get('SW')
                        scriptM = formatNc
                        weightageMN =  (scriptW * scriptM)/10000
                        formatweightageMN = float("{:.5f}".format(weightageMN))
                        weightageMove = self.niftyTable.item(i, 3)
                        weightageMove.setData(QtCore.Qt.DisplayRole,formatweightageMN)
                        weightageMove.setForeground(self.colorchange(formatweightageMN))

                        indexContribution = formatweightageMN*float(self.niftyPrice.text())
                        formatindexContribution = float("{:.3f}".format(indexContribution))
                        indexContri = self.niftyTable.item(i, 4)
                        indexContri.setData(QtCore.Qt.DisplayRole,formatindexContribution)
                        indexContri.setForeground(self.colorchange(formatindexContribution))

                    self.niftyTable.viewport().update()
                self.niftyTable.sortItems(4, QtCore.Qt.AscendingOrder)

        for i in range(self.rowPositionBNKnifty):
            if int(shareInfo.get('tk')) == int(self.bankniftyTable.item(i,0).text()):
                formatNc = float("{:.4f}".format(float(shareInfo.get('nc'))))
                netchange = self.bankniftyTable.item(i, 2)
                netchange.setData(QtCore.Qt.DisplayRole,formatNc)
                netchange.setForeground(self.colorchange(formatNc))

                for j in self.swbListObj:
                    if int(shareInfo.get('tk')) == j.get('TK'):
                        scriptW = j.get('SW')
                        scriptM = formatNc
                        weightageMBN =  (scriptW * scriptM)/10000
                        formatweightageMBN = float("{:.5f}".format(weightageMBN))
                        weightageMove = self.bankniftyTable.item(i, 3)
                        weightageMove.setData(QtCore.Qt.DisplayRole,formatweightageMBN)
                        weightageMove.setForeground(self.colorchange(formatweightageMBN))

                        indexContribution = formatweightageMBN*float(self.bankniftyPrice.text())
                        formatindexContribution = float("{:.3f}".format(indexContribution))
                        indexContri = self.bankniftyTable.item(i, 4)
                        indexContri.setData(QtCore.Qt.DisplayRole,formatindexContribution)
                        indexContri.setForeground(self.colorchange(formatindexContribution))

                    self.bankniftyTable.viewport().update()
                self.bankniftyTable.sortItems(4, QtCore.Qt.AscendingOrder)
        
        # self.weightageMove()

    def weightageMove(self):
        for i in range(self.rowPositionNifty):
            for j in self.swnListObj:
                if int(self.niftyTable.item(i, 0).text()) == j.get('TK'):
                    scriptW = j.get('SW')
                    scriptM = float(self.niftyTable.item(i, 2).text())
                    weightageMN =  (scriptW * scriptM)/10000
                    formatweightageMN = float("{:.5f}".format(weightageMN))
                    item = self.niftyTable.item(i, 3)
                    item.setData(QtCore.Qt.DisplayRole,formatweightageMN)
                    item.setForeground(self.colorchange(formatweightageMN))
                    self.niftyTable.viewport().update()
            
            if self.bankniftyTable.item(i, 2) is not None:
                for j in self.swbListObj:
                    if int(self.bankniftyTable.item(i, 0).text()) == j.get('TK'):
                        scriptW = j.get('SW')
                        scriptM = float(self.bankniftyTable.item(i, 2).text())
                        weightageMBN =  (scriptW * scriptM)/10000
                        formatweightageMBN = float("{:.5f}".format(weightageMBN))
                        item = self.bankniftyTable.item(i, 3)
                        item.setData(QtCore.Qt.DisplayRole,formatweightageMBN)
                        item.setForeground(self.colorchange(formatweightageMBN))
                        self.bankniftyTable.viewport().update()

            self.indexContribution()

    def indexContribution(self):
        for i in range(self.rowPositionNifty):
            if self.niftyTable.item(i, 3) is not None:
                for j in self.swnListObj:
                    if int(self.niftyTable.item(i, 0).text()) == j.get('TK'):
                        weightagetM = float(self.niftyTable.item(i, 3).text())
                        indexContribution = weightagetM*float(self.niftyPrice.text())
                        formatindexContribution = float("{:.3f}".format(indexContribution))
                        item = self.niftyTable.item(i, 4)
                        item.setData(QtCore.Qt.DisplayRole,formatindexContribution)
                        item.setForeground(self.colorchange(formatindexContribution))
                        self.niftyTable.viewport().update()
            
            if self.bankniftyTable.item(i, 3) is not None:
                for j in self.swbListObj:
                    if int(self.bankniftyTable.item(i, 0).text()) == j.get('TK'):
                        weightagetM = float(self.bankniftyTable.item(i, 3).text())
                        indexContribution = weightagetM*float(self.bankniftyPrice.text())
                        formatindexContribution = float("{:.3f}".format(indexContribution))
                        item = self.bankniftyTable.item(i, 4)
                        item.setData(QtCore.Qt.DisplayRole,formatindexContribution)
                        item.setForeground(self.colorchange(formatindexContribution))
                        self.bankniftyTable.viewport().update()

    def colorchange(self,value):
        if value < 0:return QtGui.QBrush(QtGui.QColor(239, 107, 107))
        elif value == 0:return QtGui.QBrush(QtGui.QColor(255, 255, 255))
        else:return QtGui.QBrush(QtGui.QColor(107, 239, 129))
    
