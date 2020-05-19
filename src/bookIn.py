from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QStyleOption, QStyle, QToolButton, QTextEdit, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import os
from DocumentOperations import DocumentOperation 
import printer
from sqliteOperations import SqliteOperations
from shutil import copyfile
import datetime

class bookIn(QWidget):
    '''
    Kitap depolama arayüzü
    '''

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookIn_layout = QGridLayout()  #  Izgara düzeni nesnesi oluşturma 2
        self.setLayout(self.bookIn_layout)  #  Izgara düzeni için sağ taraftaki arayüz 2 düzenini ayarlayın
       
        self.returnMain_button = QPushButton()  #  Arayüz atlama için bir tane ekleyin
        self.returnMain_button.setText('Ana sayfaya dön')
        self.bookIn_layout.addWidget(self.returnMain_button, 0, 0, 1, 7)

        self.book_number_label = QLabel('Dokuman Adı')
        self.bookIn_layout.addWidget(self.book_number_label, 2, 1, 1, 1)
        self.book_number_label.setObjectName('lblDokumanAdı')
        
        self.book_number = QLineEdit()
        self.bookIn_layout.addWidget(self.book_number, 2, 2, 1, 3)

        self.btnDocNameEkle = QPushButton()
        self.btnDocNameEkle.setText('Ekle')
        self.bookIn_layout.addWidget(self.btnDocNameEkle, 2, 5, 1, 1)

        # Tekil depolama
        self.bookIn_single = QToolButton()
        self.bookIn_single.setText('Belge Sec')
        self.bookIn_single.setObjectName('bookInLibrary')
        self.bookIn_single.setIcon(
            QtGui.QIcon('./img/bookinlibrary_single.png'))
        self.bookIn_single.setIconSize(QtCore.QSize(150, 150))
        self.bookIn_single.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.bookIn_single, 3, 1, 2, 2)

        # Kitap depolama
        self.bookIn_multi = QToolButton()
        self.bookIn_multi.setText('Hedef Dokuman Sec')
        self.bookIn_multi.setObjectName('bookInLibrary')
        basePath = os.path.abspath('.')
        self.bookIn_multi.setIcon(
            QtGui.QIcon(basePath+'/resource/img/bookinlibrary_multi.png'))
        self.bookIn_multi.setIconSize(QtCore.QSize(150, 150))
        self.bookIn_multi.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.bookIn_multi, 3, 4, 2, 2)

        # Kitap saklama sayfası seçimi
        self.bookIn_label = QLabel('Dokuman Tanıt')
        self.bookIn_label.setObjectName('bookInLibrary_label')
        self.bookIn_layout.addWidget(self.bookIn_label, 5, 5, 1, 2)
    

    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için, stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)




class multiBookIn(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.multiBookIn_layout = QGridLayout()
        self.setLayout(self.multiBookIn_layout)

        # Kitap depolama arayüzüne dönmek için düğme
        self.return_button = QPushButton('Önceki arayüze dön')
        self.multiBookIn_layout.addWidget(self.return_button, 0, 0, 1, 6)

        # Alan genişletme için yay etiketi
        # self.space_label1 = QLabel()
        # self.multiBookIn_layout.addWidget(self.space_label1, 1, 0, 1, 6)
        # self.space_label1.setObjectName('multiBookIn_spaceLabel1')

        # self.bookDataEdit = QTextEdit()
        # self.bookDataEdit.setObjectName('textEdit')
        # self.data = self.bookDataEdit.toPlainText()  # Metin kutusundaki içeriği döndürür
        # self.multiBookIn_layout.addWidget(self.bookDataEdit, 2, 1, 4, 4)

        self.chooseFile_button = QPushButton('Dosya seç')
        self.chooseFile_button.setObjectName('chooseFile')
        self.multiBookIn_layout.addWidget(self.chooseFile_button, 7, 1, 1, 2)
        self.chooseFile_button.clicked.connect(self.readDoc)

        # self.submit_button = QPushButton('Sunum')
        # self.submit_button.setObjectName('submit')
        # self.multiBookIn_layout.addWidget(self.submit_button, 7, 3, 1, 2)
        # self.submit_button.clicked.connect(self.submit)

        # Alan genişletme için yay etiketi
        # self.space_label2 = QLabel()
        # self.multiBookIn_layout.addWidget(self.space_label2, 8, 0, 2, 6)
        # self.space_label2.setObjectName('multiBookIn_spaceLabel2')


        # self.label = QLabel('Çok kitaplı depolama')
        # self.label.setObjectName('multiBookIn_title')
        # self.multiBookIn_layout.addWidget(self.label, 9, 4, 2, 2)

    def readDoc(self):
       
        fname = QFileDialog.getOpenFileName(
            self, 'Belge okut', './', 'Pdf(*.pdf)')
        filePath = fname[0]

        folder = QFileDialog.getExistingDirectory(
            self, 'Hedef Klasör Seç', './', QFileDialog.ShowDirsOnly
                                                | QFileDialog.DontResolveSymlinks)

        print("folderPath : ",folder)

        if(folder != ""):
            docOpr =DocumentOperation()
            results = docOpr.readDoc(filePath)
            basePath = os.path.abspath('.')
            for result in results:
                print("*******************************")
                # Belge isminden TargetDocuments  tablosuna istek atılacak
                #Eğer eşleşen varsa o dosyayı printer ile yazdıracak
                targetDocument = ""
                try :
                    targetDocumentInformations = SqliteOperations().findByDocumentNameFromTargetDocuments(result[0][0])
                    targetDocument = targetDocumentInformations[2]
                    print(targetDocument)
                except:
                    QMessageBox.information(self, 'hata ','hata ', QMessageBox.Ok)
                    break
                self.copy(basePath+'/resource/txt-docs/'+targetDocument,folder)
                print("Belge ismi : " , result[0][0])
                for r in result : 
                    print(r[1] ," : ", r[2])
                    path = folder+'/' + targetDocument
                    pattern = "@@"+ r[1]
                    subst = r[2]
                    printer.replaceText(path,pattern,subst)
                path = folder+'/' + targetDocument
                now = str(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")).replace(' ','').replace(':','')
                newPath = folder +'/'+now+'.txt'
                os.rename(path,newPath)
                print(newPath)
        QMessageBox.information(self, 'İşlem bitti',' işlem bitti', QMessageBox.Ok)


    def copy(self,src, dst):
        if os.path.isdir(dst):
            dst = os.path.join(dst.encode('utf-8'), os.path.basename(src).encode('utf-8'))
            copyfile(src,dst)



    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için,
        stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
