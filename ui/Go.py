import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class New(QDialog):

    def __init__(self):
        super(New, self).__init__()
        loadUi('./ui/New.ui', self)

