# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 07:45:09 2017

@author: ladislav.zednik
"""

def dispTime(t0):
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
    
t0=600
print(dispTime(t0))
print(dispDuration(t0))
