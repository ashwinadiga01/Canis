import json
from operator import concat
from smartapi import SmartWebSocket, SmartConnect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont,QFontDatabase
from dialog import errorMain
from thread import thread_with_trace
import sys
from datetime import datetime

now = datetime.now()
today3pm = now.replace(hour=15, minute=30, second=0, microsecond=0)
today9am = now.replace(hour=9, minute=30, second=0, microsecond=0)

try:
    niftyToken = 'SWnifty.json'
    niftyTokenList = []
    bankniftyToken = 'SWbnknifty.json'
    bankniftyTokenList = []

    with open(niftyToken) as fp:
        niftyTokenList = json.load(fp)

    with open(bankniftyToken) as fp:
        bankniftyTokenList = json.load(fp)

except:
    error = "<html><head/><body><p>Either 'SWnifty.json' is missing<br>or<br>'SWbnknifty.json' is missing</p></body></html>"
    errorMain(error)

niftyTokenTemp = "nse_cm|26000&nse_cm|26009&"
bankniftyTokenTemp = "nse_cm|26000&nse_cm|26009&"

i=0
j=0


for token in niftyTokenList:
    if i == (len(niftyTokenList)-1):
        token = "nse_cm|" + str(token['TK']) 
        niftyTokenTemp = concat(niftyTokenTemp,token)
    else:
        token = "nse_cm|" + str(token['TK']) +"&"
        niftyTokenTemp = concat(niftyTokenTemp,token)
    i = i + 1

