from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont



class bookReturn(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookReturn_layout = QGridLayout()
        self.setLayout(self.bookReturn_layout)

        self.returnMain_button = QPushButton('ana arayüze geri dön')
        self.bookReturn_layout.addWidget(self.returnMain_button, 0, 0, 1, 6)

        # self.book_number_label = QLabel('Kitap Numarası')
        # self.bookReturn_layout.addWidget(self.book_number_label, 2, 1, 1, 1)
        # self.book_number_label.setObjectName('bookReturn_label')
        # self.book_number = QLineEdit()
        # self.bookReturn_layout.addWidget(self.book_number, 2, 2, 1, 3)
        # self.book_number.setObjectName('bookReturn_edit')

        # self.card_number_label = QLabel('Kütüphane kart numarası')
        # self.bookReturn_layout.addWidget(self.card_number_label, 3, 1, 1, 1)
        # self.card_number_label.setObjectName('bookReturn_label')
        # self.card_number = QLineEdit()
        # self.bookReturn_layout.addWidget(self.card_number, 3, 2, 1, 3)
        # self.card_number.setObjectName('bookReturn_edit')

        self.Return_button = QPushButton('Return')
        self.bookReturn_layout.addWidget(self.Return_button, 4, 2, 1, 2)
        self.Return_button.setObjectName('bookReturn_button')
        self.Return_button.clicked.connect(self.Return)

        # self.record_label = QLabel('Şu anda ödünç alınan kitaplar:')
        # self.bookReturn_layout.addWidget(self.record_label, 5, 2, 1, 2)
        # self.record_label.setObjectName('bookBorrow_already')


        self.label = QLabel('Kitapları iade et')
        self.label.setObjectName('bookReturn_title')
        self.bookReturn_layout.addWidget(self.label, 10, 4, 2, 2)

    def Return(self):
        '''
        Kitapları iade et

        '''
        print("return fonksiyonu")
        
    def showTable(self, cursor, data):
        '''
        Kullanıcının ödünç aldığı kitapları göster
        '''
        # if data:
        #     # Sütun adı
        #     column = [s[0] for s in cursor.description]
        #     # 数据大小
        #     # Veri boyutu
        #     row = len(data)
        #     vol = len(data[0])
        #     # 插入表格
        #     # Tablo ekle
        #     table = QTableWidget(row, vol)
        #     # font = QFont('Microsoft Yahei', 10)
        #     table.setHorizontalHeaderLabels(column)
        #     table.verticalHeader().setVisible(False)
        #     table.setFrameShape(QFrame.NoFrame)

        #     for i in range(row):
        #         for j in range(vol):
        #             table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        #     # Geçerli kayıt tablosunu kaydet
        #     if self.returnRecord_table:
        #         self.bookReturn_layout.removeWidget(self.returnRecord_table)
        #         sip.delete(self.returnRecord_table)
        #     # 保存得到的当前记录表
        #     self.returnRecord_table = table
        # else:
        #     # 如果data不存在，则创建空表
        #     # Veri yoksa, boş bir tablo oluşturun
        #     self.returnRecord_table = QTableWidget()
        # # 重新添加该表
        # # Tabloyu yeniden ekleyin
        # self.bookReturn_layout.addWidget(self.returnRecord_table, 6, 1, 4, 4)

    def paintEvent(self, event):
        '''
        Birden çok değer aktarımından sonra işlev arızasını önlemek için, stili ayarlamak için qss kullanmaya devam edebilirsiniz.
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
