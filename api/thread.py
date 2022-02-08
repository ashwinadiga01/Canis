import json
import sys
import threading
from PyQt5 import QtCore, QtGui
from updateData import updateData

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run	
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:   
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

    def func():
        while True:
            print('thread running')

    def readData(self,message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice):
        updateData(message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice)
        # getData(message)

        # self.data = 'stockData.json'
        # self.backup = 'bkup.json'
        # self.dataList = []
        # self.bkup = []

        # with open(self.data) as fp:
        #     self.dataList = json.load(fp)
        #     print(len(self.dataList))
        
        # if len(self.dataList) == 0:
        #     print("akadks")
        
        # self.data = 'stockData.json'
        # self.bk = 'bkup.json'
        # self.dataList = []

        # # try:
        # with open(self.data) as fp:
        #     self.dataList = json.load(fp)

        # except:
        #     with open(self.bk) as fp:
        #         self.dataList = json.load(fp)
        #         print("aaaaaaaaa",len(self.dataList))


        # tableUpdate(niftyTable,bankniftyTable,self.dataList)
        # mainPrice(self.dataList,niftyPrice,bankniftyPrice)

def mainPrice(dataList,niftyPrice,bankniftyPrice):
    _translate = QtCore.QCoreApplication.translate
    for j in dataList:
        if j['TK'] == 26000:
            temp = float(niftyPrice.text())
            if temp > j['PRICE']:
                niftyPrice.setStyleSheet("color: #EF6B6B;")
            else:
                niftyPrice.setStyleSheet("color: rgb(107, 239, 129);")

        if j['TK'] == 26009:
            temp = float(bankniftyPrice.text())
            if temp > j['PRICE']:
                bankniftyPrice.setStyleSheet("color: #EF6B6B;")
            else:
                bankniftyPrice.setStyleSheet("color: rgb(107, 239, 129);")

def tableUpdate(niftyTable,bankniftyTable,dataList):
    _translate = QtCore.QCoreApplication.translate
    rowPositionNifty = niftyTable.rowCount()
    rowPositionBNKnifty = bankniftyTable.rowCount()

    for i in range(rowPositionNifty):
        for j in dataList:
            if j['TK'] == int(niftyTable.item(i,0).text()):
                item = niftyTable.item(i, 2)
                item.setData(QtCore.Qt.DisplayRole,float(j['NETCNG']))
                item.setForeground(colorchange(j['NETCNG']))

                item = niftyTable.item(i, 3)
                item.setData(QtCore.Qt.DisplayRole,float(j['WMN']))
                item.setForeground(colorchange(j['WMN']))

                item = niftyTable.item(i, 4)
                item.setData(QtCore.Qt.DisplayRole,float(j['ICN']))
                item.setForeground(colorchange(j['ICN']))

                niftyTable.viewport().update()
                niftyTable.sortItems(4, QtCore.Qt.AscendingOrder)

    for i in range(rowPositionBNKnifty):
        for j in dataList:
            if j['TK'] == int(bankniftyTable.item(i,0).text()) and j["WMBN"] is not None:
                item = bankniftyTable.item(i, 2)
                item.setData(QtCore.Qt.DisplayRole,float(j['NETCNG']))
                item.setForeground(colorchange(j['NETCNG']))
                item = bankniftyTable.item(i, 3)
                item.setData(QtCore.Qt.DisplayRole,float(j['WMBN']))
                item.setForeground(colorchange(j['WMBN']))
                item = bankniftyTable.item(i, 4)
                item.setData(QtCore.Qt.DisplayRole,float(j['ICB']))
                item.setForeground(colorchange(j['ICB']))
                bankniftyTable.viewport().update()
                bankniftyTable.sortItems(4, QtCore.Qt.AscendingOrder)
                

def colorchange(value):
    if value < 0:return QtGui.QBrush(QtGui.QColor(239, 107, 107))
    elif value == 0:return QtGui.QBrush(QtGui.QColor(255, 255, 255))
    else:return QtGui.QBrush(QtGui.QColor(107, 239, 129))