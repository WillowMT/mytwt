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
epc = []
cat = []
cm = []
thirteenB = []

for row in cursor.fetchall():
    tmp.append(row)
    date_machine.append(row[0])
    epc.append(row[1])
    cat.append(row[11])
    cm.append(row[13])
    thirteenB.append(row[15])
'''
for i in date_machine:
    print(i)
    print(machine[date_machine.index(i)])
    '''
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
epc_points = np.array(epc)
cat_points = np.array(cat)
cm_points = np.array(cm)
thirteenB_points = np.array(thirteenB)
'''
for i in dates:
    print(i)
'''


plt.plot(xpoints,epc_points,color="purple",label="EPC")
plt.plot(xpoints,cat_points,color="red",label="CAT")
plt.plot(xpoints,cm_points,color="yellow",label="CM")
plt.plot(xpoints,thirteenB_points,color="green",label="13B")
plt.xlabel("Dates")
plt.ylabel("CAT")

ax = plt.gca()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(True)
plt.title('EPC')
plt.legend()
plt.show()

