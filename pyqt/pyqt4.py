import sys
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
    QHBoxLayout, QVBoxLayout,QLabel)

class MyWidget(QWidget):

    clicked = pyqtSignal()
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        self.color = QColor(0, 0, 0)
        
        self.lb1=QLabel(self)
        self.lb1.move(10,10)
        self.lb1.setText('label 1')
        self.lb1.adjustSize()  
        

        self.sl1=QSlider(Qt.Horizontal,self)
        self.sl1.move(50,50)
        self.sl1.setRange(0,10)
        self.sl1.setSingleStep(1)
        self.sl1.valueChanged[int].connect(self.changeValue)

    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), QBrush(self.color))
        painter.end()
   
    
    def mousePressEvent(self, event):
    
        self.setFocus(Qt.OtherFocusReason)
        event.accept()
    
    def mouseReleaseEvent(self, event):
    
        if event.button() == Qt.LeftButton:
        
            self.color = QColor(self.color.green(), self.color.blue(),
                                127 - self.color.red())
            print(self.color)
            self.update()
            self.clicked.emit()
            event.accept()
    
    def sizeHint(self):
    
        return QSize(200, 200)
 
    def changeValue(self,value):
        print(value)
        #self.lbl3.setText(str(value))
        #self.lbl3.adjustSize()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    
    mywidget = MyWidget()
    label = QLabel('hi hi')
    
    #mywidget.clicked.connect(label.clear)
    mywidget.clicked.connect(label.clear)
    
    layout = QVBoxLayout()
    layout.addWidget(mywidget)
    layout.addWidget(label)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
