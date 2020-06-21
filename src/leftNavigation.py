from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QStyleOption, QStyle
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter



# Genel UI'da sol kısımdaki grafikler ve buttonlar burada yer almaktadır.

class leftNavigation(QWidget):
    '''
    Sol gezinme çubuğu
    '''

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.left_layout = QGridLayout()  # Izgara düzeni nesneleri oluşturma
        self.setLayout(self.left_layout)  # Sol parçayı ızgara düzenine ayarla

        # Başlangıçta sol etiket ve düğme oluştur
        self.init_left_close_mini_visit()
        self.init_left_label()
        self.init_left_Book_operation()

        # Başlatılan sol etiketi ve düğmeyi sol ızgara düzenine ekleyin
        # Bazı düğmeleri simge durumuna küçültün, yakınlaştırın ve kapatın
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 2, 1, 1)
        # Kitap işlemi bölümündeki etiketler ve düğmeler
        self.left_layout.addWidget(self.left_label1, 1, 0, 1, 3)
       
        self.left_layout.addWidget(self.left_button2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button3, 4, 0, 1, 3)
        # Kütüphane yönetimi bölümündeki etiketler ve düğmeler
        self.left_layout.addWidget(self.left_label2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button4, 6, 0, 1, 3)

        # Yardım
        self.left_layout.addWidget(self.left_label3, 8, 0, 1, 3)

    def init_left_close_mini_visit(self):
        '''
        Kapat, simge durumuna küçültme, yakınlaştırma ve geri yükleme düğmeleri oluşturma
        '''
        self.left_close = QPushButton("")  # Kapat düğmesi
        self.left_close.setObjectName('left_close')
        self.left_mini = QPushButton("")  # Simge durumuna küçült düğmesi
        self.left_mini.setObjectName('left_mini')
        self.left_visit = QPushButton("")  # Boş düğme
        self.left_visit.setObjectName('left_visit')

        # self.left_close.clicked.connect(self.closeWindow)
        # self.left_mini.clicked.connect(self.minimizeWindow)
        # self.visitFlag = False
        # self.left_visit.clicked.connect(self.visitWindow)

    def init_left_label(self):
        '''
        Sol başlık çubuğu
        '''
        self.left_label1 = QPushButton('Veritabanı islemleri')
        self.left_label1.setObjectName('left_label')
        self.left_label2 = QPushButton('Dokuman Islemleri')
        self.left_label2.setObjectName('left_label')
        self.left_label3 = QPushButton('İletişim ve yardım')
        self.left_label3.setObjectName('left_label')

    def init_left_Book_operation(self):
        '''
        Sol kitap çalıştırma düğmesi
        '''
        
        self.left_button2 = QPushButton('Dokümanlar')
        self.left_button2.setObjectName('left_button')
        self.left_button2.setIcon(QtGui.QIcon('./img/bookborrow.png'))
        self.left_button3 = QPushButton('Doküman Eşleştirme')
        self.left_button3.setObjectName('left_button')
        self.left_button3.setIcon(QtGui.QIcon('./img/bookreturn.png'))

        self.left_button4 = QPushButton('Doküman Tanıt')
        self.left_button4.setObjectName('left_button')
        self.left_button4.setIcon(QtGui.QIcon('./img/bookin.png'))


    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için, stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