for token in bankniftyTokenList:
    if j == (len(bankniftyTokenList)-1):
        token = "nse_cm|" + str(token['TK']) 
        bankniftyTokenTemp = concat(bankniftyTokenTemp,token)
    else:
        token = "nse_cm|" + str(token['TK']) +"&"
        bankniftyTokenTemp = concat(bankniftyTokenTemp,token)
    j = j + 1


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_Canis(object):
    def __init__(self):
        QFontDatabase.addApplicationFont("Overpass.otf")
        self.font = QFont("Overpass")

        try:
            file1 = open('personalData.txt', 'r')
            Lines = file1.readlines()
            
            count = 0
            for line in Lines:
                count += 1
                if count == 1:
                    self.client_code = line.strip()
                
                if count == 2:
                    self.password = line.strip()

                if count == 3:
                    self.api_key = line.strip()
                
            CLIENT_CODE=self.client_code
            PASSWORD=self.password
            API_KEY=self.api_key

            try:
                obj=SmartConnect(api_key=API_KEY)
                obj.generateSession(CLIENT_CODE,PASSWORD)
                FEED_TOKEN = obj.getfeedToken() 
                self.ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

            except:
                error = "<html><head/><body><p>Wrong credentials entered!<br>Please check whether your credentials are correct or not.</p></body></html>"
                errorMain(error)

        except:
            error = "<html><head/><body><p>Either credential file is missing<br>or<br>'personalData.txt' is empty.</p></body></html>"
            errorMain(error)

        self.niftyTokenTemp = niftyTokenTemp
        self.bankniftyTokenTemp = bankniftyTokenTemp
        
        self.task="mw"
        self.t1=None
        self.t2=None
        self.t3=None
        self.t4=None
        self.t5=None
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        QtWidgets.QApplication.setFont(self.font)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(710, 720))
        Form.setMaximumSize(QtCore.QSize(710, 720))
        Form.setStyleSheet("background: #313131;")

        self.niftyPriceDisplay = QtWidgets.QFrame(Form)
        self.niftyPriceDisplay.setGeometry(QtCore.QRect(20, 22, 261, 80))
        self.niftyPriceDisplay.setStyleSheet("position: absolute; left: 19px; top: 49px; color:#ffffff; background: #232222;border-radius: 16px;")
        self.niftyPriceDisplay.setObjectName("niftyPriceDisplay")

        self.nifty = QtWidgets.QLabel(self.niftyPriceDisplay)
        self.nifty.setGeometry(QtCore.QRect(30, 0, 91, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nifty.setFont(font)
        self.nifty.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.nifty.setObjectName("nifty")

        self.niftyPrice = QtWidgets.QLabel(self.niftyPriceDisplay)
        self.niftyPrice.setGeometry(QtCore.QRect(120, 0, 121, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.niftyPrice.setFont(font)
        self.niftyPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.niftyPrice.setObjectName("niftyPrice")

        self.bankniftyPriceDisplay = QtWidgets.QFrame(Form)
        self.bankniftyPriceDisplay.setGeometry(QtCore.QRect(300, 22, 280, 80))
        self.bankniftyPriceDisplay.setStyleSheet("position: absolute; left: 19px; top: 49px; color:#ffffff; background: #232222; border-radius: 16px;")
        self.bankniftyPriceDisplay.setObjectName("bankniftyPriceDisplay")

        self.banknifty = QtWidgets.QLabel(self.bankniftyPriceDisplay)
        self.banknifty.setGeometry(QtCore.QRect(20, 0, 131, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.banknifty.setFont(font)
        self.banknifty.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.banknifty.setObjectName("banknifty")

        self.bankniftyPrice = QtWidgets.QLabel(self.bankniftyPriceDisplay)
        self.bankniftyPrice.setGeometry(QtCore.QRect(150, 0, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bankniftyPrice.setFont(font)
        self.bankniftyPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.bankniftyPrice.setObjectName("bankniftyPrice")

        self.stopMarket = QtWidgets.QRadioButton(Form)
        self.stopMarket.setGeometry(QtCore.QRect(605, 69, 81, 30))
        self.stopMarket.setStyleSheet("QRadioButton{color:white;} QRadioButton::indicator{width:10px; height:10px; border-radius:7px;} QRadioButton::indicator:checked{background-color:rgb(255, 60, 89); border:2px solid rgb(97, 0, 1);} QRadioButton::indicator:unchecked {background-color:rgb(166, 166, 166); border:2px solid white;}  QRadioButton::indicator:disabled {color:#414141;background-color:#5b5b5b; border:2px solid #414141;}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopMarket.sizePolicy().hasHeightForWidth())
        self.stopMarket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stopMarket.setFont(font)
        self.stopMarket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopMarket.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stopMarket.setObjectName("stopMarket")

        self.startMarket = QtWidgets.QRadioButton(Form)
        self.startMarket.setGeometry(QtCore.QRect(605, 30, 80, 30))
        self.startMarket.setStyleSheet("QRadioButton{color:white;} QRadioButton::indicator{width:10px;height:10px;border-radius:7px;} QRadioButton::indicator:checked{background-color:rgb(73, 255, 118); border:2px solid rgb(10, 100, 0);} QRadioButton::indicator:unchecked {background-color:rgb(166, 166, 166); border:2px solid white;} QRadioButton::indicator:disabled {color:#414141;background-color:#5b5b5b; border:2px solid #414141;}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startMarket.sizePolicy().hasHeightForWidth())
        self.startMarket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.startMarket.setFont(font)
        self.startMarket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startMarket.setObjectName("startMarket")

        self.stockData = QtWidgets.QTabWidget(Form)
        self.stockData.setGeometry(QtCore.QRect(-10, 120, 741, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockData.sizePolicy().hasHeightForWidth())
        self.stockData.setSizePolicy(sizePolicy)

        self.stockData.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stockData.setStyleSheet("*{background: #4D4D4D;border : 0px;} QTabBar{background: #313131;} QTabBar::tab{font : 18px;width:200px;height: 60px;background:  #3B3B3B;color: #fff ;border-radius: 10px ;top: 10;padding-bottom: 5;} QTabBar::tab::selected{font: bold; color: white; width: 200px;height: 60px;background: #4D4D4D;"
                                        "border-radius: 10px;} QTabBar::tab:first{margin-left:30; margin-right:5;} QTableWidget{color: #fff; background-color: #2C2C2C; border-radius: 16px; font : 16px; gridline-color: #000; alternate-background-color: #111;padding:5;} QHeaderView::section{background-color: #2C2C2C; color: #fff; padding-top:10;"
                                        "padding-bottom:10; border-radius: 16px; color:#9CD0F6; font : 17px; font-weight:bold;} QTableWidget QTableCornerButton:section{background-color: #2C2C2C;} QTableWidget::item:selected{background-color: #2C2C2C;} QHeaderView{background-color: #2C2C2C;border-bottom: 2px solid #C2AEAE;} QScrollBar{"
                                        "background-color: #2c2c2c;width:14px;padding: 57px 3px 10px 0px;} QScrollBar::handle:vertical {min-height: 0px;border-radius: 5px;background-color: rgb(92, 95, 141);} QScrollBar::add-line:vertical {height: 0px;subcontrol-position: bottom;subcontrol-origin: margin;} QScrollBar::sub-line:vertical"
                                        "{height: 0 px;subcontrol-position: top;subcontrol-origin: margin;}")
        self.stockData.setTabPosition(QtWidgets.QTabWidget.North)
        self.stockData.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.stockData.setIconSize(QtCore.QSize(40, 20))
        self.stockData.setElideMode(QtCore.Qt.ElideMiddle)
        self.stockData.setUsesScrollButtons(False)
        self.stockData.setObjectName("stockData")

        self.niftyTable = QtWidgets.QWidget()
        self.niftyTable.setStyleSheet("")
        self.niftyTable.setObjectName("niftyTable")

        self.niftyStockPrices = QtWidgets.QTableWidget(self.niftyTable)
        self.niftyStockPrices.setObjectName("niftyStockPrices")
        self.niftyStockPrices.setColumnCount(5)
        self.niftyStockPrices.setRowCount(len(niftyTokenList))

        for i in range(self.niftyStockPrices.rowCount()):    
            item = QtWidgets.QTableWidgetItem()
            self.niftyStockPrices.setVerticalHeaderItem(i, item)

        for i in range(self.niftyStockPrices.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.niftyStockPrices.setHorizontalHeaderItem(i, item)

        for i in range(self.niftyStockPrices.rowCount()):
            for j in range(self.niftyStockPrices.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.niftyStockPrices.setItem(i, j, item)

        self.stockData.addTab(self.niftyTable, "")

        self.bankniftyTable = QtWidgets.QWidget()
        self.bankniftyTable.setObjectName("bankniftyTable")
        self.bankniftyStockPrices = QtWidgets.QTableWidget(self.bankniftyTable)

        for i in [self.niftyStockPrices, self.bankniftyStockPrices]:
            i.setGeometry(QtCore.QRect(30, 20, 671, 491))
            delegate = AlignDelegate(i)
            i.setItemDelegate(delegate)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(i.sizePolicy().hasHeightForWidth())
            i.setSizePolicy(sizePolicy)
            i.setLayoutDirection(QtCore.Qt.LeftToRight)
            i.setStyleSheet("")
            i.setLineWidth(1)
            i.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            i.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            i.setGridStyle(QtCore.Qt.DashDotDotLine)

        self.bankniftyStockPrices.setObjectName("bankniftyStockPrices")
        self.bankniftyStockPrices.setColumnCount(5)
        self.bankniftyStockPrices.setRowCount(len(bankniftyTokenList))

        for i in range(self.bankniftyStockPrices.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.bankniftyStockPrices.setVerticalHeaderItem(i, item)

        for i in range(self.bankniftyStockPrices.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.bankniftyStockPrices.setHorizontalHeaderItem(i, item)

        for i in range(self.bankniftyStockPrices.rowCount()):
            for j in range(self.bankniftyStockPrices.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.bankniftyStockPrices.setItem(i, j, item)

        for i in [self.niftyStockPrices, self.bankniftyStockPrices]:
            i.horizontalHeader().setVisible(True)
            i.horizontalHeader().setCascadingSectionResizes(False)
            i.horizontalHeader().setDefaultSectionSize(128)
            i.horizontalHeader().setHighlightSections(True)
            i.horizontalHeader().setMinimumSectionSize(128)
            i.horizontalHeader().setSortIndicatorShown(False)
            i.horizontalHeader().setStretchLastSection(False)
            i.verticalHeader().setVisible(False)
            i.verticalHeader().setCascadingSectionResizes(True)
            i.verticalHeader().setDefaultSectionSize(44)
            i.verticalHeader().setMinimumSectionSize(44)
            i.verticalHeader().setStretchLastSection(True)

        self.stockData.addTab(self.bankniftyTable, "")
        self.retranslateUi(Form)
        self.stockData.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Canis"))
        self.nifty.setText(_translate("Form", "NIFTY :"))
        self.niftyPrice.setText(_translate("Form", "0"))
        self.banknifty.setText(_translate("Form", "BANK NIFTY :"))
        self.bankniftyPrice.setText(_translate("Form", "0"))
        self.stopMarket.setText(_translate("Form", "STOP"))
        self.startMarket.setText(_translate("Form", "START "))

        __sortingEnabled = self.niftyStockPrices.isSortingEnabled()
        self.niftyStockPrices.setSortingEnabled(False)
        __sortingEnabled = self.bankniftyStockPrices.isSortingEnabled()
        self.bankniftyStockPrices.setSortingEnabled(False)

        tokenList = [niftyTokenList,bankniftyTokenList]
        count = 0
        for i in [self.niftyStockPrices, self.bankniftyStockPrices]:
            count2 = 0
            for j in ["Token no.","Stock Name","Net CNG (%)","WM (%)","IC (%)"]:
                item = i.horizontalHeaderItem(count2)
                item.setText(_translate("Form", j))
                count2+=1
        
            for j in range(i.rowCount()):
                item = i.item(j, 0)
                item.setText(_translate("Form", str(tokenList[count][j].get('TK'))))
                item = i.item(j, 1)
                item.setText(_translate("Form", str(tokenList[count][j].get('STOCKNAME'))))
                for k in range(2,5):
                    item = i.item(j, k)
                    item.setData(QtCore.Qt.DisplayRole,0)

            count+=1
                
        self.niftyStockPrices.setSortingEnabled(__sortingEnabled)
        self.stockData.setTabText(self.stockData.indexOf(self.niftyTable), _translate("Form", "NIFTY"))
        self.bankniftyStockPrices.setSortingEnabled(__sortingEnabled)
        self.stockData.setTabText(self.stockData.indexOf(self.bankniftyTable), _translate("Form", "BANK NIFTY"))

        self.startMarket.clicked.connect(self.webSocketCall)
        self.stopMarket.clicked.connect(self.webSocketCall)

        i = 0
        self.onChange(i)
        self.stockData.currentChanged.connect(self.onChange)

        if self.startMarket.isChecked() is False:
            self.stopMarket.setDisabled(True)

    def threadMsg(self,message):    
        if message is not None:
            now = datetime.now()
            if now > today3pm:
                self.startMarket.setChecked(False)
                self.startMarket.setEnabled(False)
                self.stopMarket.setChecked(True)
                self.threadKill()

            else:
                self.t2 = thread_with_trace(target = thread_with_trace.readData(self,message,self.niftyStockPrices,self.bankniftyStockPrices,self.niftyPrice,self.bankniftyPrice))
                self.t2.start()
                self.t4 = thread_with_trace(target = thread_with_trace.dataUpdate(self,message,self.niftyStockPrices,self.bankniftyStockPrices,self.niftyPrice,self.bankniftyPrice))
                self.t4.start()
                self.t5 = thread_with_trace(target = thread_with_trace.dataUpdate2(self,message,self.niftyStockPrices,self.bankniftyStockPrices,self.niftyPrice,self.bankniftyPrice))
                self.t5.start()

    def onChange(self,i):
        if i == 0 and self.startMarket.isChecked() is False and self.stopMarket.isChecked() is False:
            self.token = self.niftyTokenTemp
        
        if i == 1 and self.startMarket.isChecked() is False and self.stopMarket.isChecked() is False:
            self.token = self.bankniftyTokenTemp

        if i == 0 and self.t1 is not None and self.t5 is not None and self.startMarket.isChecked() is True:
            self.t1.kill()
            self.t5.kill()
            self.token = self.niftyTokenTemp
            self.webSocketLmao()
            
        if i == 1 and self.t1 is not None and self.t4 is not None and self.startMarket.isChecked() is True:
            self.t1.kill()
            self.t4.kill()
            self.token = self.bankniftyTokenTemp
            self.webSocketLmao()
        
    def webSocketLmao(self):
            self.ss._on_open = lambda ws:self.ss.subscribe(self.task,self.token)
            self.ss._on_message = lambda ws,message:self.threadMsg(message)
            self.ss._on_error = lambda ws,error:print(error)
            self.ss._on_close = lambda ws:print("Close")
            self.t1 = thread_with_trace(target = self.ss.connect)
            self.t1.start()
            

    def webSocketCall(self):
        if self.startMarket.isChecked():
            self.webSocketLmao()
            self.stopMarket.setDisabled(False)
            
        if self.stopMarket.isChecked():
            self.t1.kill()
            if self.t2 is not None:self.t2.kill()

    def threadKill(self):
        if self.t1 and self.t1 is not None:self.t1.kill()
        if self.t2 and self.t2 is not None:self.t2.kill()
        if self.t3 and self.t3 is not None:self.t3.kill()
        if self.t4 and self.t4 is not None:self.t4.kill()
        if self.t4 and self.t5 is not None:self.t5.kill()

def sysExit():
    app.exec_()
    ui.threadKill()

if __name__ == "__main__":
    if now < today3pm and now > today9am:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Canis = QtWidgets.QWidget()
        ui = Ui_Canis()
        ui.setupUi(Canis)
        Canis.show()
        sys.exit(sysExit())

    else:
        error = "<html><head/><body><p>App can be accessed only when the<br>Market is open!<br>(9:30am IST to 3:30pm IST)</p></body></html>"
        errorMain(error)
