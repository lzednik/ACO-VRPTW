import datetime
import random
import numpy as np
import sqlite3
import sys
sys.path.insert(0, 'C:/Users/Lada/Documents/ACO/ACO-VRPTW')
from aco_funs import *
from aco_vrptw import *

dtb='data_files/medSched.sqlite'

conn=sqlite3.connect(dtb)
c=conn.cursor()




def gen_start_time():

    bounds=(84,228)
    new_start=0


    #10am peak
    choice_type=random.choice([1,2,3])

    if choice_type==1:
        #uniform all day
        new_start=random.randint(bounds[0],bounds[1])
    if choice_type==2:
        #morning normal peak
        mu=120
        sigma=12
        while new_start<bounds[0] or new_start>bounds[1]:
            new_start=int(np.random.normal(mu,sigma,1))

    if choice_type==3:
        #afternoon normal peak
        mu=198
        sigma=12
        while new_start<bounds[0] or new_start>bounds[1]:
            new_start=int(np.random.normal(mu,sigma,1))

    return new_start

def gen_win_len():
    win_len=random.choice([6,12])
    return win_len

def gen_svc_len():
    svc_len=random.choice([3,6,6,6,6,6,6,12,12,12])
    return svc_len

def gen_mbr():
    mbr=random.randint(1,98202)
    return mbr

svc_dt=datetime.date(2017,4,1)
end_dt=datetime.date(2017,4,30)

