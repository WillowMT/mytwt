import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime as dt
import numpy as np
import pypyodbc as pyodbc
import os
import matplotlib.dates as mdates
import PySimpleGUI as sg

sg.theme('LightBlue3')
font = ("Courier New" , 11)

direc = os.getcwd() + '\Twantay Daily.accdb'
print(direc + '\n')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'%(direc) )
cursor = conn.cursor()
cursor.execute('select * from Daily')

dates = []
ice = []

for row in cursor.fetchall():
  if row[1] == None:
    continue
  else:
    dates.append(row[2])
    ice.append(row[3])

y = ice
def removeDubs(x):
  return list(dict.fromkeys(x))





x = pd.DataFrame({'dates':dates,'values':y})
x['dates'] = pd.to_datetime(x['dates'])
x.index = x['dates'].dt.to_period('m')

#getting all years from raw datea
monthss = ['01','02','03','04','05','06','07','08','09','10','11','12']
years = []
for i in x.index:
    years.append(i.year)
years = removeDubs(years)

##########################################################################
#years = [2021]
layout = [[sg.Text('Monthly ICE')]]
val = []
for i in years:
  print(i)
  real_months = []
  condition = x.index.year == i
  new_df = x[condition]

  y = new_df.groupby(level=0).sum()
  print(y)
  
  real_months = y.index.month.tolist()
  for i in range(1,13):
    if i in real_months:

      val.append(int(y.values[real_months.index(i)]))
    else:

      val.append(0)
  #y = y.reindex(pd.period_range(y.index.min(), y.index.max(), freq='m'), fill_value=0)
FINAL = pd.DataFrame({'Year':np.repeat(years,12),
                       'Months':monthss*len(years),
                        'Values':val})
FINAL_PV = FINAL.pivot(index='Months',columns='Year',values='Values')
FINAL_PV.plot.bar()
plt.show()
plt.close()
layout.append([sg.Text(FINAL_PV)])

layout.append([sg.OK(),sg.Cancel()])
window = sg.Window('Monthly List',font=font).Layout([[sg.Column(layout, size=(400,310), scrollable=True)]])
event, values = window.read()
window.close()

