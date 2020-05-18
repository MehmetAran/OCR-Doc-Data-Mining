from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont
import datetime
import sqlite3
import os

class bookBorrow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookBorrow_layout = QGridLayout()
        self.setLayout(self.bookBorrow_layout)

        self.returnMain_button = QPushButton('Ana sayfaya dön')
        self.bookBorrow_layout.addWidget(self.returnMain_button, 0, 0, 1, 6)

        basePath = os.path.abspath('.')
        self.conn = sqlite3.connect(basePath+"/resource/db/sql.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        self.c.close()


        # self.book_number_label = QLabel('Kitap numarası')
        # self.bookBorrow_layout.addWidget(self.book_number_label, 2, 1, 1, 1)
        # self.book_number_label.setObjectName('bookBorrow_label')
        # self.book_number = QLineEdit()
        # self.bookBorrow_layout.addWidget(self.book_number, 2, 2, 1, 3)
        # self.book_number.setObjectName('bookBorrow_edit')

        # self.card_number_label = QLabel('Kütüphane kartı numarası')
        # self.bookBorrow_layout.addWidget(self.card_number_label, 3, 1, 1, 1)
        # self.card_number_label.setObjectName('bookBorrow_label')
        # self.card_number = QLineEdit()
        # self.bookBorrow_layout.addWidget(self.card_number, 3, 2, 1, 3)
        # self.card_number.setObjectName('bookBorrow_edit')

        # self.return_date_label = QLabel('Dönüş tarihi')
        # self.bookBorrow_layout.addWidget(self.return_date_label, 4, 1, 1, 1)
        # self.return_date_label.setObjectName('bookBorrow_label')
        # self.return_date = QLineEdit()
        # self.bookBorrow_layout.addWidget(self.return_date, 4, 2, 1, 3)
        # self.return_date.setObjectName('bookBorrow_edit')

        self.Borrow_button = QPushButton('Borrow')
        self.bookBorrow_layout.addWidget(self.Borrow_button, 5, 2, 1, 2)
        self.Borrow_button.setObjectName('bookBorrow_button')
        self.Borrow_button.clicked.connect(self.showTable)

        

        self.tableWidget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Döküman Adı", "Sayfa No", "Sem", "Mobile", "Address"))

        self.bookBorrow_layout.addWidget(self.tableWidget, 7, 1, 4, 4)
        # self.tableWidget.hide()


        # self.borrowRecord_table = QTableWidget()
        # self.bookBorrow_layout.addWidget(self.borrowRecord_table, 7, 1, 4, 4)
        # self.borrowRecord_table.hide()

        self.label = QLabel('Kitap ödünç al')
        self.label.setObjectName('bookBorrow_title')
        self.bookBorrow_layout.addWidget(self.label, 11, 4, 2, 2)

    

    def showTable(self, cursor):
        '''
        Kullanıcılar tarafından ödünç alınan kitapları görüntüle
        '''
        
        QMessageBox.information(self, 'Sorgu başarılı oldu ',' veriler yükleniyor', QMessageBox.Ok)
        if QMessageBox.Ok:
            self.tableWidget.show()
            basePath = os.path.abspath(".")
            self.connection = sqlite3.connect(basePath+"/resource/db/database.db")
            query = "SELECT * FROM students"
            result = self.connection.execute(query)
            self.tableWidget.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
           
            self.connection.close()

    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için,
        stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
