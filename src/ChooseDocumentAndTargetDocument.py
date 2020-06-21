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


# Doküman tanıtma işlemleri bu class ile gerçekleşir.

class ChoseDocument(QWidget):
  

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.choose_document_layout = QGridLayout()  
        self.setLayout(self.choose_document_layout)  
       
        self.returnMain_button = QPushButton()  
        self.returnMain_button.setText('Ana sayfaya dön')
        self.choose_document_layout.addWidget(self.returnMain_button, 0, 0, 1, 7)
        

        self.choose_doc_tool_btn = QToolButton()
        self.choose_doc_tool_btn.setText('Belge Sec')
        self.choose_doc_tool_btn.setObjectName('bookInLibrary')
        self.choose_doc_tool_btn.setIcon(
            QtGui.QIcon('./img/bookinlibrary_single.png'))
        self.choose_doc_tool_btn.setIconSize(QtCore.QSize(150, 150))
        self.choose_doc_tool_btn.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.choose_document_layout.addWidget(self.choose_doc_tool_btn, 3, 1, 2, 2)

        self.choose_target_doc_tool_btn = QToolButton()
        self.choose_target_doc_tool_btn.setText('Hedef Dokuman Sec')
        self.choose_target_doc_tool_btn.setObjectName('bookInLibrary')
        basePath = os.path.abspath('.')
        self.choose_target_doc_tool_btn.setIcon(
            QtGui.QIcon(basePath+'/resource/img/bookinlibrary_multi.png'))
        self.choose_target_doc_tool_btn.setIconSize(QtCore.QSize(150, 150))
        self.choose_target_doc_tool_btn.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.choose_document_layout.addWidget(self.choose_target_doc_tool_btn, 3, 4, 2, 2)

     
        self.buttom_title_lable = QLabel('Dokuman Tanıt')
        self.buttom_title_lable.setObjectName('bookInLibrary_label')
        self.choose_document_layout.addWidget(self.buttom_title_lable, 5, 5, 1, 2)
    

    def paintEvent(self, event):
  
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)



# Daha önceden tanımlanan bir belgeden veri alınır ve seçilen dokümana atılır.

class ChooseTargetDocument(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.choose_target_doc_layout = QGridLayout()
        self.setLayout(self.choose_target_doc_layout)

        self.return_button = QPushButton('Önceki arayüze dön')
        self.choose_target_doc_layout.addWidget(self.return_button, 0, 0, 1, 6)

        

        self.chooseFile_button = QPushButton('Dosya seç')
        self.chooseFile_button.setObjectName('chooseFile')
        self.choose_target_doc_layout.addWidget(self.chooseFile_button, 7, 1, 1, 2)
        self.chooseFile_button.clicked.connect(self.readDoc)


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
    
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
