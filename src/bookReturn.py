from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont
from sqliteOperations import SqliteOperations
import os
from shutil import copyfile
class bookReturn(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookReturn_layout = QGridLayout()
        self.setLayout(self.bookReturn_layout)

        self.returnMain_button = QPushButton('Anasayfaya dön')
        self.bookReturn_layout.addWidget(self.returnMain_button, 0, 0, 1, 6)

        self.documentNameLabel = QLabel('Eşleşecek Belgenin Adı')
        self.bookReturn_layout.addWidget(self.documentNameLabel, 2, 1, 1, 1)
        self.documentNameLabel.setObjectName('bookReturn_label')
        
        self.documentNameText = QLineEdit()
        self.bookReturn_layout.addWidget(self.documentNameText, 2, 2, 1, 3)
        self.documentNameText.setObjectName('bookReturn_edit')        
     

        self.addToSqlBtn = QPushButton('Ekle')
        self.bookReturn_layout.addWidget(self.addToSqlBtn, 4, 2, 1, 2)
        self.addToSqlBtn.setObjectName('bookReturn_button')
        self.addToSqlBtn.clicked.connect(self.addTargetDocumentToSqlite)

        self.selectDocumentPath = QPushButton('Döküman Seç')
        self.bookReturn_layout.addWidget(self.selectDocumentPath, 4, 4, 1, 2)
        self.selectDocumentPath.setObjectName('bookReturn_button')
        self.selectDocumentPath.clicked.connect(self.chooseFile)


        

        self.record_label = QLabel('')
        self.bookReturn_layout.addWidget(self.record_label, 5, 2, 1, 2)
        self.record_label.setObjectName('bookBorrow_already')

        """
        self.label = QLabel('')
        self.label.setObjectName('bookReturn_title')
        self.bookReturn_layout.addWidget(self.label, 10, 4, 2, 2)"""

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