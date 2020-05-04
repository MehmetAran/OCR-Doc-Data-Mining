import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import os

class SecondPage(QDialog):
    basePath = os.path.abspath('.')
    def __init__(self):
        super(SecondPage, self).__init__()
        loadUi(basePath+'/src/ui/SecondPage.ui', self)

        self.btnAddDoc.clicked.connect(self.SelectDoc)
        self.btnNewInfo.clicked.connect(self.NewPage)


    def SelectDoc(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def NewPage(self):
        from ui.Go import New
        newClass = New()
        print(newClass)
        newClass.exec()
