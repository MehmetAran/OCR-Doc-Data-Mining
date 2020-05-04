import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import os

class New(QDialog):
    basepath = os.path.abspath(".")
    def __init__(self):
        super(New, self).__init__()
        loadUi(basepath+'src/ui/New.ui', self)

