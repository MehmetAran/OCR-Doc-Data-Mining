from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont
from sqliteOperations import SqliteOperations
import os
import sqlite3
from sqliteOperations import SqliteOperations
from shutil import copyfile

# Dokümanları ve dokümandaki verilerin aktarılacağı belgeyi eşleştirdiğimiz yer.


class PairDocuments(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.pair_doc_layout = QGridLayout()
        self.setLayout(self.pair_doc_layout)

        self.returnMain_button = QPushButton('Anasayfaya dön')
        self.pair_doc_layout.addWidget(self.returnMain_button, 0, 0, 1, 6)

        self.documentNameLabel = QLabel('Eşleşecek Belgenin Adı')
        self.pair_doc_layout.addWidget(self.documentNameLabel, 2, 1, 1, 1)
        self.documentNameLabel.setObjectName('bookReturn_label')
        
        self.documentNameText = QLineEdit()
        self.pair_doc_layout.addWidget(self.documentNameText, 2, 2, 1, 3)
        self.documentNameText.setObjectName('bookReturn_edit')        
        

        self.addToSqlBtn = QPushButton('Ekle')
        self.pair_doc_layout.addWidget(self.addToSqlBtn, 4, 2, 1, 2)
        self.addToSqlBtn.setObjectName('bookReturn_button')
        self.addToSqlBtn.clicked.connect(self.addTargetDocumentToSqlite)

        self.selectDocumentPath = QPushButton('Dokuman Seç')
        self.pair_doc_layout.addWidget(self.selectDocumentPath, 4, 4, 1, 2)
        self.selectDocumentPath.setObjectName('bookReturn_button')
        self.selectDocumentPath.clicked.connect(self.chooseFile)

    

        

        self.record_label = QLabel('')
        self.pair_doc_layout.addWidget(self.record_label, 5, 2, 1, 2)
        self.record_label.setObjectName('bookBorrow_already')

        self.tableWidget = QTableWidget()
        #self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Doküman Adı", "Hedef Doküman"))

        self.pair_doc_layout.addWidget(self.tableWidget,6, 1, 1, 3)

        self.Borrow_button = QPushButton('Dokümanları Getir')
        self.pair_doc_layout.addWidget(self.Borrow_button, 5, 2, 1, 2)
        self.Borrow_button.setObjectName('bookBorrow_button')
        self.Borrow_button.clicked.connect(self.showTable)


        self.getSelectedDocumentsBtn = QPushButton('Güncelle')
        self.pair_doc_layout.addWidget(self.getSelectedDocumentsBtn, 5, 1, 1, 1)
        self.getSelectedDocumentsBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.updateAtIndexSQLiteAndTable)


        self.getSelectedDocumentsBtn = QPushButton('Sil')
        self.pair_doc_layout.addWidget(self.getSelectedDocumentsBtn, 5, 4, 1, 1)
        self.getSelectedDocumentsBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.deleteAtIndexSQLiteAndTable)
        

        

        self.label = QLabel('')
        self.label.setObjectName('bookReturn_title')
        self.pair_doc_layout.addWidget(self.label, 10, 4, 2, 2)

    def addTargetDocumentToSqlite(self):
        if(self.fname == ""):
            return
        if(self.documentNameText.text() == ""):
            return 
        print(self.documentNameText.text()," : ",self.documentNameText.text())
        SqliteOperations().insertTargetDocument(self.documentNameText.text(),self.fname)

        ## dosyayı kopyala txt-docs klasörüne
        basePath = os.path.abspath('.')
        print("filePath",self.filePath)
        self.copy(self.filePath,basePath+"/resource/txt-docs")
    
    def copy(self,src, dst):
        if os.path.isdir(dst):
            dst = os.path.join(dst.encode('utf-8'), os.path.basename(src).encode('utf-8'))
            copyfile(src,dst)

    def chooseFile(self):
        self.filePath = QFileDialog.getOpenFileName(
        self, 'Belge seçme işlemi', './', 'Text(*.txt)')
        self.filePath = self.filePath[0]
        dirname = os.path.dirname(self.filePath)
        self.fname = self.filePath.replace(dirname+'/',"")
        print(self.fname)
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)    

    def showTable(self, cursor):
        
        #QMessageBox.information(self, 'Sorgu başarılı oldu ',' veriler yükleniyor', QMessageBox.Ok)
        if QMessageBox.Ok:
            self.tableWidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/sql.db")
            query = "SELECT * FROM TargetDocuments"
            result = self.connection.execute(query).fetchall()
            self.tableWidget.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
           
            self.connection.close()

    def deleteAtIndexSQLiteAndTable(self):
        row = self.tableWidget.currentRow()
        index0 = self.tableWidget.item(row,0).text()
        SqliteOperations().deleteFromTargetDocuments(index0)

        self.tableWidget.removeRow(row)
    def updateAtIndexSQLiteAndTable(self):
        row = self.tableWidget.currentRow()
        if(row == ""):
            return
        index0 = self.tableWidget.item(row,0).text()
        index1 = self.tableWidget.item(row,1).text()
        index2 = self.tableWidget.item(row,2).text()

        SqliteOperations().updateFromTargetDocuments(index0,index1,index2)


