impor
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("XXXX", "XXXX")
In [75]:
conn = MySQLdb.connect(host="localhost", user="root", passwd="XXXX", db="world")
cursor = conn.cursor()
In [76]:
cursor.execute('select Name, Continent, Population, LifeExpectancy, GNP from Country');
In [77]:
rows = cursor.fetchall()
In [78]:
str(rows)[0:300]