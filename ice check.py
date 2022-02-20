from asyncio.windows_events import NULL
import pypyodbc as pyodbc
import os
import pandas as pd

direc = os.getcwd() + '\Twantay Daily.accdb'
print(direc + '\n')

print('Loading Data...')
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'%(direc) )
cursor = conn.cursor()
cursor.execute('select * from Machine')

cursor2 = conn.cursor()
cursor2.execute('select * from Daily')


#Machine
machine_dates = []
machine_ice = []
machine = []
for row in cursor.fetchall():
    machine_dates.append(row[0])
    machine_ice.append(row[len(row)-3])


for i in range(len(machine_dates)):
    machine.append([machine_dates[i],machine_ice[i]])
machine = sorted(machine, key=lambda x: x[0], reverse=False)

#Daily
daily_dates = []
daily_ice = []
for row in cursor2.fetchall():
    daily_dates.append(row[2])
    daily_ice.append(row[3])
    
pd.to_datetime(daily_dates)
df = pd.DataFrame({'Dates':daily_dates,
                  'Ice':daily_ice})

daily_pv = df.groupby(by=['Dates']).sum()

daily_dates_pv = daily_pv.index.to_list()
daily_ice_pv = daily_pv.values.tolist()

dailyday = daily_dates_pv[96:len(daily_dates_pv)]
dailyice = daily_ice_pv[96:len(daily_ice_pv)]

faulty = []

for i in range(len(dailyday)):
    try:
        if dailyday[i] == machine[i][0] and dailyice[i] == [machine[i][1]]:
            continue
        
        else:
            faulty.append([dailyday[i],machine[i][0],dailyice[i],machine[i][1]])
    except:
        print("One index is out of range")

if len(faulty) == 0:
    print('\nThere are no ICE mismatch.\nAll good to go!')
else:
    print(' ')
    print(len(faulty),'Critical Error(s)!\n')
    for i in faulty:
        print('-------------------')
        print(i[0],i[1],'\nDaily: ',i[2],'Machine: ',[i[3]])
        print('-------------------')
x = input('\nExit??')
