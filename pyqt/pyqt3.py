from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *

import sys

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.form_widget1 = FormWidget(self)
        self.layout.addWidget(self.form_widget1)

        self.form_widget2= FormWidget(self)
        self.layout.addWidget(self.form_widget2)

        self.setLayout(self.layout)
        #self.setCentralWidget(self.form_widget) 
        

class FormWidget(QWidget):

    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())
