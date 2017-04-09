import time
from aco_funs import *
from aco_vrptw import *


import sqlite3
import numpy as np

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import math
import random

import sys
import os
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
    QHBoxLayout, QVBoxLayout,QLabel,QGridLayout,QFileDialog,QPushButton,QCheckBox,QLineEdit)


class slide(QWidget):

    clicked = pyqtSignal()
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
       
        tFont=QFont()
        tFont.setBold(True)
        
        self.lbMin=QLabel(self)
        self.lbMax=QLabel(self)
        self.lbNme=QLabel(self)
        self.lbVal=QLabel(self)

        self.lbMin.setFont(tFont)
        self.lbMax.setFont(tFont)
        self.lbNme.setFont(tFont)
        self.lbVal.setFont(tFont)

        self.lbMin.move(10,40)
        self.lbMax.move(140,40)
        self.lbNme.move(10,1)
        self.lbVal.move(10,20)

        self.slide=QSlider(Qt.Horizontal,self)
        self.slide.move(40,40)
        self.slide.valueChanged[int].connect(self.slideChangeValue)
    
        
        
    def setSlide(self,nme,tpe,dVal,minVal,maxVal):
        self.slNme=nme
        self.tpe=tpe

        if tpe =='perc':
            dVal0=round(dVal/100.,2)
            minVal0=round(minVal/100.,2)
            maxVal0=round(maxVal/100.,2)
        
        if tpe=='count':
            dVal0=dVal
            minVal0=minVal
            maxVal0=maxVal


        self.lbMin.setText(str(minVal0))
        self.lbMin.adjustSize()
    
        self.lbMax.setText(str(maxVal0))
        self.lbMax.adjustSize()
        
        self.lbNme.setText(nme)
        self.lbNme.adjustSize()
        
        #self.lbVal.setText(str(dVal0))
        #self.lbVal.adjustSize()
        
        self.slide.setRange(minVal,maxVal)
        self.slide.setSingleStep(1)
        
        self.slideChangeValue(dVal)

    def sizeHint(self):
        return QSize(180, 80)
 
    def slideChangeValue(self,value):
        #print(value)
        if self.tpe=='perc':
            value0=round(value/100.,2)
        if self.tpe=='count':
            value0=value
        
        slideVals[self.slNme]=value
        print(slideVals)
        self.lbVal.setText(str(value0))
        self.lbVal.adjustSize()
        self.slide.setValue(value)

