
#importando bibliotecas

import numpy as np
import seawater.eos80 as eos80
import matplotlib.pyplot as plt
import pandas as pd
import os

%matplotlib auto

#abrindo o diretorio de trabalho
os.chdir('/home/gustavo/Documentos/python_aulas/dados')


# Extraindo dados dos arquivos
Temperature = pd.read_csv('TemperaturaMercator.csv',delimiter=';')

Salinity = pd.read_csv('SalinidadeMercator.csv',delimiter=';')


 
# declarando variaveis
# aqui vamos pegar as 12 primeiras profundidades
temp = np.array(Temperature.iloc[1,1:12])
salt = np.array(Salinity.iloc[1,1:12])


# limites da figura (mins and maxs)
smin = salt.min() - (0.025 * salt.min())
smax = salt.max() + (0.025 * salt.max())
tmin = temp.min() - (0.25 * temp.max())
tmax = temp.max() + (0.25 * temp.max())
 
# calculo do numero de celulas necessarias no plot
xdim = round((smax-smin), 0)
ydim = round((tmax-tmin), 0)
 
# criando uma matriz com zeros  para receber os dados
dens = np.zeros([len(temp), len(salt)])
 

# criando os vetores de teperatura e sal
ti = np.arange(1,ydim-1, ydim)
si = np.arange(1,xdim-1,xdim)


# Loop para calcular as desidades
for j in range(0, len(salt),1):
    for i in range(0,len(temp),1):
        dens[j,i] = eos80.dens0(salt[j],temp[i])
 

#subtraindo 1000 para obermos o sigma-t
dens = dens - 1000

# o meshgrid transforma uma matriz unidimensional
# em uma matriz bidimensional combinando os indices das matrizes
# x[i], y[j] = X[i,j], Y[i,j]
salt1, temp1 = np.meshgrid(salt, temp)


# Plot dado
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
#plt.contourf(salt1, temp1, dens)
CS = plt.contour(salt1, temp1, dens, linestyles='dashed', colors='k')
plt.clabel(CS, fontsize=12, inline=1, fmt='%1.2f') # Label every second level
#plt.colorbar()
 

#plotando as legendas e os pontos
ax1.plot(salt,temp,'ob',markersize=9)
ax1.set_xlabel('Salinity')
ax1.set_ylabel('Temperature (C)')