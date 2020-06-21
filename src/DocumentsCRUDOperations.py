from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont
import datetime
import sqlite3
import os
from sqliteOperations import SqliteOperations
from InsertDialog import InsertDialog

# Dokümanlar ile ilgili CRUD veri tabanı işlemlerinin 
# bir arayüz yardımıyla gerçekleştirildi class.

class DocumentCRUDOperations(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.doc_layout = QGridLayout()
        self.setLayout(self.doc_layout)

        self.returnMain_button = QPushButton('Ana sayfaya dön')
        self.doc_layout.addWidget(self.returnMain_button, 0, 0, 1, 8)

        self.fetch_all_doc_button = QPushButton('Dokümanları Getir')
        self.doc_layout.addWidget(self.fetch_all_doc_button, 5, 2, 1, 2)
        self.fetch_all_doc_button.setObjectName('bookfetch_all_doc_button')
        self.fetch_all_doc_button.clicked.connect(self.showTable)


        self.getSelectedDocumentsBtn = QPushButton('Güncelle')
        self.doc_layout.addWidget(self.getSelectedDocumentsBtn, 5, 2, 2, 2)
        self.getSelectedDocumentsBtn.setObjectName('bookfetch_all_doc_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.updateAtIndexSQLiteAndTable)

        self.getSelectedDocumentsBtn = QPushButton('Eleman Ekle')
        self.doc_layout.addWidget(self.getSelectedDocumentsBtn, 5, 4, 1, 1)
        self.getSelectedDocumentsBtn.setObjectName('bookfetch_all_doc_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.addNewDocumentToSQLiteAndRefreshTable)

        self.getSelectedDocumentsBtn = QPushButton('Sil')
        self.doc_layout.addWidget(self.getSelectedDocumentsBtn, 5, 2, 3, 2)
        self.getSelectedDocumentsBtn.setObjectName('bookfetch_all_doc_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.deleteAtIndexSQLiteAndTable)

        
        self.textForSearch = QLineEdit()
        self.doc_layout.addWidget(self.textForSearch, 3, 3, 1, 2)
        self.textForSearch.setObjectName('bookBorrow_edit')

        self.getSelectedDocumentsWithSelectedTextBtn = QPushButton('Ara')
        self.doc_layout.addWidget(self.getSelectedDocumentsWithSelectedTextBtn, 3, 3, 2, 3)
        self.getSelectedDocumentsWithSelectedTextBtn.setObjectName('bookfetch_all_doc_button')
        self.getSelectedDocumentsWithSelectedTextBtn.clicked.connect(self.getDataWithLike)


        self.documents_tablewidget = QTableWidget()
        # self.setCentralWidget(self.documents_tablewidget)
        self.documents_tablewidget.setAlternatingRowColors(True)
        self.documents_tablewidget.setColumnCount(8)
        self.documents_tablewidget.horizontalHeader().setCascadingSectionResizes(False)
        self.documents_tablewidget.horizontalHeader().setSortIndicatorShown(False)
        self.documents_tablewidget.horizontalHeader().setStretchLastSection(True)
        self.documents_tablewidget.verticalHeader().setVisible(False)
        self.documents_tablewidget.verticalHeader().setCascadingSectionResizes(False)
        self.documents_tablewidget.verticalHeader().setStretchLastSection(False)
        self.documents_tablewidget.setHorizontalHeaderLabels(("Id", "Döküman Adı", "Sayfa No", "Verilen İsim", "Soldaki Metin", "Sağdaki Metin",
        "Üstündeki Metin","Altındaki Metin"))

        self.doc_layout.addWidget(self.documents_tablewidget, 7, 1, 4, 7)


        #Sağ altta bulunan ve ekranı dengelemek için yazdığımız boş label
        self.DONT_HANDLE_LBL_JUST_NOW = QLabel('')
        self.DONT_HANDLE_LBL_JUST_NOW.setObjectName('bookBorrow_title')
        self.doc_layout.addWidget(self.DONT_HANDLE_LBL_JUST_NOW, 11, 4, 2, 2)

    

    def showTable(self, cursor):
        if QMessageBox.Ok:
            self.documents_tablewidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/sql.db")
            query = "SELECT * FROM Documents"
            result = self.connection.execute(query).fetchall()
            self.documents_tablewidget.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.documents_tablewidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.documents_tablewidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
           
            self.connection.close()




    def deleteAtIndexSQLiteAndTable(self):
        row = self.documents_tablewidget.currentRow()
        index0 = self.documents_tablewidget.item(row,0).text()
        SqliteOperations().delete(index0)

        self.documents_tablewidget.removeRow(row)

    def addNewDocumentToSQLiteAndRefreshTable(self,cursor):
        InsertDialog().exec_()  
        self.showTable(cursor)

    def updateAtIndexSQLiteAndTable(self):
        row = self.documents_tablewidget.currentRow()
        if(row == ""):
            return
        index0 = self.documents_tablewidget.item(row,0).text()
        index1 = self.documents_tablewidget.item(row,1).text()
        index2 = self.documents_tablewidget.item(row,2).text()
        index3 = self.documents_tablewidget.item(row,3).text()
        index4 = self.documents_tablewidget.item(row,4).text()
        index5 = self.documents_tablewidget.item(row,5).text()
        index6 = self.documents_tablewidget.item(row,6).text()
        index7 = self.documents_tablewidget.item(row,7).text()

        SqliteOperations().update(index0,index1,index2,index3,index4,index5,index6,index7)



    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
    
    def getDataWithLike(self):
        if QMessageBox.Ok:
            self.documents_tablewidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/sql.db")
            self.cursor = self.connection.cursor()
            result = self.cursor.execute("select * from Documents where documentName like ? ",
                                                                            ('%'+self.textForSearch.text()+'%',))


         

            self.documents_tablewidget.setRowCount(0)
            print(result)
            for row_number, row_data in enumerate(result):
                self.documents_tablewidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.documents_tablewidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
           
            self.connection.close()
        