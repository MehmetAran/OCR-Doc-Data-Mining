from PyQt5.QtWidgets import *
import sqlite3
import os
from sqliteOperations import SqliteOperations 



# Dokümanların listelendiği kısımda
# yeni bir veri eklemek için gerekli olan ui ve veri tabanı
# işlemleri burda gerçekleşir


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Ekle")

        self.setWindowTitle("Yeni Bir Satır Ekle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Eklenecek Veriler")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addDocumentIndex)

        layout = QVBoxLayout()

        self.docName = QLineEdit()
        self.docName.setPlaceholderText("Dokuman Adı")
        layout.addWidget(self.docName)


        self.indexName = QLineEdit()
        self.indexName.setPlaceholderText("İndex Adı")
        layout.addWidget(self.indexName)


        self.leftText = QLineEdit()
        self.leftText.setPlaceholderText("Solundaki metin")
        layout.addWidget(self.leftText)

        self.rightText = QLineEdit()
        self.rightText.setPlaceholderText("Sağındaki metin")
        layout.addWidget(self.rightText)
  
        
        self.topText = QLineEdit()
        self.topText.setPlaceholderText("Üstündeki metin")
        layout.addWidget(self.topText)
    
        self.bottomText = QLineEdit()
        self.bottomText.setPlaceholderText("Altındaki metin")
        layout.addWidget(self.bottomText)


        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addDocumentIndex(self):
        documentName = self.docName.text()
        indexName = self.indexName.text()
        leftText = self.leftText.text()
        rightText = self.rightText.text()
        topText = self.topText.text()
        bottomText = self.bottomText.text()
        SqliteOperations().insert(documentName,0,indexName,leftText,rightText,topText,bottomText)
        self.close()