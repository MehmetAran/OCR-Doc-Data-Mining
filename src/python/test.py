import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import os

class MainPage(QDialog):

    def __init__(self):
        super(MainPage, self).__init__()
        basepath = os.path.abspath(".")
        loadUi(basepath+"/src/ui/Homepage.ui", self)
        # self.pushbutton_2.clicked.connect(self.retrieveText)
        self.btnNewDoc.clicked.connect(self.move)
        self.btnReadDoc.clicked.connect(self.readDoc)

    def move(self):
        from ui.OtherPage import SecondPage
        theClass = SecondPage()
        print(theClass)
        theClass.exec()

    def readDoc(self):
        from DocumentOperation import DocumentOperation
        readDocument = DocumentOperation()
        informations = readDocument.readDoc()
        
        for information1,information2 in zip(informations[0],informations[1]):
            print(information1,information2)


app = QApplication(sys.argv)    
widget = MainPage()
widget.show()
sys.exit(app.exec())
