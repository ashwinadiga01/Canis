import json
import sys
import trace
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from stockIndices import getData

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

    def readData(self,message,niftyTable,niftyPrice,bankniftyPrice):
        getData(message)
        self.data = 'stockData.json'
        self.dataList = []
        with open(self.data) as fp:
            self.dataList = json.load(fp)

        tableUpdate(niftyTable,self.dataList)
        mainPrice(self.dataList,niftyPrice,bankniftyPrice)

def mainPrice(dataList,niftyPrice,bankniftyPrice):
    _translate = QtCore.QCoreApplication.translate

    for j in dataList:
        # print(j)
        if j['TK'] == 26000:
            niftyPrice.setText(_translate("Canis", str(j['PRICE'])))

        if j['TK'] == 26009:
            bankniftyPrice.setText(_translate("Canis", str(j['PRICE'])))


def tableUpdate(niftyTable,dataList):
    # print(self.dataList)
    _translate = QtCore.QCoreApplication.translate
    rowPosition = niftyTable.rowCount()
    # print(rowPosition,niftyTable.item(1,0).text())

    for i in range(rowPosition):
        for j in dataList:
            # print(j)
            if j['TK'] == int(niftyTable.item(i,0).text()):
                item = niftyTable.item(i, 2)
                item.setText(_translate("Canis", str(j['NETCNG'])))
                item = niftyTable.item(i, 3)
                item.setText(_translate("Canis", str(j['WMN'])))
                item = niftyTable.item(i, 4)
                item.setText(_translate("Canis", str(j['ICN'])))

                niftyTable.viewport().update()

        


# t1 = thread_with_trace(target = func)
# t1.start()
# time.sleep(2)
# t1.kill()
# t1.join()
# if not t1.isAlive():
#     print('thread killed')
