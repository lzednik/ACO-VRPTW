
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3


dtb='data_files/medSched.sqlite'

 
class newAppt(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        layout = QGridLayout()
        
        tFont=QFont()
        tFont.setBold(True)
        
        self.lbTitle=QLabel('                                        Create New Appointment                                        ')
        self.lbTitle.setFont(tFont)
        
        self.st0=slideT0()
        self.st1=slideT0()

        layout.addWidget(self.lbTitle,1,1,1,2)
        layout.addWidget(self.st0,2,1)
        layout.addWidget(self.st1,2,2)
        self.setLayout(layout)
    

class slideT0(QWidget):

    clicked = pyqtSignal()
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
       
        tFont=QFont()
        tFont.setBold(True)

        self.lbMin=QLabel('FROM',self)
        self.lbMax=QLabel('TO',self)
        self.lbNme=QLabel('TIME',self)
        self.lbVal=QLabel('',self)

        self.lbMin.setFont(tFont)
        self.lbMax.setFont(tFont)
        self.lbNme.setFont(tFont)
        self.lbVal.setFont(tFont)

        self.lbMin.move(0,40)
        self.lbMax.move(140,40)
        self.lbNme.move(10,1)
        self.lbVal.move(10,20)

        self.slide=QSlider(Qt.Horizontal,self)
        self.slide.move(40,40)
        
        #self.slide=QSlider(Qt.Horizontal,self)
        #self.slide.move(40,40)
        #self.slide.valueChanged[int].connect(self.slideChangeValue)
    
        
        
#    def setSlide(self,nme,tpe,dVal,minVal,maxVal):
#        self.slNme=nme
#        self.tpe=tpe
#
#        if tpe =='perc':
#            dVal0=round(dVal/100.,2)
#            minVal0=round(minVal/100.,2)
#            maxVal0=round(maxVal/100.,2)
#        
#        if tpe=='count':
#            dVal0=dVal
#            minVal0=minVal
#            maxVal0=maxVal
#
#
#        self.lbMin.setText(str(minVal0))
#        self.lbMin.adjustSize()
#    
#        self.lbMax.setText(str(maxVal0))
#        self.lbMax.adjustSize()
#        
#        self.lbNme.setText(nme)
#        self.lbNme.adjustSize()
#        
#        #self.lbVal.setText(str(dVal0))
#        #self.lbVal.adjustSize()
#        
#        self.slide.setRange(minVal,maxVal)
#        self.slide.setSingleStep(1)
#        
#        self.slideChangeValue(dVal)
#
#    def sizeHint(self):
#        return QSize(180, 80)
# 
#    def slideChangeValue(self,value):
#        #print(value)
#        if self.tpe=='perc':
#            value0=round(value/100.,2)
#        if self.tpe=='count':
#            value0=value
#        
#        slideVals[self.slNme]=value
#        print(slideVals)
#        self.lbVal.setText(str(value0))
#        self.lbVal.adjustSize()
#        self.slide.setValue(value)


class careMans(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        layout = QGridLayout()
        
        
        self.lb1=QLabel('Care Manager:')
        self.cmb1=QComboBox()
        
        self.cmb1.activated[str].connect(self.onActivated) 

        layout.addWidget(self.lb1,1,1)
        layout.addWidget(self.cmb1,1,2)
        
        self.setLayout(layout)
    
    def onActivated(self, cm_id):
        tbs.setCMTable(cm_id)
        #print('cal date is:',cal1.selectedDate().toPyDate())

    def addCM(self,cm_list):
        self.cmb1.clear()
        for cm in cm_list:
            self.cmb1.addItem(str(cm[0]))


class tbSched(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        layout = QGridLayout()
        
        self.table 	= QTableWidget()
        self.tableItem 	= QTableWidgetItem()
        self.table.verticalHeader().hide()
        # initiate table
        #self.table.setWindowTitle('CARE MANAGER #1')
        #self.table.resize(300, 300)
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        
        
        # set label
        self.table.setHorizontalHeaderLabels(['Member','Svc From','Svc To','Svc Actual','Address'])
        #table.setVerticalHeaderLabels(QString("V1;V2;V3;V4").split(";"))
 

        self.table.setColumnWidth(5,250)
        self.table.horizontalHeader().setStretchLastSection(True)
        
        
        # on click function
        #self.table.cellClicked.connect(cellClick)
        
        self.CMlb1=QLabel('')
       
        layout.addWidget(self.CMlb1,1,1)
        layout.addWidget(self.table,2,1)
        
        self.setLayout(layout)

    def setCMTable(self,cm_id):
        conn=sqlite3.connect(dtb)
        c=conn.cursor()
        print('CMT IS',cm_id)
        print('cal date is:',cal1.selectedDate().toPyDate())
        svc_dt=cal1.selectedDate().toPyDate()

        self.CMlb1.setText('Care Manager #'+str(cm_id))
        self.CMlb1.adjustSize()

        c.execute('''select a.mbr_id, 
                            a.svc_tm_from,
                            a.svc_tm_to,
                            a.svc_tm_actual,
                            b.full_addr
                    from    schedule a,
                            mbrs b
                    where   a.mbr_id = b.mbr_id and
                            cm_id =? and svc_dt =?''',(cm_id,svc_dt,))
        
        recs=c.fetchall()
        for pos in range(len(recs)):
            self.table.setItem(pos,0, QTableWidgetItem(str(recs[pos][0])))
            self.table.setItem(pos,1, QTableWidgetItem(str(recs[pos][1])))
            self.table.setItem(pos,2, QTableWidgetItem(str(recs[pos][2])))
            self.table.setItem(pos,3, QTableWidgetItem(str(recs[pos][3])))
            self.table.setItem(pos,4, QTableWidgetItem(str(recs[pos][4])))
        conn.close()
 
        #self.table.setItem(0,0, QTableWidgetItem('hello'))

#def cellClick(row,col):
#    print("Click on " + str(row) + " " + str(col))

def calClick(date):

    sd=date.toPyDate()
    print("Clicked on " + str(sd))
    conn=sqlite3.connect(dtb)
    c=conn.cursor()
    
    c.execute('''select distinct cm_id
                from schedule
                where svc_dt =?''',(sd,))
        
    cm_list=c.fetchall()
    for cm in cm_list:
        print(cm[0])
    
    crm.addCM(cm_list)
    conn.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Medica Care Management Scheduler')
   
    
    layout=QGridLayout()
    
    cal1=QCalendarWidget()
    cal1.clicked[QDate].connect(calClick)
    crm=careMans()
    tbs=tbSched()
    nappt=newAppt()

    layout.addWidget(cal1,1,1,1,1)
    layout.addWidget(nappt,1,2,1,1)
    layout.addWidget(crm,2,1,1,1)
    layout.addWidget(tbs,3,1,1,2)
    
    window.setGeometry(50, 50, 900, 500)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
