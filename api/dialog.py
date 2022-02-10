from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(420, 278)
        Error.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Error.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        Error.setMinimumSize(QtCore.QSize(420, 278))
        Error.setMaximumSize(QtCore.QSize(420, 278))
        font = QtGui.QFont()
        font.setPointSize(4)
        Error.setFont(font)
        Error.setStyleSheet("QDialog{background: #242222;border-radius: 15px;}")
        self.close = QtWidgets.QPushButton(Error)
        self.close.setGeometry(QtCore.QRect(200, 210, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Overpass")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close.setFont(font)
        self.close.setStyleSheet("*{width: 175px;height: 40px;background: #EB6868;border-radius: 7px;font-family: Overpass;font-style: normal;font-weight: bold;font-size: 15px;line-height: 19px;text-align: center;color: #0D0C0C;} QPushButton:hover{background: #954545;}")
        self.close.setObjectName("close")
        
        self.frame = QtWidgets.QFrame(Error)
        self.frame.setGeometry(QtCore.QRect(30, 70, 364, 121))
        self.frame.setStyleSheet("background: #DCDADA;border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.detailLabel = QtWidgets.QLabel(self.frame)
        self.detailLabel.setGeometry(QtCore.QRect(13, 13, 331, 21))
        self.detailLabel.setStyleSheet("font-family: Overpass;font-style: normal;font-weight: bold;font-size: 17px;line-height: 18px;")
        self.detailLabel.setObjectName("detailLabel")
        self.errorLabel = QtWidgets.QLabel(self.frame)
        self.errorLabel.setGeometry(QtCore.QRect(10, 40, 341, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setStyleSheet("*{font-family: Roboto;font-style: normal;font-size: 16px;color:red;line-height: 18px;}")
        self.errorLabel.setTextFormat(QtCore.Qt.RichText)
        self.errorLabel.setScaledContents(False)
        self.errorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.erroOccurred = QtWidgets.QLabel(Error)
        self.erroOccurred.setGeometry(QtCore.QRect(90, 30, 251, 31))
        self.erroOccurred.setStyleSheet("*{font-family: Overpass;font-style: normal;font-weight: bold;font-size: 21px;line-height: 27px;color: #FFFFFF;}")
        self.erroOccurred.setObjectName("erroOccurred")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error"))
        self.close.setText(_translate("Error", "CLOSE APPLICATION"))
        self.detailLabel.setText(_translate("Error", "The details of the error are as follows: "))
        self.erroOccurred.setText(_translate("Error", "AN ERROR OCCURRED"))
        self.close.clicked.connect(self.clickme)

    def errorMsg(self,errormsg):
        _translate = QtCore.QCoreApplication.translate
        self.errorLabel.setText(_translate("Error",errormsg))

    def clickme(self):
        self.close.clicked.connect(sysExit())

def sysExit():
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

def errorMain(errorMsg):
    app = QtWidgets.QApplication(sys.argv)
    Error = QtWidgets.QDialog()
    ui = Ui_Error()
    ui.setupUi(Error)
    Error.show()
    ui.errorMsg(errorMsg)
    sys.exit(app.exec_())
