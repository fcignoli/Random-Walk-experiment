#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:08:06 2020

@author: felipe
"""



import numpy as np
import matplotlib.pyplot as plt

def leermd(filename):
    result = []
    from pandas import read_csv
    import numpy as np
    # Leer el archivo, separado por espacios, salteando 2 lineas de header
    #     y empleando la coma como separador decimal
    df = read_csv(filename, sep=' ', skiprows=2, decimal=',')
    # Convertir el dataframe de pandas a un array de numpy
    nparray = df.values
    nparray = nparray.astype(np.float)
    # Remover los posibles nans del archivo
    # nparray = nparray[~np.isnan(nparray).any(axis=1)]
    # Asignar las columnas a variables de salida
    for cols in range(nparray.shape[1]):
        out = nparray[:,cols]
        result.append(out)
       
    return result

#Trayectorias y media


N=12
t0,x0m,y0m=leermd('4masa1.csv')
t1,x1m,y1m=leermd('4masa2.csv')
t2,x2m,y2m=leermd('4masa3.csv')
t3,x3m,y3m=leermd('4masa4.csv')
t4,x4m,y4m=leermd('4masa5.csv')
t5,x5m,y5m=leermd('4masa6.csv')
t6,x6m,y6m=leermd('4masa7.csv')
t7,x7m,y7m=leermd('4masa8.csv')
t8,x8m,y8m=leermd('4masa9.csv')
t9,x9m,y9m=leermd('4masa10.csv')
t10,x10m,y10m=leermd('4masa11.csv')
t11,x11m,y11m=leermd('4masa12.csv')


#Variables corridas al origen:
x0=x0m-x0m[0]
x1=x1m-x1m[0]
x2=x2m-x2m[0]
x3=x3m-x3m[0]
x4=x4m-x4m[0]
x5=x5m-x5m[0]
x6=x6m-x6m[0]
x7=x7m-x7m[0]
x8=x8m-x8m[0]
x9=x9m-x9m[0]
x10=x10m-x10m[0]
x11=x11m-x11m[0]

y0=y0m-y0m[0]
y1=y1m-y1m[0]
y2=y2m-y2m[0]
y3=y3m-y3m[0]
y4=y4m-y4m[0]
y5=y5m-y5m[0]
y6=y6m-y6m[0]
y7=y7m-y7m[0]
y8=y8m-y8m[0]
y9=y9m-y9m[0]
y10=y10m-y10m[0]
y11=y11m-y11m[0]


#media y varianza

x_media=(x0+x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11)/N
x_var=((x0-x_media)**2 +(x1-x_media)**2 +(x2-x_media)**2 +(x3-x_media)**2 +(x4-x_media)**2 +(x5-x_media)**2 +(x6-x_media)**2 +(x7-x_media)**2 +(x8-x_media)**2 +(x9-x_media)**2 +(x10-x_media)**2 +(x11-x_media)**2)/(N-1)
y_media=(y0+y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11)/N

plt.plot(t0,x0,label='P1')
plt.plot(t1,x1,label='P2')
plt.plot(t2,x2,label='P3')
plt.plot(t3,x3,label='P4')
plt.plot(t4,x4,label='P5')
plt.plot(t5,x5,label='P6')
plt.plot(t6,x6,label='P7')
plt.plot(t7,x7,label='P8')
plt.plot(t8,x8,label='P9')
plt.plot(t9,x9,label='P10')
plt.plot(t10,x10,label='P11')
plt.plot(t11,x11,label='P12')
plt.plot(t0,x_media,'.',label='Media')
plt.plot(t0,x_var,label='varianza')
plt.legend()

#%%
from scipy.optimize import curve_fit
#ajustar la varianza
ydata=np.array([ 0.        ,  0.09916947,  0.17628986,  0.26309535,  0.38497331,
        0.59256119,  0.56640334,  0.79906643,  0.91180866,  0.74994996,
        1.05472465,  1.55616279,  1.70279208,  1.86216448,  2.16886876,
        2.46668956,  3.32678788,  4.48047817,  4.15715941,  4.42030743,
        6.01723203,  6.77740175,  8.00907467,  9.50288886, 10.19595723,
       10.74363231, 12.75816242, 12.84108177, 12.09773587, 11.49684706,
       11.02300146, 10.93220661, 10.76914362, 10.22125333,  9.28630843,
       11.31214524, 12.25741765, 13.60760412, 14.83455628, 16.37368067,
       18.36617903, 20.30890477, 21.57070547, 21.53918513, 22.52027619,
       23.87111066, 23.74954526, 25.25067892, 25.03015603, 25.85489837,
       24.84753468, 24.13993996, 22.7626955 , 19.54166653, 16.64493727,
       16.10619468, 16.34775106, 16.01707993, 15.05103473, 16.28262262,
       16.09287415, 16.60751198, 17.49589622, 19.01509231, 18.54193923,
       20.00915462, 21.38245723, 21.31572633, 20.37786485, 19.04358743,
       18.96745096, 19.15012359, 20.24572204, 20.16728695, 20.35667964,
       20.68561913, 22.07904171, 21.45900215, 20.75212437, 21.25629506,
       22.31649901, 23.58003636, 24.84593508, 26.16934723, 27.74839813,
       27.07628523, 29.01216193, 27.30113844, 27.67419003, 30.24095849,
       30.33846309, 30.56764402, 32.03234574, 31.39815115, 30.11665133,
       29.65144291, 29.91947818, 29.58450578, 29.87852449, 29.39430832,
       29.86417647, 28.62353958, 28.70597374, 29.5686236 , 29.45463856,
       29.73129432, 31.30182395, 34.85072701, 36.90334629, 39.27797265,
       39.95322565, 43.01338499, 44.08352845, 43.45040864, 45.08613883,
       44.95279009, 44.47780961, 50.73926523, 53.50733787, 55.38748647,
       62.35015918, 66.61806218, 69.37846239, 68.37785909, 68.16865889,
       69.81603785, 75.3070565 , 74.59891319, 74.68135048, 73.82339687,
       71.94238008, 68.97260977, 71.11975434, 70.33074624, 68.83482476,
       69.63977381, 69.99449231, 69.02714282, 69.3744678 , 75.87723539,
       75.63957868, 76.02561034, 76.84608778, 82.22808849, 82.85441818,
       83.12422988, 80.9283537 , 76.83424848, 73.19833199, 71.30340086,
       69.48226304, 67.25037289, 65.06713414, 63.23410217, 62.22529794,
       62.0884562 , 61.86976833, 62.13982874, 64.35764967, 65.87457606,
       70.52574656, 71.01439954, 72.67605145, 73.70187238, 75.56127425,
       76.90043028, 76.41696404, 76.63437484, 76.73932555, 76.77474306])
xdata=np.array([0.0667, 0.1   , 0.133 , 0.167 , 0.2   , 0.233 , 0.267 , 0.3   ,
       0.333 , 0.367 , 0.4   , 0.433 , 0.467 , 0.5   , 0.533 , 0.567 ,
       0.6   , 0.633 , 0.667 , 0.7   , 0.733 , 0.767 , 0.8   , 0.833 ,
       0.867 , 0.9   , 0.933 , 0.967 , 1.    , 1.03  , 1.07  , 1.1   ,
       1.13  , 1.17  , 1.2   , 1.23  , 1.27  , 1.3   , 1.33  , 1.37  ,
       1.4   , 1.43  , 1.47  , 1.5   , 1.53  , 1.57  , 1.6   , 1.63  ,
       1.67  , 1.7   , 1.73  , 1.77  , 1.8   , 1.83  , 1.87  , 1.9   ,
       1.93  , 1.97  , 2.    , 2.03  , 2.07  , 2.1   , 2.13  , 2.17  ,
       2.2   , 2.23  , 2.27  , 2.3   , 2.33  , 2.37  , 2.4   , 2.43  ,
       2.47  , 2.5   , 2.53  , 2.57  , 2.6   , 2.63  , 2.67  , 2.7   ,
       2.73  , 2.77  , 2.8   , 2.83  , 2.87  , 2.9   , 2.93  , 2.97  ,
       3.    , 3.03  , 3.07  , 3.1   , 3.14  , 3.17  , 3.2   , 3.24  ,
       3.27  , 3.3   , 3.34  , 3.37  , 3.4   , 3.44  , 3.47  , 3.5   ,
       3.54  , 3.57  , 3.6   , 3.64  , 3.67  , 3.7   , 3.74  , 3.77  ,
       3.8   , 3.84  , 3.87  , 3.9   , 3.94  , 3.97  , 4.    , 4.04  ,
       4.07  , 4.1   , 4.14  , 4.17  , 4.2   , 4.24  , 4.27  , 4.3   ,
       4.34  , 4.37  , 4.4   , 4.44  , 4.47  , 4.5   , 4.54  , 4.57  ,
       4.6   , 4.64  , 4.67  , 4.7   , 4.74  , 4.77  , 4.8   , 4.84  ,
       4.87  , 4.9   , 4.94  , 4.97  , 5.    , 5.04  , 5.07  , 5.1   ,
       5.14  , 5.17  , 5.2   , 5.24  , 5.27  , 5.3   , 5.34  , 5.37  ,
       5.4   , 5.44  , 5.47  , 5.5   , 5.54  , 5.57  , 5.6   , 5.64  ,
       5.67  , 5.7 ])




plt.plot(xdata,ydata, label='Varianza')



def func(x,c):

    return c*x

c=popt
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt),'r.',

         label='fit:sigma=%5.3f' % tuple(popt))
plt.legend()


#%%Desplazamiento cuadratico medio

MSD=(t0,x_media+x_var)

plt.plot(MSD)
plt.xlabel('$ \tau  [s]$')
plt.ylabel('$x[mm]$')

#%% Trayectorias de la particulas( si todas hubieran salido del origen)
plt.figure()
plt.plot(x0,y0,label='P1')
plt.plot(x1,y1,label='P2')
plt.plot(x2,y2,label='P3')
plt.plot(x3,y3,label='P4')
plt.plot(x4,y4,label='P5')
plt.plot(x5,y5,label='P6')
plt.plot(x6,y6,label='P7')
plt.plot(x7,y7,label='P8')
plt.plot(x8,y8,label='P9')
plt.plot(x9,y9,label='P10')
plt.plot(x10,y10,label='P11')
plt.plot(x11,y11,label='P12')
plt.plot(x_media,y_media,'.',label='Media')
plt.xlabel('X[mm]')
plt.ylabel('Y[mm]')
plt.title('Trayectorias de la particulas( si todas hubieran partido del origen)')
plt.legend()
#Trayectoria real de las particulas
plt.figure()
plt.plot(x0m,y0m,label='P1')
plt.plot(x1m,y1m,label='P2')
plt.plot(x2m,y2m,label='P3')
plt.plot(x3m,y3m,label='P4')
plt.plot(x4m,y4m,label='P5')
plt.plot(x5m,y5m,label='P6')
plt.plot(x6m,y6m,label='P7')
plt.plot(x7m,y7m,label='P8')
plt.plot(x8m,y8m,label='P9')
plt.plot(x9m,y9m,label='P10')
plt.plot(x10m,y10m,label='P11')
plt.plot(x11m,y11m,label='P12')
plt.plot(x_media,y_media,'.',label='Media')
plt.xlabel('X[mm]')
plt.ylabel('Y[mm]')
plt.title('Trayectorias real de la particulas')
plt.legend()