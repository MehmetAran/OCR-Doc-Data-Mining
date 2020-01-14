# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnReadDoc = QtWidgets.QPushButton(Dialog)
        self.btnReadDoc.setGeometry(QtCore.QRect(110, 80, 161, 32))
        self.btnReadDoc.setObjectName("btnReadDoc")
        self.btnNewDoc = QtWidgets.QPushButton(Dialog)
        self.btnNewDoc.setGeometry(QtCore.QRect(110, 120, 161, 32))
        self.btnNewDoc.setObjectName("btnNewDoc")
        self.btnUpdDoc = QtWidgets.QPushButton(Dialog)
        self.btnUpdDoc.setGeometry(QtCore.QRect(110, 160, 161, 32))
        self.btnUpdDoc.setObjectName("btnUpdDoc")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnReadDoc.setText(_translate("Dialog", "Dokuman Okut"))
        self.btnNewDoc.setText(_translate("Dialog", "Yeni Dokuman Ekle"))
        self.btnUpdDoc.setText(_translate("Dialog", "Dokuman Guncelle"))


