#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:14:22 2020

@author: thando
"""

#%% Loading Dependecnies
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
#%% Loading file using pandas
#fname1 = '/media/thando/Transcend/ZATM0031/MSc2019/Whale Data/hump_filled.csv'
fname2 = '../Data/WhaleData/hump_filled_RR.csv'
df = pd.read_csv(fname2, sep= ';')


### NEED TO SLICE BELOW 40 DEG SOUTH!
df = df[df['lat'] <= -40]
df = df[(df['long'] >= -70) & (df['long'] <= 150)]
#df = df.replace(np.nan, 0)
#%% MONTHS
NOV19001978 = df[df['month']==11]
NOV = NOV19001978[NOV19001978['class'] <7]

DEC19001978 = df[df['month']==12]
DEC = DEC19001978[DEC19001978['class'] <7]


JAN19001978 = df[df['month']==1]
JAN = JAN19001978[JAN19001978['class'] <7]

FEB19001978 = df[df['month']==2]
FEB = FEB19001978[FEB19001978['class'] <7]

#%%
#bins_list_A = np.arange(1900,1980,1)
#bins_list_D = [1900, 1910, 1920, 1940, 1950, 1960, 1970]
#%%
fig, axs = plt.subplots(2, 2,sharey=True, sharex = True, tight_layout=True )
axs[0,0].hist(NOV['year'], bins= np.arange(1900,1961,10)-0.5, color='green', zorder=2, rwidth=0.8, align = "left") ## 10 for Decadal or 1 for annual
axs[0,0].set_title('a) November', loc = 'left', fontsize=12)
axs[0,0].grid(True, which='major')
axs[0,1].hist(DEC['year'], bins=np.arange(1900,1961,10)-0.5, color='green', zorder=2, rwidth=0.8, align = "left")  ## 10 for Decadal
axs[0,1].set_title('b) December', loc = 'left', fontsize=12)
axs[0,1].grid(True)
axs[1,0].hist(JAN['year'], bins=np.arange(1900,1961,10)-0.5, color='green', zorder=2, rwidth=0.8, align = "left")  ## 10 for Decadal
axs[1,0].set_title('c) January', loc = 'left', fontsize=12)
axs[1,0].grid(True)
axs[1,1].hist(FEB['year'], bins=np.arange(1900,1961,10)-0.5, color='green', zorder=2, rwidth=0.8, align = "left")  ## 10 for Decadal
axs[1,1].set_title('d) February', loc = 'left', fontsize=12)
axs[1,1].grid(True)



plt.yticks(np.arange(0, 7000, 500,)) ##or 2000 for annual ##7000 for decadal

x = [1905, 1915, 1925, 1935, 1945, 1955, 1965, 1975] ##FOR DECADAL
# x = np.arange(1900,1981,10)##For AnNUAL
cc= dict.fromkeys(x)


for ax in axs.flat:
    ax.set_xticklabels(cc.keys())
    ax.set(xlabel='Year', ylabel='Whale Catches')
    ax.xaxis.get_label().set_fontsize(16)
    ax.yaxis.get_label().set_fontsize(16)
    ax.xaxis.set_tick_params(labelsize=14)
    ax.yaxis.set_tick_params(labelsize=14)
    ax.set_xlim([1900, 1970])
    ax.set_ylim([0, 6500])  #6500 for Decadal or 2000 for annual
for ax in axs.flat:
    ax.label_outer()    
    
#%%
plt.savefig('Whale Catches_Bins_Decadal', dpi = 350)
#%%
