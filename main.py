# -*- coding: utf-8 -*-

import math
import csv


print('IMPORTANT NOTE: FILE GEOMETRY.IN MUST BE ORDERED AS C,O,O AND TM ATOMS (top to bottom) IN ORDER TO RUNNING THE SCRIPT PROPERLY!!')


lista_x = []
lista_y = []
lista_z = []


with open('geometry.in', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)

    test_file = open('geometry.in', 'r')
    test_lines = test_file.readlines()
    test_file.close()

    count_geo = len(open('geometry.in').readlines())
    for row in table:
        lista_x.append(row[1])
        lista_y.append(row[2])
        lista_z.append(row[3])

#The first element in 'lista_x' is the x-coordinates for the carbon atom while the second is the x-coor. for O1 atom and so on.

#Calculating the distance between C-O1
d_co1 =  math.sqrt((float(lista_x[0])-float(lista_x[1]))**2 + (float(lista_y[0])-float(lista_y[1]))**2 + (float(lista_z[0])-float(lista_z[1]))**2)
print('Distance bewteen C and O¹ is', round(d_co1, 2), 'A')

#Calculating the distance between C-O2
d_co2 = math.sqrt((float(lista_x[0])-float(lista_x[2]))**2 + (float(lista_y[0])-float(lista_y[2]))**2 + (float(lista_z[0])-float(lista_z[2]))**2)
print('Distance bewteen C and O² is', round(d_co2, 2), 'A')

#Calculating the OCO angle
#First, lets define vectors u and v as C-O1 and C-O2 respectively:

u = [(float(lista_x[1]) - float(lista_x[0])), (float(lista_y[1]) - float(lista_y[0])), (float(lista_z[1]) - float(lista_z[0]))]
v = [(float(lista_x[2]) - float(lista_x[0])), (float(lista_y[2]) - float(lista_y[0])), (float(lista_z[2]) - float(lista_z[0]))]

#Calculating upper and lower values of the fraction

upper = (float(u[0])*float(v[0]) + float(u[1])*float(v[1]) + float(u[2])*float(v[2]))
lower = (math.sqrt(u[0]**2 + u[1]**2 + u[2]**2) * math.sqrt(v[0]**2 + v[1]**2 + v[2]**2))

cos_theta = float(upper) / float(lower)

#This result is in radians
theta = math.acos(cos_theta)
#Printing and directly converting to degrees
print('The angle between the OCO bond is', round(math.degrees(theta), 2), 'degrees.')


#Calculating the shortest distance bewtween TM-C and TM-O
#TM-C first

TM_C = []
TM_O = []

for i in range(3, 11):
    TM_C.append(math.sqrt((float(lista_x[0])-float(lista_x[i]))**2 + (float(lista_y[0])-float(lista_y[i]))**2 + (float(lista_z[0])-float(lista_z[i]))**2))
print('The shortest TM-C distance is', round(min(TM_C), 2), 'A.')

#Now for both TM-O distances
for j in range(1, 3):
    for i in range(3, 11):
        TM_O.append(math.sqrt((float(lista_x[j])-float(lista_x[i]))**2 + (float(lista_y[j])-float(lista_y[i]))**2 + (float(lista_z[j])-float(lista_z[i]))**2))
print('The shortest TM-O distance is', round(min(TM_O), 2), 'A.')

#Exporting into separate text files in the same folder as the script is located

with open('dCO1', 'w') as wf:
    wf.write(str(round(d_co1, 2)))

with open('dCO2', 'w') as wf:
    wf.write(str(round(d_co2, 2)))

with open('TM_C', 'w') as wf:
    wf.write(str(round(min(TM_C), 2)))

with open('TM_O', 'w') as wf:
    wf.write(str(round(min(TM_O), 2)))

with open('ANGLE', 'w') as wf:
    wf.write(str(round(math.degrees(theta), 2)))