class filedialog(QWidget):
   def __init__(self, parent = None):
      super(filedialog, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton('Select Input File')
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.inpFileLb = QLabel('File Name')	
      layout.addWidget(self.inpFileLb)
	 
      self.setLayout(layout)
		
   def getfile(self):
      inpFile = QFileDialog.getOpenFileName(self, 'Open file','C:\\Users\Lada\Documents\ACO\ACO-VRPTW\Input',"Txt Files (*.txt)")
      self.inpFilePath=inpFile[0]

      base=os.path.basename(inpFile[0])
      self.inputFileName=os.path.splitext(base)[0]
      
      self.inpFileLb.setText('FileName: '+self.inputFileName)
      self.inpFileLb.adjustSize()
      
      #self.le.setPixmap(QPixmap(fname))

class resDisp(QWidget):
    def __init__(self,titleD,parent=None):
        QWidget.__init__(self, parent)
		
        tFont=QFont()
        tFont.setBold(True)
        
        
        layout = QGridLayout()
      
        self.titleD=QLabel(titleD)
        self.titleD.setFont(tFont)
        
        
        self.iterD=QLabel('Iteration')
        self.iterDv=QLabel('0')
       
        self.iterCountD=QLabel('Iteration Count')
        self.iterCountDv=QLabel('0')
        
        self.colD=QLabel('Colony')
        self.colDv=QLabel('0')
        
        self.colSizeD=QLabel('Colony Size')
        self.colSizeDv=QLabel('0')
       
        self.alphaD=QLabel('Alpha')
        self.alphaDv=QLabel('0')
       
        self.brcpD=QLabel('Theta')
        self.brcpDv=QLabel('0')
       
        self.vehCountD = QLabel('Vehicle Count')	
        self.vehCountDv = QLabel('0')

        self.distD=QLabel('Distance')
        self.distDv=QLabel('0')
       

        layout.addWidget(self.titleD,1,1)
        
        layout.addWidget(self.iterD,2,1)
        layout.addWidget(self.iterDv,2,2)
        layout.addWidget(self.iterCountD,3,1)
        layout.addWidget(self.iterCountDv,3,2)
        
        layout.addWidget(self.colD,4,1)
        layout.addWidget(self.colDv,4,2)
        layout.addWidget(self.colSizeD,5,1)
        layout.addWidget(self.colSizeDv,5,2)
        
        layout.addWidget(self.alphaD,6,1)
        layout.addWidget(self.alphaDv,6,2)
        
        layout.addWidget(self.brcpD,7,1)
        layout.addWidget(self.brcpDv,7,2)
        
        layout.addWidget(self.vehCountD,8,1)
        layout.addWidget(self.vehCountDv,8,2)

        layout.addWidget(self.distD,9,1)
        layout.addWidget(self.distDv,9,2)
	 
        self.setLayout(layout)
    
    def dispRefresh(self,vehicleCount,distance,iteration,iterationCount,colony,colonySize,alpha,Theta):
    
        self.vehCountDv.setText(str(vehicleCount))
        self.vehCountDv.adjustSize()
        
        self.distDv.setText(str(distance))
        self.distDv.adjustSize()

        self.iterDv.setText(str(iteration))
        self.iterDv.adjustSize()
        
        self.iterCountDv.setText(str(iterationCount))
        self.iterDv.adjustSize()

        self.colDv.setText(str(colony))
        self.colDv.adjustSize()
        
        self.colSizeDv.setText(str(colonySize))
        self.colSizeDv.adjustSize()

        self.alphaDv.setText(str(alpha))
        self.alphaDv.adjustSize()
        
        self.brcpDv.setText(str(Theta))
        self.brcpDv.adjustSize()


class chartDisp(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        
        #layout = QVBoxLayout()
        layout = QGridLayout()
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.figure.subplots_adjust(left=0.2,right=0.95,bottom=0.2,top=0.95)
        #self.figure.subplots_adjust(left=0.4,right=0.7,bottom=0.4,top=0.7)
        
        #self.button1 = QPushButton('Plot1')
        #self.button1.clicked.connect(self.plot1)
        
        #self.button2=QPushButton('Plot2')
        #self.button2.clicked.connect(self.plot2)
        
        #layout.addWidget(self.button1,1,1,1,1)
        #layout.addWidget(self.button2,2,1,1,1)
        layout.addWidget(self.canvas,1,1,1,1)
        self.setFixedSize(300, 300)
        
        self.setLayout(layout)
    
    def plot1(self):
        #vehcount data
        c.execute('select vehCount,count(distinct idVar) from solutions group by vehCount')
        vehCtList0=c.fetchall()
        vehCounts=[]
        vehData=[]
        for vcd in vehCtList0:
            vehCounts.append(vcd[0])
            vehData.append(vcd[1])
        
        bar_width=0.6 

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)
        # plot data
        ax.bar(vehCounts,vehData,width=bar_width,color='b')
        
        #labels
        ax.set_xlabel('Vehicle Counts')
        ax.set_ylabel('Run Counts')
        ax.set_xticks([w+0.5*bar_width for w in vehCounts])
        ax.set_xticklabels(vehCounts)
        # refresh canvas
        self.canvas.draw()
          
    def plot2(self):
        #watch var
        rsv=rsv1.resVar
        if rsv=='Colony Size':
            rsv='colonySize'
        
        #rsvs
        c.execute('select distinct '+ rsv +' from solutions')
        rsvDt=[x[0] for x in c.fetchall()]
       
        #vehcounts
        c.execute('select distinct vehCount from solutions')
        vcs=[x[0] for x in c.fetchall()]
        
        bar_width=0.8/len(rsvDt) 
        color_list=[ 'b','g','r','c','m','y','k','w','navy','salmon']
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.hold(True)
        rsvarCt=1
        for rsvar in rsvDt:
            #get a record for eavh vecount
            vehCounts=[]
            vehData=[]
            for vc in vcs:
                c.execute('select count(distinct idVar) from solutions where '+rsv+' = '+str(rsvar)+ ' and vehCount = '+str(vc))
                vehCounts.append(vc+rsvarCt*bar_width)
                vehData.append(c.fetchall()[0][0])

            print(rsvar,vehCounts,vehData) 
            ax.bar( vehCounts,
                    vehData,
                    width=bar_width,
                    color=color_list[rsvarCt-1],
                    label=rsv+' '+str(rsvar))
            
            # Add a legend
            handles, labels = ax.get_legend_handles_labels()
            ax.legend(handles[::-1], labels[::-1], loc='upper right', fontsize = 'xx-small')
            rsvarCt+=1
        
        #labels
        ax.set_xlabel('Vehicle Counts')
        ax.set_ylabel('Run Counts')
        ax.set_xticks([vc+0.5*len(rsvDt)*bar_width for vc in vcs])
        ax.set_xticklabels(vcs)

        # refresh canvas
        self.canvas.draw()

class runDisp(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
		
        tFont=QFont()
        tFont.setBold(True)
        
        layout = QGridLayout()
        
        self.runD = QLabel('Run')	
        self.runDv = QLabel('0')
        
        self.runD.setFont(tFont)
        self.runDv.setFont(tFont)
        
        layout.addWidget(self.runD,1,1)
        layout.addWidget(self.runDv,1,2)
    
        self.setLayout(layout)

    def runRefresh(self,run):
        self.runDv.setText(str(run+1))
        self.runDv.adjustSize()


class processInd(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
		
        processFont=QFont()
        processFont.setBold(True)
        processFont.setPointSize(20)        

        layout = QGridLayout()
        
        self.processLabel = QLabel('')	
        self.processLabel.setFont(processFont)
        
        layout.addWidget(self.processLabel,1,1)
    
        self.setLayout(layout)

    def processStatus(self,status):
        self.processLabel.setText(str(status))
        QApplication.processEvents()

class researchVar(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
	    
        layout = QHBoxLayout()
        
        self.b1 = QPushButton("Alpha")
        self.b1.setCheckable(True)
        self.b1.clicked[bool].connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)
		
        self.b2 = QPushButton("Theta")
        self.b2.setCheckable(True)
        self.b2.clicked[bool].connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)
    
        self.b3 = QPushButton("Colony Size")
        self.b3.setCheckable(True)
        self.b3.clicked[bool].connect(lambda:self.btnstate(self.b3))
        layout.addWidget(self.b3)
        
        self.fromL=QLabel('From')
        self.fromLv=QLineEdit()
        layout.addWidget(self.fromL)
        layout.addWidget(self.fromLv)

        self.toL=QLabel('To')
        self.toLv=QLineEdit()
        layout.addWidget(self.toL)
        layout.addWidget(self.toLv)
        
        self.stepL=QLabel('Step')
        self.stepLv=QLineEdit()
        layout.addWidget(self.stepL)
        layout.addWidget(self.stepLv)
       
        self.resVar='None'
        self.setLayout(layout)
    
    def btnstate(self,b):
        self.resVar='None'
        if b.text()=='Alpha':
            self.b2.setChecked(False)
            self.b3.setChecked(False)
            if self.b1.isChecked():
                self.resVar='Alpha'
            else:
                self.resVar='None'
        if b.text()=='Theta':
            self.b1.setChecked(False)
            self.b3.setChecked(False)
            if self.b2.isChecked():
                self.resVar='Theta'
            else:
                self.resVar='None'
        
        if b.text()=='Colony Size':
            self.b1.setChecked(False)
            self.b2.setChecked(False)
            if self.b3.isChecked():
                self.resVar='Colony Size'
            else:
                self.resVar='None'
        print(self.resVar)

def run_bt_clicked(self):
    print('running')
    pStatus.processStatus('Running')

    #QApplication.processEvents()
    #aco_dtb
    #dtb='Output/aco_dtb.sqlite'
    #conn=sqlite3.connect(dtb)
    #c=conn.cursor()
    c.execute('DELETE FROM Solutions')
    c.execute('DELETE FROM Vehicles')

    rsv=rsv1.resVar
    if rsv == 'None':
        rsvFrom=1
        rsvTo=1
        rsvStep=1
    else:
        rsvFrom=round(float(rsv1.fromLv.text()),2)
        rsvTo=round(float(rsv1.toLv.text()),2)
        rsvStep=round(float(rsv1.stepLv.text()),2)
    
    depo=0
    file_select=True
    try:
        input_file=fd.inpFilePath
    except:
        file_select=False

    if file_select:
        srt=aco_setup(input_file,depo)
        dataM=srt['dataM']
        distM=srt['distM']
        locCount=srt['locCount']
        initSol=srt['initSol']

        alpha=round(slideVals['Alpha']/100.,2)
        Theta=round(slideVals['Theta']/100.,2)
        runCount=slideVals['Run Count']
        iterCount=slideVals['Iteration Count']
        colSize=slideVals['Colony Size']
        
        print('alpha',alpha)
        print('Theta',Theta)
        print('runCount',runCount)
        print('iterCount',iterCount)
        print('colSize',colSize)

        id_var=1
        for run in range(runCount):
            
            rsvV=rsvFrom
            while rsvV<=rsvTo:
                if rsv=='Alpha':
                    alpha=rsvV
                if rsv=='Theta':
                    Theta=rsvV
                if rsv=='Colony Size':
                    colSize=int(rsvV)

                solution=aco_run(dataM,distM,depo,locCount,initSol,alpha,Theta,iterCount,colSize)

                c.execute('''INSERT INTO Solutions(idVar,run,iteration,iterCount,colony,colonySize,alpha,theta,vehCount,distance)
          VALUES(?,?,?,?,?,?,?,?,?,?)''', (id_var,run,solution['iteration'],iterCount,solution['colony'],colSize,alpha,Theta,solution['vehicleCount'],solution['distance'])) 
               
                for veh in solution['vehicles']:
                    c.execute('''INSERT INTO Vehicles(idVar,vehNum,vehTour)
                               VALUES(?,?,?)''', (id_var,veh['vehNum'],str(veh['tour']))) 
                
                id_var+=1
                conn.commit()

                bsRefresh=False
                if run==0:
                    bestSolution=solution
                    bsRefresh=True

                if solution['vehicleCount']< bestSolution['vehicleCount']:
                    bestSolution=solution
                    bsRefresh=True
                if solution['vehicleCount']==bestSolution['vehicleCount'] and solution['distance']<bestSolution['distance']:
                    bestSolution=solution        
                    bsRefresh=True

                d1.dispRefresh(solution['vehicleCount'],solution['distance'],solution['iteration'],iterCount,solution['colony'],colSize,alpha,Theta)
                if bsRefresh==True:
                    d2.dispRefresh(bestSolution['vehicleCount'],bestSolution['distance'],bestSolution['iteration'],iterCount,bestSolution['colony'],colSize,alpha,Theta)
                
                rd1.runRefresh(run)
                if rsv == 'None':
                    chart1.plot1()
                else:
                    chart1.plot2()
                
                rsvV+=rsvStep
                rsvV=round(rsvV,2)
                
                

                QApplication.processEvents()
    pStatus.processStatus('Run Complete')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('ACO VRPTW')

    dtb='Output/aco_dtb.sqlite'
    conn=sqlite3.connect(dtb)
    c=conn.cursor()
    
    slideVals={}
    
    fd = filedialog()
    
    run_bt=QPushButton('RUN ACO')
    run_bt.setToolTip('run')  
    run_bt.clicked.connect(run_bt_clicked)

    layout=QGridLayout()
    
    s1 = slide()
    s2 = slide()
    s3 = slide()
    s4 = slide()
    s5 = slide()
    
    
    s1.setSlide('Alpha','perc',20,5,50)
    s2.setSlide('Theta','perc',60,0,100)
    s3.setSlide('Run Count','count',1,1,100)
    s4.setSlide('Iteration Count','count',30,1,50)
    s5.setSlide('Colony Size','count',20,1,100)
   
    d1=resDisp('Current Solution')
    d2=resDisp('Best Solution')

    pStatus=processInd()

    rd1=runDisp()
    rsv1=researchVar()
    chart1=chartDisp()

    layout.addWidget(s3,1,1)
    layout.addWidget(s4,1,2)
    layout.addWidget(s1,2,1)
    layout.addWidget(s2,2,2)
    layout.addWidget(s5,2,3)
    layout.addWidget(pStatus,1,3)
    
    layout.addWidget(rsv1,3,1,1,3)

    layout.addWidget(fd,4,1,1,1)
    layout.addWidget(run_bt,5,1,1,1)
    
    layout.addWidget(rd1,5,2,1,1)

    layout.addWidget(d1,6,1,1,1)
    layout.addWidget(d2,6,2,1,1)
    layout.addWidget(chart1,4,3,3,1)


    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
    conn.close()        
