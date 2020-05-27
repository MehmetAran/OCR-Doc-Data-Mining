from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont
import datetime
import sqlite3
import os
from sqliteOperations import SqliteOperations
from InsertDialog import InsertDialog
class bookBorrow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookBorrow_layout = QGridLayout()
        self.setLayout(self.bookBorrow_layout)

        self.returnMain_button = QPushButton('Ana sayfaya dön')
        self.bookBorrow_layout.addWidget(self.returnMain_button, 0, 0, 1, 8)

       




        self.Borrow_button = QPushButton('Dökümanları Getir')
        self.bookBorrow_layout.addWidget(self.Borrow_button, 5, 2, 1, 2)
        self.Borrow_button.setObjectName('bookBorrow_button')
        self.Borrow_button.clicked.connect(self.showTable)


        self.getSelectedDocumentsBtn = QPushButton('Güncelle')
        self.bookBorrow_layout.addWidget(self.getSelectedDocumentsBtn, 5, 2, 2, 2)
        self.getSelectedDocumentsBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.updateAtIndexSQLiteAndTable)

        self.getSelectedDocumentsBtn = QPushButton('Eleman Ekle')
        self.bookBorrow_layout.addWidget(self.getSelectedDocumentsBtn, 5, 4, 1, 1)
        self.getSelectedDocumentsBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.addNewDocumentToSQLiteAndRefreshTable)

        self.getSelectedDocumentsBtn = QPushButton('Sil')
        self.bookBorrow_layout.addWidget(self.getSelectedDocumentsBtn, 5, 2, 3, 2)
        self.getSelectedDocumentsBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsBtn.clicked.connect(self.deleteAtIndexSQLiteAndTable)

        
        self.textForSearch = QLineEdit()
        self.bookBorrow_layout.addWidget(self.textForSearch, 3, 3, 1, 2)
        self.textForSearch.setObjectName('bookBorrow_edit')

        self.getSelectedDocumentsWithSelectedTextBtn = QPushButton('Ara')
        self.bookBorrow_layout.addWidget(self.getSelectedDocumentsWithSelectedTextBtn, 3, 3, 2, 3)
        self.getSelectedDocumentsWithSelectedTextBtn.setObjectName('bookBorrow_button')
        self.getSelectedDocumentsWithSelectedTextBtn.clicked.connect(self.getDataWithLike)


        self.tableWidget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Döküman Adı", "Sayfa No", "Verilen İsim", "Soldaki Metin", "Sağdaki Metin",
        "Üstündeki Metin","Altındaki Metin"))

        self.bookBorrow_layout.addWidget(self.tableWidget, 7, 1, 4, 7)
        # self.tableWidget.hide()


        # self.borrowRecord_table = QTableWidget()
        # self.bookBorrow_layout.addWidget(self.borrowRecord_table, 7, 1, 4, 4)
        # self.borrowRecord_table.hide()

        self.label = QLabel('')
        self.label.setObjectName('bookBorrow_title')
        self.bookBorrow_layout.addWidget(self.label, 11, 4, 2, 2)

    

    def showTable(self, cursor):
        '''
        Kullanıcılar tarafından ödünç alınan kitapları görüntüle
        '''
        
        #QMessageBox.information(self, 'Sorgu başarılı oldu ',' veriler yükleniyor', QMessageBox.Ok)
        if QMessageBox.Ok:
            self.tableWidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/sql.db")
            query = "SELECT * FROM Documents"
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
        SqliteOperations().delete(index0)

        self.tableWidget.removeRow(row)


        
        

    def addNewDocumentToSQLiteAndRefreshTable(self,cursor):
        InsertDialog().exec_()  
        self.showTable(cursor)

    def updateAtIndexSQLiteAndTable(self):
        row = self.tableWidget.currentRow()
        if(row == ""):
            return
        index0 = self.tableWidget.item(row,0).text()
        index1 = self.tableWidget.item(row,1).text()
        index2 = self.tableWidget.item(row,2).text()
        index3 = self.tableWidget.item(row,3).text()
        index4 = self.tableWidget.item(row,4).text()
        index5 = self.tableWidget.item(row,5).text()
        index6 = self.tableWidget.item(row,6).text()
        index7 = self.tableWidget.item(row,7).text()

        SqliteOperations().update(index0,index1,index2,index3,index4,index5,index6,index7)



    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için,
        stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
    
    def getDataWithLike(self):
        if QMessageBox.Ok:
            self.tableWidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/sql.db")
            self.cursor = self.connection.cursor()
            result = self.cursor.execute("select * from Documents where documentName like ? ",
                                                                            ('%'+self.textForSearch.text()+'%',))

            self.tableWidget.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
           
            self.connection.close()
        