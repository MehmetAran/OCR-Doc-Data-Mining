from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QDialog, QFrame, QLabel, QToolButton, QFileDialog
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtCore import Qt
import sys
import os
from bookIn import bookIn
from bookIn import multiBookIn
from leftNavigation import leftNavigation
from bookBorrow import bookBorrow
from bookReturn import bookReturn
import os
from DocumentOperations import DocumentOperation 
from AddDocument import AddDocumentToSqlite

class Main(QMainWindow):
    '''
    Main
    '''

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        Genel düzeni başlat
        '''
        self.title = "DDVT"
        self.resize(1000, 800)
        self.desktopWidth = QApplication.desktop().width()  # Geçerli masaüstünün genişliğini al
        self.desktopHeight = QApplication.desktop().height()  # Geçerli masaüstünün yüksekliğini al
        
        self.main_widget = QWidget()  # Pencerenin ana widget'ını oluşturun
        self.setWindowTitle(self.title)
        
        self.main_widget.setObjectName('main_widget')  # nesne adlandırma
        self.main_layout = QGridLayout()  # Izgara düzeni nesnesi oluştur
        self.main_widget.setLayout(self.main_layout)  # Ana widget'ı ızgara düzenine ayarla

        self.init_left()  # sol alanı başlat
        self.init_right()  # Doğru alanı başlat

        # Sol gezinme çubuğu, sağ ana arabirim, 
        # kitap depolama arabirimi (tek depolama ve çok kitaplı dosya içe aktarma),
        
        self.main_layout.addWidget(self.left_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.right_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.bookIn_widget, 0, 1, 1, 6)
        # self.main_layout.addWidget(self.singleBookIn_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.multiBookIn_widget, 0, 1, 1, 6)

        self.main_layout.addWidget(self.bookBorrow_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.bookReturn_widget, 0, 1, 1, 6)
        self.setCentralWidget(self.main_widget)  # Ana widget'ı ayarlama

        # pencere ozellik ayarlari
        # self.setWindowOpacity(2.0)  # Pencere saydamlığını ayarlama
        # self.setAttribute(Qt.WA_TranslucentBackground)  # Pencere arka planını saydam hale getirme
        # self.setWindowFlag(Qt.FramelessWindowHint)  # kenarlığı gizle
        self.main_layout.setSpacing(0)  # Sol ve sağ arasındaki boşluğu kaldır

    def init_left(self):
        '''
        Sol düzeni başlat
        '''
        self.left_widget = leftNavigation()  # Sol parçayı oluşturun
        self.left_widget.setObjectName('left_widget')  # Sol parça nesnesini adlandırın

        self.left_widget.left_close.clicked.connect(self.closeWindow)
        self.left_widget.left_mini.clicked.connect(self.minimizeWindow)
        self.visitFlag = False
        self.left_widget.left_visit.clicked.connect(self.visitWindow)

        self.left_widget.left_button4.clicked.connect(self.into_BookInView)
        self.left_widget.left_button2.clicked.connect(self.into_BookBorrowView)
        self.left_widget.left_button3.clicked.connect(self.into_BookReturnView)


    def init_right(self):
        '''
        Doğru düzeni başlat
        '''
        
        self.main_view()
        self.bookIn_view()
        self.borrow_view()
        self.return_view()
        


    def main_view(self):
        '''
        Giriş için ana arayüz
        '''
        self.right_widget = QWidget()  # Doğru arayüzü oluşturun 1
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()  # Izgara düzeni nesnesi oluşturma 1
        self.right_widget.setLayout(self.right_layout)  # Izgara düzeni için sağdaki arayüz 1 yerleşimini ayarlayın
        # Destek alanı
        self.label1 = QLabel()
        self.right_layout.addWidget(self.label1, 0, 0, 2, 4)


        introduction = '''
            <div style="text-align:center; font-size: 60px;font-family:'Microsoft Yahei'; color:#F76677;"><b>DDVT</b></div> 
            <div style="text-align:center; font-size: 15px;font-family: 'Arial'; color:#F76677;"><b>author: omer ustunay - mehmet aran</b><div>
            <div style="text-align:center; font-size: 15px;font-family: 'Arial'; color:#F76677;"><b>Kocaeli University</b></div>
        '''
        self.label_introduction = QLabel()
        self.label_introduction.setText(introduction)
        self.label_introduction.setObjectName('introduction')

        self.right_layout.addWidget(self.label_introduction, 3, 1, 2, 2)

        self.noneLabel1_2 = QLabel()  # Alanı desteklemek için kullanılır
        self.right_layout.addWidget(self.noneLabel1_2, 5, 0, 2, 4)

    def bookIn_view(self):
        '''
        Kitap depolama: sayfa seçimi: tekli depolama veya toplu depolama
        '''
        
        # Kitap saklama kılavuzu sayfası oluşturma
        self.bookIn_widget = bookIn()
        self.bookIn_widget.setObjectName('bookIn_widget')
        # Anahtar arabiriminin düğmesini atlama işlevine bağlayın
        self.bookIn_widget.returnMain_button.clicked.connect(
            self.return_mainView)
        
        self.bookIn_widget.btnDocNameEkle.clicked.connect(self.btnDocNameEkle)

        # Bu düğmeyle tek kitap depolama alanına geçiş arayüzünü bağlayın
        self.bookIn_widget.bookIn_single.clicked.connect(
            self.addDocument)

        # Bu düğme ile çoklu kitap depolamaya geçmek için arayüzü bağlayın
        self.bookIn_widget.bookIn_multi.clicked.connect(
            self.into_MultiBookInView)

        # Çok kitaplı depolama sayfası oluşturma
        self.multiBookIn_widget = multiBookIn()
        self.multiBookIn_widget.setObjectName('multiBookIn_widget')
        self.multiBookIn_widget.return_button.clicked.connect(
            self.into_BookInView)
        
        # Başlangıç ​​durumu: gizli
        self.multiBookIn_widget.hide()
        self.bookIn_widget.hide()

    def borrow_view(self):
        '''
        Borçlanma arayüzü
        '''
        self.bookBorrow_widget = bookBorrow()
        self.bookBorrow_widget.setObjectName('bookBorrow_widget')
        self.bookBorrow_widget.returnMain_button.clicked.connect(self.return_mainView)
        self.bookBorrow_widget.hide()

    def return_view(self):
        '''
        Kitap İade Arayüzü
        '''
        self.bookReturn_widget = bookReturn()
        self.bookReturn_widget.setObjectName('bookReturn_widget')
        self.bookReturn_widget.returnMain_button.clicked.connect(self.return_mainView)
        self.bookReturn_widget.hide()

   

    def return_mainView(self):
        self.right_widget.show()
        # self.singleBookIn_widget.hide()
        self.multiBookIn_widget.hide()
        self.bookIn_widget.hide()

        self.bookBorrow_widget.hide()
        self.bookReturn_widget.hide()


    def btnDocNameEkle(self):

        print("degeri buradan alcaz")


    def addDocument(self):
        fname = QFileDialog.getOpenFileName(
        self, 'Belge seçme işlemi', './', 'PDF(*.pdf)')
        filePath = fname[0]
        if(filePath == ""):
            return
        a = AddDocumentToSqlite()
        a.start(filePath)
        
        # Dosya acma islemi burada yapılacak

        '''
        Dosyayı açın ve metin kutusunda görüntüleyin
        '''
    



    

    def into_BookInView(self):
        '''
        Kitap depolama arayüzüne geçme
        '''
        self.bookIn_widget.show()
        # self.singleBookIn_widget.hide()
        self.multiBookIn_widget.hide()
        self.right_widget.hide()

        self.bookBorrow_widget.hide()
        self.bookReturn_widget.hide()


    def into_MultiBookInView(self):
        '''
        Çok kitaplı depolama arayüzü
        '''
        self.multiBookIn_widget.show()
        # self.singleBookIn_widget.hide()
        self.bookIn_widget.hide()
        self.right_widget.hide()

        self.bookBorrow_widget.hide()
        self.bookReturn_widget.hide()

    def into_BookBorrowView(self):
        '''
        Borçlanma arayüzüne geç
        '''
        self.bookBorrow_widget.show()

        # self.singleBookIn_widget.hide()
        self.multiBookIn_widget.hide()
        self.bookIn_widget.hide()
        self.right_widget.hide()
        self.bookReturn_widget.hide()


    def into_BookReturnView(self):
        '''
        Kitap iade arayüzüne geçme
        '''
        self.bookReturn_widget.show()
        self.bookBorrow_widget.hide()

        # self.singleBookIn_widget.hide()
        self.multiBookIn_widget.hide()
        self.bookIn_widget.hide()
        self.right_widget.hide()
       
    def closeWindow(self):
        '''
        Kapat düğmesine karşılık gelen pencereyi kapat
        '''
        self.close()

    def minimizeWindow(self):
        '''
        Mini düğmeye karşılık gelen simge durumuna küçültülmüş pencere
        '''
        self.showMinimized()

    def visitWindow(self):
        '''
        Ziyaret düğmesine karşılık gelen tam ekran veya geri yükleme penceresi boyutu
        '''
        if self.visitFlag == False:

            # sayfa tam ekran ayari

            self.showFullScreen()
            self.showMaximized()
            self.lastWidth = self.width()
            self.lastHeight = self.height()
            self.resize(self.desktopWidth, self.desktopHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)

            self.visitFlag = True
        else:
            self.resize(self.lastWidth, self.lastHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)

            self.visitFlag = False

    def mousePressEvent(self, QMouseEvent):
        '''
        Mevcut fare aşağı olayını yeniden tanımla
        '''
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos()-self.pos()  # Farenin pencereye göre konumunu alma
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        '''
        Mevcut fare hareketi olaylarını yeniden tanımlayın
        '''
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # Pencere konumunu değiştir
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        '''
        Mevcut fare bırakma olaylarını yeniden tanımlayın
        '''
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


def main():
    basePath = os.path.abspath('.')
    with open(basePath+'/resource/view/app.qss', encoding='utf-8') as f:
        qss = f.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    gui = Main()
    gui.setWindowIcon(QIcon(basePath+'resource/img/book.ico'))
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
