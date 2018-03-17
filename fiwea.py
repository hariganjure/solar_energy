import requests
import xlsxwriter
from datetime import date
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

api_add='http://api.openweathermap.org/data/2.5/weather?appid=9b1d5041a7d8e14fa540f79aea45063e&q='
city=input('City Name:')
url=api_add+city
json_data=requests.get(url).json()
formatted_data=json_data['main']
a=json_data['main']['temp']
b=json_data['main']['humidity']
name=json_data['name']
wind=json_data['wind']['speed']


ce=(a-273)
today = str(date.today())
print(formatted_data)
workbook   = xlsxwriter.Workbook('test.xls')

worksheet1 = workbook.add_worksheet()
worksheet1.write('A1', 'City')
worksheet1.write('B1', 'Date')
worksheet1.write('C1', 'Temp')
worksheet1.write('D1', 'Humidity')
worksheet1.write('E1', 'wind')

worksheet1.write('A2', name)
worksheet1.write('B2', today)
worksheet1.write('C2', ce)
worksheet1.write('D2', b)
worksheet1.write('E2', wind)


#worksheet1.save('excelwrite.xlsx')

workbook.close()