while svc_dt <= end_dt:
    if svc_dt.weekday() <=4:
        print('service date',svc_dt)

        #cms_in ct
        c.execute('''select count(distinct cm_id) 
                    from    schedule
                    where   svc_dt =?''',(svc_dt,))
        
        cms_in=c.fetchall()[0][0]
        cm_ct=5
        cmAvl=True


        while cm_ct>=cms_in and cmAvl:
            print('cm max',cm_ct,'cm_curr',cms_in)
            new_mbr=gen_mbr()
            new_start=gen_start_time()
            new_end=new_start+gen_win_len()
            new_svc_len=gen_svc_len()
            print(new_mbr,new_start,new_end,new_svc_len)



            c.execute('''select mbr_id, 
                                svc_tm_from,
                                svc_tm_to,
                                svc_len
                        from    schedule
                        where   svc_dt =?''',(svc_dt,))

            recs=c.fetchall()

            #check if mbr already has appt for that day
            dupl_appt=False
            for rec in recs:
                if new_mbr==rec[0]:
                    dupl_appt=True

            if dupl_appt==False:
                if len(recs)==0:
                    #first appointment
                    print('first appointment')
                    FirstAppt=True
                else:
                    FirstAppt=False
                    dataM=[]
                    custList=[0]
                    rec0={}
                    
                    #depo data
                    rec0['cust_no']=0
                    rec0['ready_time']=0
                    rec0['due_time']=1500
                    rec0['service_time']=0
                    dataM.append(rec0)

                    #create dataM records for already created appointments
                    for rec in recs:
                        rec0={}
                        rec0['cust_no']=rec[0]
                        rec0['ready_time']=rec[1]
                        rec0['due_time']=rec[2]
                        rec0['service_time']=rec[3]
                        dataM.append(rec0)
                        custList.append(rec[0])

                    #add new mbr to dataM
                    rec0={}
                    rec0['cust_no']=new_mbr
                    rec0['ready_time']=new_start
                    rec0['due_time']=new_end
                    rec0['service_time']=new_svc_len
                    dataM.append(rec0)
                    custList.append(new_mbr)
                    

                    #create distM
                    distM=[]
                    for cust1 in custList:
                        d0M=[]
                        for cust2 in custList:
                            c.execute(  '''
                                select  distinct    a.lat,
                                                    a.lon,
                                                    b.lat,
                                                    b.lon,
                                                    c.tme,
                                                    c.crow_dist
                                from    mbrs a,
                                        mbrs b,
                                        distTme c
                                where   a.mbr_id = ? and
                                        b.mbr_id = ? and
                                        a.zip_cd = c.zip_cd1 and
                                        b.zip_cd = c.zip_cd2

                                        ''',(cust1,cust2,))
                            
                            recs=c.fetchall()
                            
                            coord_from=(recs[0][0],recs[0][1])
                            coord_to=(recs[0][2],recs[0][3])
                            tme0=recs[0][4]
                            crow0=recs[0][5]
                            crow1=round(distance.euclidean(coord_from,coord_to),5)
                            tme1=float(crow1*tme0/crow0)
                            d0M.append(round(tme1/5,2))
                        distM.append(d0M)

                    
                    #Solution
                    initSol=initSolution(0,dataM,distM)
                    depo=0
                    locCount=len(dataM)
                    alpha=0.1
                    BRCP=0.7
                    iterCount=20
                    colSize=20
                            
                    solution=aco_run(dataM,distM,depo,locCount,initSol,alpha,BRCP,iterCount,colSize)
                    print('aco sol vehcount',solution['vehicleCount'])
                            
                    
                    
                #getting cm availability
                cmAvl=False
                if FirstAppt:
                    cmAvl=True
                else:
                    if solution['vehicleCount'] <= cm_ct:
                        print('')
                        print('')
                        print('####################')
                        print('####################')
                        curr_mbr_ct=len(dataM)-1
                        init_vc=initSol['vehicleCount']
                        aco_vc=solution['vehicleCount']
                        init_d=initSol['distance']
                        aco_d=solution['distance']
                        print('svc_dt',svc_dt)
                        print('current mbr count', curr_mbr_ct)
                        print('Init veh count',init_vc)
                        print('ACO veh count',aco_vc)
                        print('Init Distance',init_d)
                        print('ACO Distance',aco_d)
                        print('We have enough CMs')
                        print('####################')
                        print('####################')
                        for veh in solution['vehicles']:
                            print(veh['tour'])
                        print('####################')
                        print('####################')
                        print('')
                        print('')
                        cmAvl=True
                       
                        
                        #insert schedStats
                        c.execute('''INSERT INTO schedStats(svc_dt,mbr_ct,cm_ct_init,cm_ct_aco,dist_init,dist_aco)
                                     VALUES(?,?,?,?,?,?)''',(svc_dt,curr_mbr_ct,init_vc,aco_vc,init_d,aco_d)) 


                #confirm appt
                if cmAvl:
                    if FirstAppt:
                        print('inserting first appt')
                        cms_in=1
                        cm_id0=1
                        mbr_id0=new_mbr
                        svc_from0=new_start
                        svc_to0=new_end
                        svc_len0=new_svc_len
                        c.execute('''INSERT INTO schedule(cm_id,order_id,mbr_id,svc_dt,svc_tm_from,svc_tm_to,svc_len)
                                     VALUES(?,?,?,?,?,?,?)''',(1,1,new_mbr,svc_dt,new_start,new_end,new_svc_len)) 
                    else:
                        c.execute('''   Delete from schedule
                                        where   svc_dt =?''',(svc_dt,))
                        
                        for veh in solution['vehicles']:
                            order_id=1
                            for mbr in veh['tour']:
                                if mbr != 0:
                                    cm_id0=veh['vehNum']
                                    mbr_id0=dataM[mbr]['cust_no']
                                    svc_from0=dataM[mbr]['ready_time']
                                    svc_to0=dataM[mbr]['due_time']
                                    svc_len0=dataM[mbr]['service_time']
                                    c.execute('''INSERT INTO schedule(cm_id,order_id,mbr_id,svc_dt,svc_tm_from,svc_tm_to,svc_len)
                                                 VALUES(?,?,?,?,?,?,?)''',(cm_id0,order_id,mbr_id0,svc_dt,svc_from0,svc_to0,svc_len0)) 
                                    order_id+=1

                        cms_in=len(solution['vehicles'])
                         
                    conn.commit()
                    #time.sleep(20)
    svc_dt+=datetime.timedelta(days=1)
conn.close()
