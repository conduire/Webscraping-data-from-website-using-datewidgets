
# coding: utf-8

# In[16]:


from convertdelimiter import convertdelimiter
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import csv
import datetime
from datetime import datetime
from datetime import timedelta
import os


    

def days_between(d1, d2):
    # this function provides the number of days between the starting date and the ending date (including both of them)
    d1 = datetime.strptime(d1, "%Y/%m/%d")
    d2 = datetime.strptime(d2, "%Y/%m/%d")
    return abs((d2 - d1).days)+1


#=======================================================================================#
# Enter the start date and the end date in the same format as shown below (yyyy/mm/dd), for which you want to extract the data.
#=======================================================================================#
startdate="2018/06/24"
enddate="2018/07/10"
#=======================================================================================#
#=======================================================================================#
#Enter the location where you want to store the csv file
Folderlocation= 'C:\\Users\\Alok Singh\\Desktop\\METI_programming\\'
Filename='File2.csv'
#========================================================================================#
#========================================================================================#
if not os.path.exists(Folderlocation):
    os.makedirs(Folderlocation)
    

# the intitialization of the headers of the csv file
with open(os.path.join(Folderlocation,Filename), 'w') as csvfile:
        fieldnames = ['StartDateTime','EndDateTime','Price','PriceUnit','Volume','Volumeunit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# the difference between the two dates is found out here
diff=days_between(startdate,enddate)
diffhours=diff*24
#Since the website finds the data of the last week to the entered date the start date is incremented 
#to 6 days to obtain the data for the first week.
startdatemod=datetime.strptime(startdate, '%Y/%m/%d')+timedelta(days=6)


#Here the diff of the start and end date is used to run a while loop for extracting data till the end date.        
StartDateTime=[]*diffhours         

while diff > 0:
    ibex = "http://www.ibex.bg/en/market-data/dam/prices-and-volumes/"
    param = { "datatableDateFilter":str(startdatemod) }
    post = urllib.parse.urlencode(param).encode()
    html = urllib.request.urlopen(ibex, post)
    soup = BeautifulSoup(html,"lxml")
    #print (soup.prettify())

#table=soup.table
    tablelist=soup.find_all('table')
    table3=tablelist[2]
    
    A=[]
    B=[]
    table_rows=table3.find_all('tr')
    for tr in table_rows: 
        th=tr.find_all('th')
        head=[h.text for h in th]
        #print(head)
        A.append(head)
        td=tr.find_all('td')
        row=[i.text for i in td]
        #print(row)
        B.append(row)
    
    # the data from above is fed to the convertdelimiter function for conversion to the csv writable data       
    Datetimesemi=convertdelimiter(A,B,enddate,diff)
    
    # the csv writable data for all the weeks is stored in the StartDateTime variable
    StartDateTime+=Datetimesemi
    #print(Datetimesemi)
    #print(StartDateTime)
    
    
    #incrementing the date for accessing the next weeks data from website and decrementing the diff for controlling the while loop.
    startdatemod+=timedelta(days=7)
    diff-=7
    
   # the data obtained in the comma delimited format in the StartDateTime variable is stored in the csv file. 
for k in range(len(StartDateTime)):    
    with open(os.path.join(Folderlocation,Filename), 'a') as csvfile:
            fieldnames = ['StartDateTime','EndDateTime','Price','PriceUnit','Volume','Volumeunit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'StartDateTime':StartDateTime[k][0],'EndDateTime':StartDateTime[k][1],'Price': StartDateTime[k][2],'PriceUnit':'EUR/MWh','Volume':StartDateTime[k][3], 'Volumeunit':'MWh'})    
    
    
    
    
    

