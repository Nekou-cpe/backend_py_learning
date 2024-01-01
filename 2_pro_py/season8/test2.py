'''datetime modul'''
from datetime import date,time,datetime,timedelta
import pytz
from khayyam import *
#date
print(date.today())
day1=date(2002,11,2)
print(day1)
#time
time1=time(23,14,23,124)
print(time1)
#datetime 
print(datetime.now()) #shows system time
print(datetime.utcnow())
datetime1=datetime(2003,12,12,11,12,13)
print(datetime1)
print(date.today())
#str formats in datetime module:
#we want to show time by diffrent format ->strftime
print(datetime.now().strftime('%d,%m,%y %H:%M:%S'))
#change format from database to other formats ->strptime
datetime2='8/8/2002'
datetime3=datetime.strptime(datetime2,'%d/%m/%Y')
print(datetime3.strftime('%Y,%m,%d'))
#pytz -> python timezone ,shows real time
print(datetime.now(pytz.timezone('US/Central')))
#time delta
timeDelta=timedelta(days=34,hours=47,minutes=50)
time2=datetime(2002,2,2,10,20,30)
time3=timeDelta+time2
print(time3.second)
print(time3.minute)
#time diffrence
time4=datetime(2002,2,4,20,12,56)
time5=datetime(2006,5,8,6,34,45)
time6=abs(time4-time5)
time6_s=time6.total_seconds()
time6_m=time6.total_seconds()/60
time6_h=time6.total_seconds()/3600
print(time6)
print(time6_s)
print(time6_m)
print(time6_h)
#khayyam
print(JalaliDatetime.now())
print(JalaliDatetime.now().strftime('%c'))
datetime4=JalaliDatetime(1381,3,6)
print(datetime4.todate())
