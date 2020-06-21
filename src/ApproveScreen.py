from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import os
from sqliteOperations import SqliteOperations

# Belgeyi kırpma işleminden sonra bu class 
# belgeden alınan ve veritabanına kaydedilecek olan verileri
# kullanıcı onayına sunar ve onaylanan belgeleri ekler.
# Kullanıcı isterse güncelleme yapılır.

class ApproveScreen(QDialog):
    
    def __init__(self, data,docName,*args, **kwargs):
        self.docName = docName
        super(ApproveScreen, self).__init__(*args, **kwargs)
        self.setWindowTitle("Onaylama İşlemi")
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        layout = QVBoxLayout()
        self.approve_screen_table_widget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.approve_screen_table_widget.setAlternatingRowColors(True)
        self.approve_screen_table_widget.setColumnCount(5)
        self.approve_screen_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.approve_screen_table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.approve_screen_table_widget.horizontalHeader().setStretchLastSection(True)
        self.approve_screen_table_widget.verticalHeader().setVisible(False)
        self.approve_screen_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.approve_screen_table_widget.setHorizontalHeaderLabels(("Verdiğiniz isim", "Soldaki Metin", "Sağdaki Metin", "Yukarıdaki Metin", "Aşağıdaki Metin"))

        self.add_btn = QPushButton() 
        self.add_btn.setText("Ekle")
        self.add_btn.clicked.connect(self.selectedIndexAddToSqlite)
        layout.addWidget(self.add_btn);

        self.delete_btn = QPushButton() 
        self.delete_btn.clicked.connect(self.selectedIndexDelete)
        self.delete_btn.setText("Sil")
        layout.addWidget(self.delete_btn);

        layout.addWidget(self.approve_screen_table_widget)
        self.setLayout(layout)
        self.searchstudent(data)


    def searchstudent(self,array):
        result = array
        self.approve_screen_table_widget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.approve_screen_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.approve_screen_table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def selectedIndexDelete(self):
        row = self.approve_screen_table_widget.currentRow()
        if(row == ""):
            return
        self.approve_screen_table_widget.removeRow(row)


    def selectedIndexAddToSqlite(self):
        row = self.approve_screen_table_widget.currentRow()
        if(row == ""):
            return
        index0 = self.approve_screen_table_widget.item(row,0).text()
        index1 = self.approve_screen_table_widget.item(row,1).text()
        index2 = self.approve_screen_table_widget.item(row,2).text()
        index3 = self.approve_screen_table_widget.item(row,3).text()
        index4 = self.approve_screen_table_widget.item(row,4).text()

        SqliteOperations().insert(self.docName,0,index0,index1,index2,index3,index4)
        self.approve_screen_table_widget.removeRow(row)
