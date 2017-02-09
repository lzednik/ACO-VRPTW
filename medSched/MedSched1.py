
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3


dtb='data_files/medSched.sqlite'

 
#class tbWin(QWidget):
#     
#    def __init__(self, parent= None):
#        QWidget.__init__(self, parent)
#        self.setFixedHeight(200)
#         
#        #Container Widget        
#        widget = QWidget()
#        #Layout of Container Widget
#        layout = QVBoxLayout(self)
#        
#        tb1=tbSched()
#        tb2=tbSched()
#        tb3=tbSched()
#        layout.addWidget(tb1)
#        layout.addWidget(tb2)
#        layout.addWidget(tb3)
#        
#        #for _ in range(20):
#        #    btn = QPushButton("test")
#        #    layout.addWidget(btn)
#        widget.setLayout(layout)
# 
#        #Scroll Area Properties
#        scroll = QScrollArea()
#        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#        scroll.setWidgetResizable(False)
#        scroll.setWidget(widget)
#         
#        #Scroll Area Layer add 
#        vLayout = QVBoxLayout(self)
#        vLayout.addWidget(scroll)
#        self.setLayout(vLayout)

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
    
    def onActivated(self, cm_t):
        print('cmb box:',cm_t)
        tbs.setTableItem(cm_t)
        

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
 
        # set data
        #self.table.setItem(0,0, QTableWidgetItem("1"))
        #self.table.setItem(1,0, QTableWidgetItem("2"))
        #self.table.setItem(2,0, QTableWidgetItem("3"))
        #self.table.setItem(3,0, QTableWidgetItem("4"))
        #self.table.setItem(4,0, QTableWidgetItem("5"))
        
        #self.table.setItem(0,1, QTableWidgetItem("10:15"))
        #self.table.setItem(1,1, QTableWidgetItem("12:30"))
        #self.table.setItem(2,1, QTableWidgetItem("2:10"))
        #self.table.setItem(3,1, QTableWidgetItem("3:30"))
        #self.table.setItem(4,1, QTableWidgetItem("5:15"))

        #self.table.setItem(0,2, QTableWidgetItem("6521 Edgewood St Rockford, MN 55373"))
        #self.table.setItem(1,2, QTableWidgetItem("401 Carlson Pkwy Minnetonka, MN 55115"))
        #self.table.setItem(2,2, QTableWidgetItem("7659 78th Av NE Brooklyn Center, MN 55776"))
        #self.table.setItem(3,2, QTableWidgetItem("89766 1st St SW Bloomington, MN 55433"))
        #self.table.setItem(4,2, QTableWidgetItem("112233 ACO Street Ant City, MN, 55555"))
        


        self.table.setColumnWidth(5,250)
        self.table.horizontalHeader().setStretchLastSection(True)
        #header = self.table.horizontalHeader()
        #header.setStretchLastSection(True)
        #self.table.resizeColumnsToContents()
        #self.table.resizeColumnToContents(0)
        #self.table.resizeColumnToContents(1)
        #self.table.resizeColumnToContents(2)
        
        
        
        # on click function
        self.table.cellClicked.connect(cellClick)
        
        self.lb1=QLabel('Care Manager #1')
       
        layout.addWidget(self.lb1,1,1)
        layout.addWidget(self.table,2,1)
        
        self.setLayout(layout)

    def setTableItem(self,cm_t):
        conn=sqlite3.connect(dtb)
        c=conn.cursor()
        print('CMT IS',cm_t)
        c.execute('''select a.mbr_id, 
                            a.svc_tm_from,
                            a.svc_tm_to,
                            a.svc_tm_actual,
                            b.full_addr
                    from    schedule a,
                            mbrs b
                    where   a.mbr_id = b.mbr_id and
                            cm_id =?''',(cm_t,))
        
        recs=c.fetchall()
        for pos in range(len(recs)):
            print('col 1',pos,recs[pos][0])
            self.table.setItem(pos,0, QTableWidgetItem(str(recs[pos][0])))
            self.table.setItem(pos,1, QTableWidgetItem(str(recs[pos][1])))
            self.table.setItem(pos,2, QTableWidgetItem(str(recs[pos][2])))
            self.table.setItem(pos,3, QTableWidgetItem(str(recs[pos][3])))
            self.table.setItem(pos,4, QTableWidgetItem(str(recs[pos][4])))
        conn.close()
 
        #self.table.setItem(0,0, QTableWidgetItem('hello'))

def cellClick(row,col):
    print("Click on " + str(row) + " " + str(col))

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
   
    layout.addWidget(cal1,1,1,1,1)
    #wc=5

    #wl=[]
    #for w in range(wc):
    #    widName='Widget '+str(w)
    #    wl.append(QLabel(widName))

    
    #for pos in range(len(wl)):
    #    layout.addWidget(wl[pos],pos+3,1)

    #tb1=tbSched()

    crm=careMans()
    tbs=tbSched()
    
    placeHold=QLabel('                                                                             ')
    layout.addWidget(placeHold,1,2,1,1)
    
    layout.addWidget(crm,2,1,1,1)

    layout.addWidget(tbs,3,1,1,2)

    
    window.setGeometry(50, 50, 900, 500)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
