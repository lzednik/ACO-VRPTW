
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
        
        lbFont=QFont()
        lbFont.setPointSize(10)
        lbFont.setBold(True)



        self.lbTitle=QLabel('                           Create New Appointment                          ')
        self.lbTitle.setFont(lbFont)
        
        self.mbr1=mbrSelection()
        self.slds=sliders()
        self.checkAveB=QPushButton('Check Availability')
        self.checkAveB.clicked.connect(self.checkAvb)
        
        self.appStatL=QLabel('Available')
        
        self.confB=QPushButton('Confirm')
        
        layout.addWidget(self.lbTitle,1,1,1,2)
        layout.addWidget(self.mbr1,2,1,1,1)
        layout.addWidget(self.slds,3,1,1,2)
        layout.addWidget(self.checkAveB,4,1,1,2)
        layout.addWidget(self.appStatL,5,1,1,1)
        layout.addWidget(self.confB,5,2,1,1)

        self.setLayout(layout)
        
    #Checking Availability 
    #ACO VRPTW Implementation
    def checkAvb(self):
        print('checking availability')
        #create DataM
        conn=sqlite3.connect(dtb)
        c=conn.cursor()
        svc_dt=cal1.selectedDate().toPyDate()
        c.execute('''select mbr_id, 
                            svc_tm_from,
                            svc_tm_to
                    from    schedule
                    where   svc_dt =?''',(svc_dt,))
        
        recs=c.fetchall()
        dataM=[]
        rec0={}
        for rec in recs:
            rec0['cust_no']=rec[0]
            rec0['ready_time']=rec[1]
            rec0['due_time']=rec[2]
            rec0['service_time']=0

        








        conn.close()

        #solution=aco_run(dataM,distM,depo,locCount,initSol,alpha,BRCP,iterCount,colSize)





class mbrSelection(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self, parent)
    
        layout = QGridLayout()
        
        tFont=QFont()
        tFont.setBold(True)

        self.lb1=QLabel('Member')
        
        self.lb1.setFont(tFont)
        

        layout.addWidget(self.lb1,1,1)

        self.setLayout(layout)
        



class sliders(QWidget):

    clicked = pyqtSignal()
    
    def __init__(self,parent = None):
    
        QWidget.__init__(self, parent)
      


        tFont=QFont()
        tFont.setBold(True)
        
        self.resize(350,200)
        self.setFixedSize(350,200)


        #Slide 1
        self.lbNme1=QLabel('Service Window From:',self)
        self.lbVal1=QLabel('',self)

        self.lbNme1.setFont(tFont)
        self.lbVal1.setFont(tFont)

        self.lbNme1.move(10,10)
        self.lbVal1.move(250,10)

        self.slide1=QSlider(Qt.Horizontal,self)
        self.slide1.move(150,10)

        self.slide1.setRange(84,228)
        self.slide1.valueChanged[int].connect(self.slideChangeValue1)
    
        #Slide 2
        self.lbNme2=QLabel('Service Window To:',self)
        self.lbVal2=QLabel('',self)

        self.lbNme2.setFont(tFont)
        self.lbVal2.setFont(tFont)

        self.lbNme2.move(10,60)
        self.lbVal2.move(250,60)

        self.slide2=QSlider(Qt.Horizontal,self)
        self.slide2.move(150,60)
       
        self.slide2.setRange(84,228)
        self.slide2.valueChanged[int].connect(self.slideChangeValue2)
        
        #Slide 3
        self.lbNme3=QLabel('Appointment Length:',self)
        self.lbVal3=QLabel('',self)

        self.lbNme3.setFont(tFont)
        self.lbVal3.setFont(tFont)

        self.lbNme3.move(10,110)
        self.lbVal3.move(250,110)

        self.slide3=QSlider(Qt.Horizontal,self)
        self.slide3.move(150,110)
       
        self.slide3.setRange(3,24)
        self.slide3.valueChanged[int].connect(self.slideChangeValue3)
        
        self.lbVal3.setText(str(dispDuration(3)))
        self.lbVal3.adjustSize()
        

    def slideChangeValue1(self,value):
        self.lbVal1.setText(str(dispTime(value)))
        self.lbVal1.adjustSize()
        self.slide2.setRange(value+6,228)

    def slideChangeValue2(self,value):
        self.lbVal2.setText(str(dispTime(value)))
        self.lbVal2.adjustSize()

    def slideChangeValue3(self,value):
        self.lbVal3.setText(str(dispDuration(value)))
        self.lbVal3.adjustSize()

def dispTime(t0):
    t0=t0*5
    ampm='am'
    if t0>=720:
        ampm='pm'
    
    t1=str(int(t0/60)%12)
    t2=str(t0%60)

    if t1=='0':
        t1='12'
    
    if len(t2)==1:
        t2='0'+t2
    
    t=t1+':'+t2+' '+ampm
    return(t)


def dispDuration(t0):
    t0=t0*5
    t1=str(int(t0/60))
    t2=str(t0%60)

    h='hrs'
    m='mins'
    
    if t1=='1':
        h='hr'
    if t2=='1':
        m='min'
    t=t1+' '+h+' '+t2+' '+m  
    return(t)   


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
        self.table.setColumnCount(6)
        
        
        # set label
        self.table.setHorizontalHeaderLabels(['Member','Apt Start From','Apt Start To','Apt Start Actual','Apt Length','Address'])
        #table.setVerticalHeaderLabels(QString("V1;V2;V3;V4").split(";"))
 

        self.table.setColumnWidth(6,250)
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
                            a.svc_len,
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
            self.table.setItem(pos,5, QTableWidgetItem(str(recs[pos][5])))
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
    
    window.setGeometry(50, 50, 900, 600)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
