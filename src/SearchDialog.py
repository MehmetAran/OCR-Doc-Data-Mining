from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import os
from sqliteOperations import SqliteOperations
class SearchDialog(QDialog):
    
    def __init__(self, data,docName,*args, **kwargs):
        self.docName = docName
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Search user")
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setHorizontalHeaderLabels(("Verdiğiniz isim", "Soldaki Metin", "Sağdaki Metin", "Yukarıdaki Metin", "Aşağıdaki Metin"))

        self.btnEkle = QPushButton() 
        self.btnEkle.setText("Ekle")
        self.btnEkle.clicked.connect(self.selectedIndexAddToSqlite)
        layout.addWidget(self.btnEkle);

        self.btnSil = QPushButton() 
        self.btnSil.clicked.connect(self.selectedIndexDelete)
        self.btnSil.setText("Sil")
        layout.addWidget(self.btnSil);

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        self.searchstudent(data)


    def searchstudent(self,array):
        result = array
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def selectedIndexDelete(self):
        row = self.tableWidget.currentRow()
        if(row == ""):
            return
        self.tableWidget.removeRow(row)


    def selectedIndexAddToSqlite(self):
        row = self.tableWidget.currentRow()
        if(row == ""):
            return
        index0 = self.tableWidget.item(row,0).text()
        index1 = self.tableWidget.item(row,1).text()
        index2 = self.tableWidget.item(row,2).text()
        index3 = self.tableWidget.item(row,3).text()
        index4 = self.tableWidget.item(row,4).text()

        SqliteOperations().insert(self.docName,0,index0,index1,index2,index3,index4)
        self.tableWidget.removeRow(row)
