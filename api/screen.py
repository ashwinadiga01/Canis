import json
from operator import concat
import os
from smartapi import SmartWebSocket, SmartConnect
from dotenv import load_dotenv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont,QFontDatabase
from thread import thread_with_trace

niftyToken = 'SWnifty.json'
niftyTokenList = []
bankniftyToken = 'SWbnknifty.json'
bankniftyTokenList = []

with open(niftyToken) as fp:
    niftyTokenList = json.load(fp)

with open(bankniftyToken) as fp:
    bankniftyTokenList = json.load(fp)

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
        load_dotenv()
        QFontDatabase.addApplicationFont("Overpass.otf")
        self.font = QFont("Overpass")
        CLIENT_CODE=os.getenv('Client_ID')
        PASSWORD=os.getenv('Password')
        API_KEY=os.getenv('API_key')
        # self.example = [{'e': 'nse_cm', 'ltp': '1955.20', 'ltq': '2', 'ltt': 'NA', 'name': 'sf', 'tk': '11483'}, {'c': '17757.00', 'cng': '-146.85', 'e': 'nse_cm', 'ltp': '17610', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.827', 'tk': '26000'}, {'c': '37850.85', 'cng': '-313.65', 'e': 'nse_cm', 'ltp': '37537.20', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.8286', 'tk': '26009'}]

        obj=SmartConnect(api_key=API_KEY)
        obj.generateSession(CLIENT_CODE,PASSWORD)
        FEED_TOKEN = obj.getfeedToken() 

        self.niftyTokenTemp = niftyTokenTemp
        self.bankniftyTokenTemp = bankniftyTokenTemp
        # self.token="nse_cm|26000&nse_cm|26009&nse_cm|1130&nse_cm|11483&nse_cm|4963&nse_cm|1922&nse_cm|2885&nse_cm|1594&nse_cm|1333&nse_cm|1330&nse_cm|11536&nse_cm|1394&nse_cm|1660"
        self.token2 = self.niftyTokenTemp + self.bankniftyTokenTemp
        # print(self.token2)
        self.task="mw"
        self.ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

       

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
        self.niftyPriceDisplay.setStyleSheet("position: absolute;\n"
"left: 19px;\n"
"top: 49px;\n"
"color:#ffffff;\n"
"background: rgb(96,96,96);\n"
"border-radius: 16px;")
        self.niftyPriceDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.niftyPriceDisplay.setFrameShadow(QtWidgets.QFrame.Raised)
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
        self.bankniftyPriceDisplay.setStyleSheet("position: absolute;\n"
"left: 19px;\n"
"top: 49px;\n"
"color:#ffffff;\n"
"background: rgb(96,96,96);\n"
"border-radius: 16px;")
        self.bankniftyPriceDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bankniftyPriceDisplay.setFrameShadow(QtWidgets.QFrame.Raised)
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
        self.stopMarket.setStyleSheet("QRadioButton {\n"
"    color:white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius:7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"\n"
"background-color:rgb(255, 60, 89);\n"
"    border:2px solid rgb(97, 0, 1);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color:rgb(166, 166, 166);\n"
"    border:2px solid white;\n"
"}")
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
        self.startMarket.setStyleSheet("QRadioButton {\n"
"    color:white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius:7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"\n"
"background-color:rgb(73, 255, 118);\n"
"    border:2px solid rgb(10, 100, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color:rgb(166, 166, 166);\n"
"    border:2px solid white;\n"
"}")
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
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 77, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stockData.setPalette(palette)
        self.stockData.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stockData.setStyleSheet("*{\n"
"background: #4D4D4D;\n"
"border : 0px;\n"
"}\n"
"\n"
"QTabBar{\n"
"background: #313131;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"font : 18px;\n"
"width:200px;\n"
"height: 60px;\n"
"background:  rgb(37, 37, 37);\n"
"color: #fff ;\n"
"border-radius: 10px ;\n"
"top: 10;\n"
"padding-bottom: 5;\n"
"}\n"
"\n"
"QTabBar::tab::selected{\n"
"font: bold;\n"
"color: white;\n"
"width: 200px;\n"
"height: 60px;\n"
"background: #4D4D4D;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:first{\n"
"margin-left:30;\n"
"margin-right:5;\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"    color: #fff;\n"
"    background-color: #2C2C2C;\n"
"border-radius: 16px;\n"
"font : 16px;\n"
"    gridline-color: #000;\n"
"    alternate-background-color: #111;\n"
"    padding:5;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    background-color: #2C2C2C;\n"
"    color: #fff;\n"
"    padding-top:10;\n"
"    padding-bottom:10;\n"
"border-radius: 16px;\n"
"color:#9CD0F6;\n"
"font : 17px;\n"
"font-weight:bold;\n"
"} \n"
"QTableWidget QTableCornerButton:section\n"
"{\n"
"    background-color: #2C2C2C;\n"
"}\n"
"\n"
"QTableWidget::item:selected\n"
"{\n"
"    background-color: #2C2C2C;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #2C2C2C;\n"
"border-bottom: 2px solid #C2AEAE;\n"
"}\n"
"\n"
"\n"
"QScrollBar\n"
"{\n"
" background-color: #2c2c2c;        \n"
"width:14px;    \n"
"padding: 50px 3px 10px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {         \n"
"min-height: 0px;\n"
"border-radius: 5px;\n"
"background-color: rgb(92, 95, 141);\n"
"}\n"
"QScrollBar::add-line:vertical {       \n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}")
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
        self.niftyStockPrices.setGeometry(QtCore.QRect(30, 20, 671, 490))
        delegate = AlignDelegate(self.niftyStockPrices)
        self.niftyStockPrices.setItemDelegate(delegate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.niftyStockPrices.sizePolicy().hasHeightForWidth())
        self.niftyStockPrices.setSizePolicy(sizePolicy)
        self.niftyStockPrices.setMaximumSize(QtCore.QSize(671, 490))
        self.niftyStockPrices.setStyleSheet("")
        self.niftyStockPrices.setFrameShape(QtWidgets.QFrame.Panel)
        self.niftyStockPrices.setFrameShadow(QtWidgets.QFrame.Plain)
        self.niftyStockPrices.setLineWidth(1)
        self.niftyStockPrices.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.niftyStockPrices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.niftyStockPrices.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.niftyStockPrices.setObjectName("niftyStockPrices")
        self.niftyStockPrices.setColumnCount(5)
        self.niftyStockPrices.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.niftyStockPrices.setItem(9, 4, item)
        self.niftyStockPrices.horizontalHeader().setVisible(True)
        self.niftyStockPrices.horizontalHeader().setCascadingSectionResizes(False)
        self.niftyStockPrices.horizontalHeader().setDefaultSectionSize(128)
        self.niftyStockPrices.horizontalHeader().setHighlightSections(True)
        self.niftyStockPrices.horizontalHeader().setMinimumSectionSize(128)
        self.niftyStockPrices.horizontalHeader().setSortIndicatorShown(False)
        self.niftyStockPrices.horizontalHeader().setStretchLastSection(False)
        self.niftyStockPrices.verticalHeader().setVisible(False)
        self.niftyStockPrices.verticalHeader().setCascadingSectionResizes(True)
        self.niftyStockPrices.verticalHeader().setDefaultSectionSize(44)
        self.niftyStockPrices.verticalHeader().setMinimumSectionSize(44)
        self.niftyStockPrices.verticalHeader().setStretchLastSection(True)
        self.stockData.addTab(self.niftyTable, "")
        self.bankniftyTable = QtWidgets.QWidget()
        self.bankniftyTable.setObjectName("bankniftyTable")
        self.bankniftyStockPrices = QtWidgets.QTableWidget(self.bankniftyTable)
        self.bankniftyStockPrices.setGeometry(QtCore.QRect(30, 20, 671, 491))
        delegate = AlignDelegate(self.bankniftyStockPrices)
        self.bankniftyStockPrices.setItemDelegate(delegate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bankniftyStockPrices.sizePolicy().hasHeightForWidth())
        self.bankniftyStockPrices.setSizePolicy(sizePolicy)
        self.bankniftyStockPrices.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bankniftyStockPrices.setStyleSheet("")
        self.bankniftyStockPrices.setFrameShape(QtWidgets.QFrame.Panel)
        self.bankniftyStockPrices.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bankniftyStockPrices.setLineWidth(1)
        self.bankniftyStockPrices.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bankniftyStockPrices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bankniftyStockPrices.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.bankniftyStockPrices.setObjectName("bankniftyStockPrices")
        self.bankniftyStockPrices.setColumnCount(5)
        self.bankniftyStockPrices.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(10, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankniftyStockPrices.setItem(11, 4, item)
        self.bankniftyStockPrices.horizontalHeader().setVisible(True)
        self.bankniftyStockPrices.horizontalHeader().setCascadingSectionResizes(False)
        self.bankniftyStockPrices.horizontalHeader().setDefaultSectionSize(128)
        self.bankniftyStockPrices.horizontalHeader().setHighlightSections(True)
        self.bankniftyStockPrices.horizontalHeader().setMinimumSectionSize(128)
        self.bankniftyStockPrices.horizontalHeader().setSortIndicatorShown(False)
        self.bankniftyStockPrices.horizontalHeader().setStretchLastSection(False)
        self.bankniftyStockPrices.verticalHeader().setVisible(False)
        self.bankniftyStockPrices.verticalHeader().setCascadingSectionResizes(True)
        self.bankniftyStockPrices.verticalHeader().setDefaultSectionSize(44)
        self.bankniftyStockPrices.verticalHeader().setMinimumSectionSize(44)
        self.bankniftyStockPrices.verticalHeader().setStretchLastSection(True)
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
        item = self.niftyStockPrices.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.niftyStockPrices.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.niftyStockPrices.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.niftyStockPrices.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.niftyStockPrices.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.niftyStockPrices.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.niftyStockPrices.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.niftyStockPrices.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.niftyStockPrices.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.niftyStockPrices.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.niftyStockPrices.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Token no."))
        item = self.niftyStockPrices.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Stock Name"))
        item = self.niftyStockPrices.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Net CNG (%)"))
        item = self.niftyStockPrices.horizontalHeaderItem(3)
        item.setText(_translate("Form", "WM (%)"))
        item = self.niftyStockPrices.horizontalHeaderItem(4)
        item.setText(_translate("Form", "IC (%)"))
        __sortingEnabled = self.niftyStockPrices.isSortingEnabled()
        self.niftyStockPrices.setSortingEnabled(False)
        item = self.niftyStockPrices.item(0, 0)
        item.setText(_translate("Form", "2885"))
        item = self.niftyStockPrices.item(0, 1)
        item.setText(_translate("Form", "RELIANCE"))
        item = self.niftyStockPrices.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(1, 0)
        item.setText(_translate("Form", "1594"))
        item = self.niftyStockPrices.item(1, 1)
        item.setText(_translate("Form", "INFY"))
        item = self.niftyStockPrices.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(2, 0)
        item.setText(_translate("Form", "1333"))
        item = self.niftyStockPrices.item(2, 1)
        item.setText(_translate("Form", "HDFCBANK"))
        item = self.niftyStockPrices.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(3, 0)
        item.setText(_translate("Form", "4963"))
        item = self.niftyStockPrices.item(3, 1)
        item.setText(_translate("Form", "ICICIBANK"))
        item = self.niftyStockPrices.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(4, 0)
        item.setText(_translate("Form", "1330"))
        item = self.niftyStockPrices.item(4, 1)
        item.setText(_translate("Form", "HDFC"))
        item = self.niftyStockPrices.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(5, 0)
        item.setText(_translate("Form", "11536"))
        item = self.niftyStockPrices.item(5, 1)
        item.setText(_translate("Form", "TCS"))
        item = self.niftyStockPrices.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(6, 0)
        item.setText(_translate("Form", "11483"))
        item = self.niftyStockPrices.item(6, 1)
        item.setText(_translate("Form", "LT"))
        item = self.niftyStockPrices.item(6, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(6, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(6, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(7, 0)
        item.setText(_translate("Form", "1394"))
        item = self.niftyStockPrices.item(7, 1)
        item.setText(_translate("Form", "HINDUNILVR"))
        item = self.niftyStockPrices.item(7, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(7, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(7, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(8, 0)
        item.setText(_translate("Form", "1660"))
        item = self.niftyStockPrices.item(8, 1)
        item.setText(_translate("Form", "ITC"))
        item = self.niftyStockPrices.item(8, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(8, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(8, 4)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(9, 0)
        item.setText(_translate("Form", "1992"))
        item = self.niftyStockPrices.item(9, 1)
        item.setText(_translate("Form", "KOTAKBANK"))
        item = self.niftyStockPrices.item(9, 2)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(9, 3)
        item.setText(_translate("Form", "0"))
        item = self.niftyStockPrices.item(9, 4)
        item.setText(_translate("Form", "0"))
        self.niftyStockPrices.setSortingEnabled(__sortingEnabled)
        self.stockData.setTabText(self.stockData.indexOf(self.niftyTable), _translate("Form", "NIFTY"))
        item = self.bankniftyStockPrices.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.bankniftyStockPrices.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.bankniftyStockPrices.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.bankniftyStockPrices.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.bankniftyStockPrices.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.bankniftyStockPrices.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.bankniftyStockPrices.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.bankniftyStockPrices.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.bankniftyStockPrices.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.bankniftyStockPrices.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.bankniftyStockPrices.verticalHeaderItem(10)
        item.setText(_translate("Form", "11"))
        item = self.bankniftyStockPrices.verticalHeaderItem(11)
        item.setText(_translate("Form", "12"))
        item = self.bankniftyStockPrices.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Token no."))
        item = self.bankniftyStockPrices.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Stock Name"))
        item = self.bankniftyStockPrices.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Net CNG (%)"))
        item = self.bankniftyStockPrices.horizontalHeaderItem(3)
        item.setText(_translate("Form", "WM (%)"))
        item = self.bankniftyStockPrices.horizontalHeaderItem(4)
        item.setText(_translate("Form", "IC (%)"))
        __sortingEnabled = self.bankniftyStockPrices.isSortingEnabled()
        self.bankniftyStockPrices.setSortingEnabled(False)
        item = self.bankniftyStockPrices.item(0, 0)
        item.setText(_translate("Form", "1333"))
        item = self.bankniftyStockPrices.item(0, 1)
        item.setText(_translate("Form", "HDFCBANK"))
        item = self.bankniftyStockPrices.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(1, 0)
        item.setText(_translate("Form", "4963"))
        item = self.bankniftyStockPrices.item(1, 1)
        item.setText(_translate("Form", "ICICIBANK"))
        item = self.bankniftyStockPrices.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(2, 0)
        item.setText(_translate("Form", "1922"))
        item = self.bankniftyStockPrices.item(2, 1)
        item.setText(_translate("Form", "KOTAKBANK"))
        item = self.bankniftyStockPrices.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(3, 0)
        item.setText(_translate("Form", "5900"))
        item = self.bankniftyStockPrices.item(3, 1)
        item.setText(_translate("Form", "AXISBANK"))
        item = self.bankniftyStockPrices.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(4, 0)
        item.setText(_translate("Form", "3045"))
        item = self.bankniftyStockPrices.item(4, 1)
        item.setText(_translate("Form", "SBIN"))
        item = self.bankniftyStockPrices.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(5, 0)
        item.setText(_translate("Form", "5258"))
        item = self.bankniftyStockPrices.item(5, 1)
        item.setText(_translate("Form", "INDUSINBK"))
        item = self.bankniftyStockPrices.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(6, 0)
        item.setText(_translate("Form", "21238"))
        item = self.bankniftyStockPrices.item(6, 1)
        item.setText(_translate("Form", "AUBANK"))
        item = self.bankniftyStockPrices.item(6, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(6, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(6, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(7, 0)
        item.setText(_translate("Form", "2263"))
        item = self.bankniftyStockPrices.item(7, 1)
        item.setText(_translate("Form", "BANDHANBNK"))
        item = self.bankniftyStockPrices.item(7, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(7, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(7, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(8, 0)
        item.setText(_translate("Form", "1023"))
        item = self.bankniftyStockPrices.item(8, 1)
        item.setText(_translate("Form", "FEDERALBNK"))
        item = self.bankniftyStockPrices.item(8, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(8, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(8, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(9, 0)
        item.setText(_translate("Form", "11184"))
        item = self.bankniftyStockPrices.item(9, 1)
        item.setText(_translate("Form", "IDFCFIRSTB"))
        item = self.bankniftyStockPrices.item(9, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(9, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(9, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(10, 0)
        item.setText(_translate("Form", "10666"))
        item = self.bankniftyStockPrices.item(10, 1)
        item.setText(_translate("Form", "PNB"))
        item = self.bankniftyStockPrices.item(10, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(10, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(10, 4)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(11, 0)
        item.setText(_translate("Form", "18391"))
        item = self.bankniftyStockPrices.item(11, 1)
        item.setText(_translate("Form", "RBLBANK"))
        item = self.bankniftyStockPrices.item(11, 2)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(11, 3)
        item.setText(_translate("Form", "0"))
        item = self.bankniftyStockPrices.item(11, 4)
        item.setText(_translate("Form", "0"))
        self.bankniftyStockPrices.setSortingEnabled(__sortingEnabled)
        self.stockData.setTabText(self.stockData.indexOf(self.bankniftyTable), _translate("Form", "BANK NIFTY"))

        self.startMarket.clicked.connect(self.webSocketCall)
        self.stopMarket.clicked.connect(self.webSocketCall)

        i = 0
        self.onChange(i)
        self.stockData.currentChanged.connect(self.onChange)


    def threadMsg(self,message):        
        self.t2 = thread_with_trace(target = thread_with_trace.readData(self,message,self.niftyStockPrices,self.bankniftyStockPrices,self.niftyPrice,self.bankniftyPrice))
        self.t2.start()

    def onChange(self,i):
        
        if i == 0:
            # self.webSocketCall(self.niftyTokenTemp)
            self.token = self.niftyTokenTemp
            # print("aaaaa",self.token)

        if i == 1:
            # self.webSocketCall(self.bankniftyTokenTemp)
            self.token = self.bankniftyTokenTemp
            # print("bbbbb",self.token)

    def webSocketLmao(self):
        self.ss._on_open = lambda ws:self.ss.subscribe(self.task,self.token)
        self.ss._on_message = lambda ws,message:self.threadMsg(message)
        # self.ss._on_message = lambda ws,message:self.readData(message)
        self.ss._on_error = lambda ws,error:print(error)
        self.ss._on_close = lambda ws:print("Close")

        self.t1 = thread_with_trace(target = self.ss.connect)
        self.t1.start()

        
    def webSocketCall(self):
        if self.startMarket.isChecked():
            self.webSocketLmao()

        if self.stopMarket.isChecked():
            self.t1.kill()
            self.t2.kill()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Canis = QtWidgets.QWidget()
    ui = Ui_Canis()
    ui.setupUi(Canis)
    Canis.show()
    sys.exit(app.exec_())
