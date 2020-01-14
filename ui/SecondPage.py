# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnAddDoc = QtWidgets.QPushButton(Dialog)
        self.btnAddDoc.setGeometry(QtCore.QRect(260, 240, 113, 32))
        self.btnAddDoc.setObjectName("btnAddDoc")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(120, 40, 146, 131))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btnNewInfo = QtWidgets.QPushButton(self.splitter)
        self.btnNewInfo.setObjectName("btnNewInfo")
        self.txtOgrenciName = QtWidgets.QLineEdit(self.splitter)
        self.txtOgrenciName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtOgrenciName.setAlignment(QtCore.Qt.AlignCenter)
        self.txtOgrenciName.setObjectName("txtOgrenciName")
        self.txtDanismanBilgileri = QtWidgets.QLineEdit(self.splitter)
        self.txtDanismanBilgileri.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDanismanBilgileri.setObjectName("txtDanismanBilgileri")
        self.txtOgrenciNo = QtWidgets.QLineEdit(self.splitter)
        self.txtOgrenciNo.setAlignment(QtCore.Qt.AlignCenter)
        self.txtOgrenciNo.setDragEnabled(False)
        self.txtOgrenciNo.setPlaceholderText("ogrenci no")
        self.txtOgrenciNo.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txtOgrenciNo.setObjectName("txtOgrenciNo")
        self.txtOgrenciBolum = QtWidgets.QLineEdit(self.splitter)
        self.txtOgrenciBolum.setAlignment(QtCore.Qt.AlignCenter)
        self.txtOgrenciBolum.setObjectName("txtOgrenciBolum")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnAddDoc.setText(_translate("Dialog", "Belge Ekle"))
        self.btnNewInfo.setText(_translate("Dialog", "Yeni bir bilgi ekle"))
        self.txtOgrenciName.setText(_translate("Dialog", "Ogrenci isim"))
        self.txtDanismanBilgileri.setText(_translate("Dialog", "Danisman Bilgileri"))
        self.txtOgrenciNo.setText(_translate("Dialog", "Ogrenci No"))
        self.txtOgrenciBolum.setText(_translate("Dialog", "Ogrenci Bolum"))
