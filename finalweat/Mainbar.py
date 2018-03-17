#!C:\Users\Aai\AppData\Local\Continuum\Anaconda3\python.exe
#print("Content-Type:text/html")
print()
import cgi
import xlrd
import matplotlib.pyplot as plt;
import datetime
from datetime import date
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
book = xlrd.open_workbook("monthexcel.xlsx")

sheet = book.sheets()[0]
sheet = book.sheet_by_index(0)
r = sheet.row(0)
c = sheet.col_values(0)
a= sheet.cell_value(0,0)
b= sheet.cell_value(0,1)
c= sheet.cell_value(0,2)
d= sheet.cell_value(0,3)
e= sheet.cell_value(0,4)
f= sheet.cell_value(0,5)
u= sheet.cell_value(1,0)
v= sheet.cell_value(1,1)
w= sheet.cell_value(1,2)
x= sheet.cell_value(1,3)
y= sheet.cell_value(1,4)
z= sheet.cell_value(1,5)
#u1_as_datetime = xlrd.xldate_as_tuple(u,book.datemode)
#u1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(u, book.datemode))
#v1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(v, book.datemode))
#w1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(w, book.datemode))
#x1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(x, book.datemode))
#y1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(y, book.datemode))
#z1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(z, book.datemode))
#print (a)
#print (b)
#print (c)
#print (d)
#print (e)
#print (f)
#print(u)
today = str(date.today())
print('hi')

objects = (u,v,w,x,y,z)
y_pos = np.arange(len(objects))
performance = [a, b, c, d, e, f]
fig=plt.figure()
print(performance)
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('solar energy generation')
plt.title('energy ')
fig.savefig("plot.png")

print("hiiii")

