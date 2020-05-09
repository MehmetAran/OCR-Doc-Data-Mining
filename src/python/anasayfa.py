# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from docOkut import Ui_MainWindow
from DocumentOperations2 import DocumentOperation 
import os
class Ui_DDVT(object):

    def readDoc(self):
        docOpr =DocumentOperation()
        docOpr.readDoc()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, DDVT):
        DDVT.setObjectName("DDVT")
        DDVT.setEnabled(True)
        DDVT.resize(689, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DDVT.sizePolicy().hasHeightForWidth())
        DDVT.setSizePolicy(sizePolicy)
        DDVT.setMinimumSize(QtCore.QSize(689, 428))
        DDVT.setMaximumSize(QtCore.QSize(689, 428))
        DDVT.setAcceptDrops(True)
        DDVT.setLayoutDirection(QtCore.Qt.LeftToRight)
        DDVT.setStyleSheet("background-color: rgb(255, 255, 255);")
        DDVT.setSizeGripEnabled(False)
        DDVT.setModal(False)
        self.frame = QtWidgets.QFrame(DDVT)
        self.frame.setGeometry(QtCore.QRect(0, 0, 191, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(22, 101, 193);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnDokumanEkle = QtWidgets.QPushButton(self.frame)
        self.btnDokumanEkle.setGeometry(QtCore.QRect(0, 150, 191, 41))
        self.btnDokumanEkle.setStyleSheet("background-color: rgb(25, 118, 211);\n"
"color: rgb(255, 255, 255);")
        self.btnDokumanEkle.setObjectName("btnDokumanEkle")
        self.btnDokumanAnaliz = QtWidgets.QPushButton(self.frame)
        self.btnDokumanAnaliz.setGeometry(QtCore.QRect(0, 189, 191, 41))
        self.btnDokumanAnaliz.setStyleSheet("background-color: rgb(25, 118, 211);\n"
"color: rgb(255, 255, 255);")

        self.btnDokumanEkle.clicked.connect(self.openWindow)
        self.btnDokumanAnaliz.clicked.connect(self.readDoc)

        self.btnDokumanAnaliz.setObjectName("btnDokumanAnaliz")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 229, 191, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(25, 118, 211);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 10, 141, 121))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        basepath = os.path.abspath(".")

        icon.addPixmap(QtGui.QPixmap(basepath+"/resources/img/logo_ddvt.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(141, 124))
        self.pushButton_5.setAutoRepeatDelay(0)
        self.pushButton_5.setAutoRepeatInterval(100)
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_2 = QtWidgets.QFrame(DDVT)
        self.frame_2.setGeometry(QtCore.QRect(190, 0, 501, 431))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 501, 151))
        self.frame_3.setStyleSheet("background-color: rgb(33, 153, 245);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 381, 81))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(60, 230, 111, 91))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setStyleSheet("background-color: rgb(131, 181, 255);")
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setAutoRepeatDelay(0)
        self.pushButton.setAutoRepeatInterval(0)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 230, 111, 91))
        self.pushButton_2.setStyleSheet("background-color: rgb(104, 154, 255);")
        self.pushButton_2.setAutoRepeatDelay(0)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 230, 111, 91))
        self.pushButton_4.setStyleSheet("background-color: rgb(100, 107, 255);")
        self.pushButton_4.setAutoRepeatDelay(0)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(DDVT)
        QtCore.QMetaObject.connectSlotsByName(DDVT)

    def retranslateUi(self, DDVT):
        _translate = QtCore.QCoreApplication.translate
        DDVT.setWindowTitle(_translate("DDVT", "DDVT"))
        self.btnDokumanEkle.setText(_translate("DDVT", "Dokuman Ekle"))
        self.btnDokumanAnaliz.setText(_translate("DDVT", "Dokuman Analiz"))
        self.pushButton_3.setText(_translate("DDVT", "Ayarlar"))
        self.label_2.setText(_translate("DDVT", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Buraya yazı eklenecek</span></p></body></html>"))
        self.pushButton.setText(_translate("DDVT", "Ne"))
        self.pushButton_2.setText(_translate("DDVT", "ekleyelim"))
        self.pushButton_4.setText(_translate("DDVT", "?"))
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DDVT = QtWidgets.QDialog()
    ui = Ui_DDVT()
    ui.setupUi(DDVT)
    DDVT.show()
    sys.exit(app.exec_())
