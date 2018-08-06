
# coding: utf-8

# In[1]:


import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import csv
import datetime
from datetime import datetime
from datetime import timedelta
import os


def convertdelimiter(A,B,enddate,diff):
    
    
    
# this function converts the data to a comma delimited format.    
# the dates are extracted here for concatenation with 2018    
    days=(A[0])[2:9]
    #print(days)
    for d in range(0,7):
        days[d]=days[d].split(",")
        days[d]=(days[d])[1]
        days[d]=days[d].lstrip()
        days[d]='2018/'+days[d]

# the price and volume are extracted here
    F=[]
    first=[]
    second=[]
    third=[]
    fourth=[]
    fifth=[]
    sixth=[]
    seventh=[]
    C=B[1:25]
    #print(B)
    
    for i in C:
        F.append(i[0])
        first.append(i[2])
        second.append(i[3])
        third.append(i[4])
        fourth.append(i[5])
        fifth.append(i[6])
        sixth.append(i[7])
        seventh.append(i[8])
    
    for f in range(0,24):
        F[f]=F[f].split("-")
        F[f]=F[f][0]+':00',F[f][1]+':00'
        first[f]=first[f].split("\n")
        second[f]=second[f].split("\n")
        third[f]=third[f].split("\n")
        fourth[f]=fourth[f].split("\n")
        fifth[f]=fifth[f].split("\n")
        sixth[f]=sixth[f].split("\n")
        seventh[f]=seventh[f].split("\n")
    
    
 #All the data is put in list in a list format below. Here a new variable datetimer is created to store all the data.
 # The new variable is intialised to None (24 * 7 = 168 times). And the val describes the number of days which have to be partially extracted
  # the website being scraped.
    val=diff%7
    valh=(val*24)+1
    #if (val==0):
        #datetimer=[None]*169
    #else:
        #datetimer=[None]*valh
        
    datetimer=[]    
    i=0
    j=0
    k=0
    for i in range(len(days)):
        for j in range(len(F)):
            if (k<=23) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],first[j][1],first[j][2]])
            elif (k>=24) and (k<=47) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],second[j][1],second[j][2]])
            elif (k>=48) and (k<=71) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],third[j][1],third[j][2]])
            elif (k>=72) and (k<=95) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],fourth[j][1],fourth[j][2]])
            elif (k>=96) and (k<=119) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],fifth[j][1],fifth[j][2]])
            elif (k>=120) and (k<=143) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],sixth[j][1],sixth[j][2]])
            elif (k>=144) and (k<=167) and (datetime.strptime(days[i],'%Y/%m/%d')<datetime.strptime(enddate,'%Y/%m/%d')):
                datetimer.append([days[i]+" "+F[j][0],days[i]+" "+F[j][1],seventh[j][1],seventh[j][2]])   
            k=k+1

    
    
    return datetimer    

