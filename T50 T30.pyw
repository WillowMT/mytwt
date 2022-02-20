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
t50 = []
t30_1 = []
t30_2 = []
t30_3 = []
t15 = []

for row in cursor.fetchall():
    tmp.append(row)
    date_machine.append(row[0])
    t50.append(row[2])
    t30_1.append(row[3])
    t30_2.append(row[5])
    t30_3.append(row[7])
    t15.append(row[9])

xpoints = np.array(date_machine)
t50_points = np.array(t50)
t30_1_points = np.array(t30_1)
t30_2_points = np.array(t30_2)
t30_3_points = np.array(t30_3)
t15_points= np.array(t15)

fig, axs = plt.subplots(5,sharex=True)

axs[0].scatter(xpoints,t50_points,color="purple",label="t50")
axs[1].scatter(xpoints,t30_1_points,color="red",label="t30_1")
axs[2].scatter(xpoints,t30_2_points,color="yellow",label="t30_2")
axs[3].scatter(xpoints,t30_3_points,color="green",label="t30_3")
axs[4].scatter(xpoints,t15_points,color="blue",label="t15")


fig.suptitle('Machine')
for i in axs:
    i.legend()
plt.show()

