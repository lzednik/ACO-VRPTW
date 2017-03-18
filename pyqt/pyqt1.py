import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,Qt
import time

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'ACO - WRPTW'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(200, 20)
        self.textbox.resize(280,40)
        
        #create button
        self.b1 = QPushButton('Button 1', self)
        self.b1.setToolTip('Button 1')  
        self.b1.move(100,70)
        
        #create button2
        self.b2 = QPushButton('Button 2 - RUN', self)
        self.b2.setToolTip('Button 2')  
        self.b2.move(200,70)
        self.b2.clicked.connect(self.b2_clicked)


        #label2
        self.lb2=QLabel(self)
        self.lb2.move(200,100)
        #self.lb2.setText('button 2 click')
        
        #label
        self.lbl = QLabel(self)
        
        self.qle = QLineEdit(self)
        self.qle.move(60, 100)
        self.lbl.move(60, 40)

        self.qle.textChanged[str].connect(self.onChanged)

        #label 2
        self.lbl2 = QLabel(self)
        self.lbl2.move(20,200)

        
        # connect butt  on to function on_click
        self.b1.clicked.connect(self.on_click)
        
        
        
        #slider 1
        self.sl1=QSlider(Qt.Horizontal,self)
        self.sl1.move(300,300)
        
        self.sl1.setRange(0,100)
        self.sl1.setSingleStep(1)
        #self.sl1.setMinimum(0)
        #self.sl1.setMaximum(100)
        #self.sl1.setValue(100)
        #self.sl1.setTickPosition(QSlider.TicksBelow)
        #self.sl1.setTickInterval(1)
        
        self.sl1.valueChanged[int].connect(self.changeValue)

        #label to go along with slider 1
        self.lbl3 = QLabel(self)
        self.lbl3.move(300,350)
        
        
        # connect butt  on to function on_click
        self.b1.clicked.connect(self.on_click)
        

        self.show()

    
    @pyqtSlot()
    def b2_clicked(self):
        for i in range(5):
            self.lb2.setText(str(i))
            time.sleep(1)
            QApplication.processEvents()
        #QMessageBox.question(self,'b2', 'button 2 click', QMessageBox.Ok, QMessageBox.Ok)

    
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
    
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def changeValue(self,value):
        self.lbl3.setText(str(value))
        self.lbl3.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
