import sys
from PyQt5.QtWidgets import QAction, QApplication, QDesktopWidget, QLineEdit, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Eklemek istediğiniz veriye bir isim verin"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
      
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.center()

        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Ekleme İşlemi', "Eklendi: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        self.setVisible(False)
        return textboxValue

    def execute(self):
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

    def center(self):
            # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

        

def executor(): 
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())