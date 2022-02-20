import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
import pypyodbc as pyodbc
import os

direc = os.getcwd() + '\Twantay Daily.accdb'
print(direc + '\n')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'%(direc) )
cursor = conn.cursor()
cursor.execute('select * from Machine')

tmp = []
date_machine = []
machine = []

for row in cursor.fetchall():
    tmp.append(row)
    date_machine.append(row[0])
    machine.append(row[14])
'''
print(len(date_machine))
print(len(cat_machine))

dates = [datetime.datetime(2021,12,1),
         datetime.datetime(2021,12,2),
         datetime.datetime(2021,12,3),
         datetime.datetime(2021,12,4),
         datetime.datetime(2021,12,5)]
'''
xpoints = np.array(date_machine)
ypoints = np.array(machine)
'''
for i in dates:
    print(i)
'''


plt.plot(xpoints,ypoints,color="green")
plt.xlabel("Dates")
plt.ylabel("CAT")

ax = plt.gca()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.title('13B')
plt.show()

