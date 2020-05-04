from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys



def addNewFeature():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Yeni eleman ekle")
    flo = QFormLayout()
    
    name = QLineEdit()
    name.setFont(QFont("Thoma",20))
    flo.addRow("<font size= '20' color='red' >İsim", name)


    top = QLineEdit()
    top.setFont(QFont("Thoma",20))
    flo.addRow("<font size= '20' color='red' >Üst Etiket", top)

    left = QLineEdit()
    left.setFont(QFont("Thoma",20))
    flo.addRow("<font size= '20' color='red' >Sol Etiket", left)

    right = QLineEdit()
    right.setFont(QFont("Thoma",20))
    flo.addRow("<font size= '20' color='red' >Sağ Etiket", right)

    bottom = QLineEdit()
    bottom.setFont(QFont("Thoma",20))
    flo.addRow("<font size= '20' color='red' >Alt Etiket", bottom)


    isSingleLine = QCheckBox("Bilgi Tek Satırlık")
    isSingleLine.setFont(QFont("Thoma",10))
    isSingleLine.setStyleSheet("color: black")
    flo.addRow("", isSingleLine)

    addButton = QPushButton("Ekle")
    addButton.setFont(QFont("Thoma",20))
    addButton.setStyleSheet("color: red")

    
    def saveValues():
        values = []
        values.append(name.text())
        values.append(top.text())
        values.append(left.text())
        values.append(right.text())
        values.append(bottom.text())
        values.append(isSingleLine.isChecked())
        for value in values:
            print(value)

    addButton.clicked.connect(saveValues)
    flo.addRow("", addButton)


    win.setLayout(flo)
    win.show()

    app.exec_()


addNewFeature()