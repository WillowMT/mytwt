import pandas as pd
import numpy as np
import pypyodbc as pyodbc
import os
import PySimpleGUI as sg
#from tabulate import tabulate as tb

sg.theme('LightBlue3')
font = ("Courier New" , 11)
direc = os.getcwd() + '\Twantay Daily.accdb'
print(direc + '\n')

print('Loading Data...')
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'%(direc) )
cursor = conn.cursor()
cursor.execute('select * from Daily')

tmp = []
total_paid_0 = 0
total_paid_1 = 0
tmp2 = []
minus_values = False

for row in cursor.fetchall():
    if row[1] == None:
        continue
    else:
        tmp2.append(row)
        if row[10] == False and row[5] == False:
            tmp.append(row)
        total_paid_0 = total_paid_0 + row[9]
        #print(row[10])
        if row[10] == False :
            total_paid_1 = total_paid_1 + row[9]

name = []
remainder = []

for i in tmp2:
    name.append(i[1])
    remainder.append(i[9])

df = pd.DataFrame({"Name":name,
                   "Remainder":remainder,})
    

table = pd.pivot_table(df,values="Remainder",index=["Name"],aggfunc=np.sum)


dft = table.reindex(table['Remainder'].sort_values(ascending=False).index)


filtered_dft = dft[dft['Remainder'] != 0]

print(filtered_dft)
for x in filtered_dft.values:
    if int(x) < 0:
        minus_values = True
        break

print('\nTotal Remainder: ' ,int(sum(filtered_dft.values)))
aaaa = str('Total Remainder: ' +str(int(sum(filtered_dft.values))))
def validate():
    if total_paid_0 == total_paid_1 and minus_values == False :
        aa = 'There are no errors.'
        return aa
    else:
        bb = ('!! There is a critical error !!\nEither Negative Values or Total Paid Error!!!')
        return bb
#x = input("\nExit?")
def dd ():
    x = 100
    return x

layout = [[sg.Text('Debt List')],
          [sg.Text(filtered_dft)],
          [sg.Text(aaaa)],
          [sg.Text(validate())],
          [sg.OK(),sg.Cancel()]]

window = sg.Window('Total Debt List',font=font).Layout([[sg.Column(layout, size=(450,300), scrollable=True)]])
event, values = window.read()
window.close()

