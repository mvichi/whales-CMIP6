#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:36:21 2020

@author: thando
"""

#%% Loading Dependecnies
import netCDF4
import xarray as xr
import numpy as np
import matplotlib as m
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pylab as plt
import scipy.io
import math
# import mpl_toolkits as basemap
# from mpl_toolkits.basemap import Basemap
import sys
import pandas as pd
import datetime
from cartopy import crs as ccrs, feature as feature
import matplotlib.colors as colors
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from shapely.geometry.polygon import LinearRing
#%% Loading file using pandas
#fname1 = '/media/user/Transcend/ZATM0031/MSc2019/Whale Data/hump_filled.csv'
fname2 = '/media/thando/Transcend/ZATM0031/MSc2019/Whale Data/hump_filled_RR.csv'
df = pd.read_csv(fname2, sep= ';')

#df = df[(df.lat >= -90) & (df.lat <= -40)]
df = df[df['lat'] <= -40]

#%% JANUARY
Jtmp = df[(df['year'] >= 1900) & (df['year'] < 1910)]
Jtmp
Jtmp2 = Jtmp[Jtmp['month']==1]
Jtmp2
JtmpRR1 = Jtmp2[Jtmp2['class'] <7]

Jtmp3 = df[(df['year'] >= 1910) & (df['year'] < 1920)]
Jtmp3
Jtmp4 = Jtmp3[Jtmp3['month']==1]
Jtmp4
JtmpRR2 = Jtmp4[Jtmp4['class'] <7]

Jtmp5 = df[(df['year'] >= 1920) & (df['year'] < 1930)]
Jtmp5
Jtmp6 = Jtmp5[Jtmp5['month']==1]
Jtmp6
JtmpRR3 = Jtmp6[Jtmp6['class'] <7]

Jtmp7 = df[(df['year'] >= 1930) & (df['year'] < 1940)]
Jtmp7
Jtmp8 = Jtmp7[Jtmp7['month']==1]
Jtmp8
JtmpRR4 = Jtmp8[Jtmp8['class'] <7]

Jtmp9 = df[(df['year'] >= 1940) & (df['year'] < 1950)]
Jtmp9
Jtmp10 = Jtmp9[Jtmp9['month']==1]
Jtmp10
JtmpRR5 = Jtmp10[Jtmp10['class'] <7]

Jtmp11 = df[(df['year'] >= 1950) & (df['year'] < 1960)]
Jtmp11
Jtmp12 = Jtmp11[Jtmp11['month']==1]
Jtmp12
JtmpRR6 = Jtmp12[Jtmp12['class'] <7]

Jtmp13 = df[(df['year'] >= 1960) & (df['year'] < 1970)]
Jtmp13
Jtmp14 = Jtmp13[Jtmp13['month']==1]
Jtmp14
JtmpRR7 = Jtmp14[Jtmp14['class'] <7]

Jtmp15 = df[(df['year'] >= 1970) & (df['year'] < 1980)]
Jtmp15
Jtmp16 = Jtmp15[Jtmp15['month']==1]
Jtmp16
JtmpRR8 = Jtmp16[Jtmp16['class'] <7]

Jtmp17 = df[(df['year'] >= 1980) & (df['year'] < 1990)]
Jtmp17
Jtmp18 = Jtmp17[Jtmp17['month']==1]
Jtmp18
JtmpRR9 = Jtmp18[Jtmp18['class'] <7]

Jtmp19 = df[(df['year'] >= 1990) & (df['year'] < 2000)]
Jtmp19
Jtmp20 = Jtmp19[Jtmp19['month']==1]
Jtmp20
JtmpRR10 = Jtmp20[Jtmp20['class'] <7]


#%% FEBRUARY
Ftmp = df[(df['year'] >= 1900) & (df['year'] < 1910)]
Ftmp
Ftmp2 = Ftmp[Ftmp['month']==2]
Ftmp2
FtmpRR1 = Ftmp2[Ftmp2['class'] <7]

Ftmp3 = df[(df['year'] >= 1910) & (df['year'] < 1920)]
Ftmp3
Ftmp4 = Ftmp3[Ftmp3['month']==2]
Ftmp4
FtmpRR2 = Ftmp4[Ftmp4['class'] <7]

Ftmp5 = df[(df['year'] >= 1920) & (df['year'] < 1930)]
Ftmp5
Ftmp6 = Ftmp5[Ftmp5['month']==2]
Ftmp6
FtmpRR3 = Ftmp6[Ftmp6['class'] <7]

Ftmp7 = df[(df['year'] >= 1930) & (df['year'] < 1940)]
Ftmp7
Ftmp8 = Ftmp7[Ftmp7['month']==2]
Ftmp8
FtmpRR4 = Ftmp8[Ftmp8['class'] <7]

Ftmp9 = df[(df['year'] >= 1940) & (df['year'] < 1950)]
Ftmp9
Ftmp10 = Ftmp9[Ftmp9['month']==2]
Ftmp10
FtmpRR5 = Ftmp10[Ftmp10['class'] <7]

Ftmp11 = df[(df['year'] >= 1950) & (df['year'] < 1960)]
Ftmp11
Ftmp12 = Ftmp11[Ftmp11['month']==2]
Ftmp12
FtmpRR6 = Ftmp12[Ftmp12['class'] <7]

Ftmp13 = df[(df['year'] >= 1960) & (df['year'] < 1970)]
Ftmp13
Ftmp14 = Ftmp13[Ftmp13['month']==2]
Ftmp14
FtmpRR7 = Ftmp14[Ftmp14['class'] <7]

Ftmp15 = df[(df['year'] >= 1970) & (df['year'] < 1980)]
Ftmp15
Ftmp16 = Ftmp15[Ftmp15['month']==2]
Ftmp16
FtmpRR8 = Ftmp16[Ftmp16['class'] <7]

Ftmp17 = df[(df['year'] >= 1980) & (df['year'] < 1990)]
Ftmp17
Ftmp18 = Ftmp17[Ftmp17['month']==2]
Ftmp18
FtmpRR9 = Ftmp18[Ftmp18['class'] <7]

Ftmp19 = df[(df['year'] >= 1990) & (df['year'] < 2000)]
Ftmp19
Ftmp20 = Ftmp19[Ftmp19['month']==2]
Ftmp20
FtmpRR10 = Ftmp20[Ftmp20['class'] <7]

#%% NOVEMBER
Ntmp = df[(df['year'] >= 1900) & (df['year'] < 1910)]
Ntmp
Ntmp2 = Ntmp[Ntmp['month']==11]
Ntmp2
NtmpRR1 = Ntmp2[Ntmp2['class'] <7]

Ntmp3 = df[(df['year'] >= 1910) & (df['year'] < 1920)]
Ntmp3
Ntmp4 = Ntmp3[Ntmp3['month']==11]
Ntmp4
NtmpRR2= Ntmp4[Ntmp4['class'] <7]

Ntmp5 = df[(df['year'] >= 1920) & (df['year'] < 1930)]
Ntmp5
Ntmp6 = Ntmp5[Ntmp5['month']==11]
Ntmp6
NtmpRR3= Ntmp6[Ntmp6['class'] <7]

Ntmp7 = df[(df['year'] >= 1930) & (df['year'] < 1940)]
Ntmp7
Ntmp8 = Ntmp7[Ntmp7['month']==11]
Ntmp8
NtmpRR4= Ntmp8[Ntmp8['class'] <7]

Ntmp9 = df[(df['year'] >= 1940) & (df['year'] < 1950)]
Ntmp9
Ntmp10 = Ntmp9[Ntmp9['month']==11]
Ntmp10
NtmpRR5= Ntmp10[Ntmp10['class'] <7]

Ntmp11 = df[(df['year'] >= 1950) & (df['year'] < 1960)]
Ntmp11
Ntmp12 = Ntmp11[Ntmp11['month']==11]
Ntmp12
NtmpRR6= Ntmp12[Ntmp12['class'] <7]

Ntmp13 = df[(df['year'] >= 1960) & (df['year'] < 1970)]
Ntmp13
Ntmp14 = Ntmp13[Ntmp13['month']==11]
Ntmp14
NtmpRR7= Ntmp14[Ntmp14['class'] <7]

Ntmp15 = df[(df['year'] >= 1970) & (df['year'] < 1980)]
Ntmp15
Ntmp16 = Ntmp15[Ntmp15['month']==11]
Ntmp16
NtmpRR8= Ntmp16[Ntmp16['class'] <7]

Ntmp17 = df[(df['year'] >= 1980) & (df['year'] < 1990)]
Ntmp17
Ntmp18 = Ntmp17[Ntmp17['month']==11]
Ntmp18
NtmpRR9= Ntmp18[Ntmp18['class'] <7]

Ntmp19 = df[(df['year'] >= 1990) & (df['year'] < 2000)]
Ntmp19
Ntmp20 = Ntmp19[Ntmp19['month']==11]
Ntmp20
NtmpRR10= Ntmp20[Ntmp20['class'] <7]

#%% DECEMBER
Dtmp = df[(df['year'] >= 1900) & (df['year'] < 1910)]
Dtmp
Dtmp2 = Dtmp[Dtmp['month']==12]
Dtmp2
DtmpRR1= Dtmp2[Dtmp2['class'] <7]

Dtmp3 = df[(df['year'] >= 1910) & (df['year'] < 1920)]
Dtmp3
Dtmp4 = Dtmp3[Dtmp3['month']==12]
Dtmp4
DtmpRR2= Dtmp4[Dtmp4['class'] <7]

Dtmp5 = df[(df['year'] >= 1920) & (df['year'] < 1930)]
Dtmp5
Dtmp6 = Dtmp5[Dtmp5['month']==12]
Dtmp6
DtmpRR3= Dtmp6[Dtmp6['class'] <7]

Dtmp7 = df[(df['year'] >= 1930) & (df['year'] < 1940)]
Dtmp7
Dtmp8 = Dtmp7[Dtmp7['month']==12]
Dtmp8
DtmpRR4= Dtmp8[Dtmp8['class'] <7]

Dtmp9 = df[(df['year'] >= 1940) & (df['year'] < 1950)]
Dtmp9
Dtmp10 = Dtmp9[Dtmp9['month']==12]
Dtmp10
DtmpRR5= Dtmp10[Dtmp10['class'] <7]

Dtmp11 = df[(df['year'] >= 1950) & (df['year'] < 1960)]
Dtmp11
Dtmp12 = Dtmp11[Dtmp11['month']==12]
Dtmp12
DtmpRR6= Dtmp12[Dtmp12['class'] <7]

Dtmp13 = df[(df['year'] >= 1960) & (df['year'] < 1970)]
Dtmp13
Dtmp14 = Dtmp13[Dtmp13['month']==12]
Dtmp14
DtmpRR7= Dtmp14[Dtmp14['class'] <7]

Dtmp15 = df[(df['year'] >= 1970) & (df['year'] < 1980)]
Dtmp15
Dtmp16 = Dtmp15[Dtmp15['month']==12]
Dtmp16
DtmpRR8= Dtmp16[Dtmp16['class'] <7]

Dtmp17 = df[(df['year'] >= 1980) & (df['year'] < 1990)]
Dtmp17
Dtmp18 = Dtmp17[Dtmp17['month']==12]
Dtmp18
DtmpRR9= Dtmp18[Dtmp18['class'] <7]

Dtmp19 = df[(df['year'] >= 1990) & (df['year'] < 2000)]
Dtmp19
Dtmp20 = Dtmp19[Dtmp19['month']==12]
Dtmp20
DtmpRR10= Dtmp20[Dtmp20['class'] <7]    

#%% MATPLOTLIB PLOTTING
fig = plt.figure(figsize= (15, 5))
ax1 = plt.subplot(1,1,1, projection=ccrs.Mercator())

ax1.set_extent([-180, 180, -40, -75], crs=ccrs.PlateCarree())

lons = [-70, -70, 150, 150]
lats = [-42, -70, -70, -42]
ring = LinearRing(list(zip(lons, lats)))
ax1.add_geometries([ring], ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth = 2.5)

ax1.set_xlabel('Longitude', labelpad=2, fontsize = 14)
ax1.set_ylabel('Latitude', labelpad=2, fontsize = 14)


categories = ['1905','1915','1925','1935','1945','1955']

#NOVEMBER
ax1.scatter(NtmpRR1['long'], NtmpRR1['lat'], 100, marker='.', facecolor = 'yellow', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1905')
ax1.scatter(NtmpRR2['long'], NtmpRR2['lat'], 10, marker='.', facecolor = 'gold', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1915')
ax1.scatter(NtmpRR3['long'], NtmpRR3['lat'], 10, marker='.', facecolor = 'palegoldenrod', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1925')
ax1.scatter(NtmpRR4['long'], NtmpRR4['lat'], marker='.', facecolor = 'goldenrod', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1935')
ax1.scatter(NtmpRR5['long'], NtmpRR5['lat'], marker='.', facecolor = 'darkgoldenrod', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1945')
ax1.scatter(NtmpRR6['long'], NtmpRR6['lat'], marker='.', facecolor = 'beige', transform=ccrs.PlateCarree(), zorder=100, label = 'November 1955')

##DECEMBER
ax1.scatter(DtmpRR1['long'], DtmpRR1['lat'], marker='.', facecolor = 'blue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1905')
ax1.scatter(DtmpRR2['long'], DtmpRR2['lat'], marker='.', facecolor = 'darkblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1915')
ax1.scatter(DtmpRR3['long'], DtmpRR3['lat'], marker='.', facecolor = 'lightsteelblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1925')
ax1.scatter(DtmpRR4['long'], DtmpRR4['lat'], marker='.', facecolor = 'cornflowerblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1935')
ax1.scatter(DtmpRR5['long'], DtmpRR5['lat'], marker='.', facecolor = 'deepskyblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1945')
ax1.scatter(DtmpRR6['long'], DtmpRR6['lat'], marker='.', facecolor = 'dodgerblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1955')


## JANUARY
ax1.scatter(JtmpRR1['long'], JtmpRR1['lat'], marker='.', facecolor = 'red', transform=ccrs.PlateCarree(), zorder=1, label='January 1905')
ax1.scatter(JtmpRR2['long'], JtmpRR2['lat'], marker='.', facecolor = 'darkred', transform=ccrs.PlateCarree(), zorder=1, label='January 1915')
ax1.scatter(JtmpRR3['long'], JtmpRR3['lat'], marker='.', facecolor = 'tomato', transform=ccrs.PlateCarree(), zorder=1, label='January 1925')
ax1.scatter(JtmpRR4['long'], JtmpRR4['lat'], marker='.', facecolor = 'orangered', transform=ccrs.PlateCarree(), zorder=1, label='January 1935')
ax1.scatter(JtmpRR5['long'], JtmpRR5['lat'], marker='.', facecolor = 'rosybrown', transform=ccrs.PlateCarree(), zorder=1, label='January 1945')
ax1.scatter(JtmpRR6['long'], JtmpRR6['lat'], marker='.', facecolor = 'firebrick', transform=ccrs.PlateCarree(), zorder=1, label='January 1955')
#ax.scatter(JtmpRR7['long'], JtmpRR7['lat'], marker='.', facecolor = 'magenta', transform=ccrs.PlateCarree(), zorder=1, label='1965')
#ax.scatter(JtmpRR8['long'], JtmpRR8['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1975')
#ax.scatter(JtmpRR9['long'], JtmpRR9['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1985')
#ax.scatter(JtmpRR10['long'], JtmpRR10['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1995')


##FEBRUARY
ax1.scatter(FtmpRR1['long'], FtmpRR1['lat'], marker='.', facecolor = 'green', transform=ccrs.PlateCarree(), zorder=1, label='February 1905')
ax1.scatter(FtmpRR2['long'], FtmpRR2['lat'], marker='.', facecolor = 'darkgreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1915')
ax1.scatter(FtmpRR3['long'], FtmpRR3['lat'], marker='.', facecolor = 'palegreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1925')
ax1.scatter(FtmpRR4['long'], FtmpRR4['lat'], marker='.', facecolor = 'limegreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1935')
ax1.scatter(FtmpRR5['long'], FtmpRR5['lat'], marker='.', facecolor = 'seagreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1945')
ax1.scatter(FtmpRR6['long'], FtmpRR6['lat'], marker='.', facecolor = 'springgreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1955')

ax1.coastlines() 

gl1 = ax1.gridlines(linewidth = 0.5, color = 'grey', alpha = 0.3, linestyle = '-')
gl1.xlocator = mticker.MultipleLocator(60)
gl1.ylocator = mticker.MultipleLocator(10)


gl1.xlabels_bottom = True
gl1.ylabels_left = True

gl1.xformatter = LONGITUDE_FORMATTER
gl1.yformatter = LATITUDE_FORMATTER
gl1.xlabel_style = {'size': 13, 'color': 'black'}
gl1.ylabel_style = {'size': 13, 'color': 'black'}

#%%
plt.savefig("Decadal Whale Catches_Clusters_Mercator", format = 'png', dpi = 350, bbox_inches='tight')

#%%
#############

fig = plt.figure(figsize=(10, 50))
ax2 = fig.add_subplot(1, 2, 1, projection=ccrs.SouthPolarStereo())
ax2.set_extent([-180, 180, -90, -40], crs=ccrs.PlateCarree())

lons = [-70, -70, 150, 150]
lats = [-42, -70, -70, -42]
ring = LinearRing(list(zip(lons, lats)))
ax2.add_geometries([ring], ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth = 2.5)

##NOVEMBER
p1 = ax2.scatter(NtmpRR1['long'], NtmpRR1['lat'], marker='.', facecolor = 'yellow', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1905')
p2 = ax2.scatter(NtmpRR2['long'], NtmpRR2['lat'], marker='.', facecolor = 'gold', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1915')
p3 = ax2.scatter(NtmpRR3['long'], NtmpRR3['lat'], marker='.', facecolor = 'palegoldenrod', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1925')
p4 = ax2.scatter(NtmpRR4['long'], NtmpRR4['lat'], marker='.', facecolor = 'goldenrod', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1935')
p5 = ax2.scatter(NtmpRR5['long'], NtmpRR5['lat'], marker='.', facecolor = 'darkgoldenrod', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1945')
p6 = ax2.scatter(NtmpRR6['long'], NtmpRR6['lat'], marker='.', facecolor = 'beige', transform=ccrs.PlateCarree(), zorder=1, label = 'November 1955')


##DECEMBER
p11 = ax2.scatter(DtmpRR1['long'], DtmpRR1['lat'], marker='.', facecolor = 'blue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1905')
p22 = ax2.scatter(DtmpRR2['long'], DtmpRR2['lat'], marker='.', facecolor = 'darkblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1915')
p33 = ax2.scatter(DtmpRR3['long'], DtmpRR3['lat'], marker='.', facecolor = 'lightsteelblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1925')
p44 = ax2.scatter(DtmpRR4['long'], DtmpRR4['lat'], marker='.', facecolor = 'cornflowerblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1935')
p55 = ax2.scatter(DtmpRR5['long'], DtmpRR5['lat'], marker='.', facecolor = 'deepskyblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1945')
p66 = ax2.scatter(DtmpRR6['long'], DtmpRR6['lat'], marker='.', facecolor = 'dodgerblue', transform=ccrs.PlateCarree(), zorder=1, label = 'December 1955')


## JANUARY
p111 = ax2.scatter(JtmpRR1['long'], JtmpRR1['lat'], marker='.', facecolor = 'red', transform=ccrs.PlateCarree(), zorder=1, label='January 1905')
p222 = ax2.scatter(JtmpRR2['long'], JtmpRR2['lat'], marker='.', facecolor = 'darkred', transform=ccrs.PlateCarree(), zorder=1, label='January 1915')
p333 = ax2.scatter(JtmpRR3['long'], JtmpRR3['lat'], marker='.', facecolor = 'tomato', transform=ccrs.PlateCarree(), zorder=1, label='January 1925')
p444 = ax2.scatter(JtmpRR4['long'], JtmpRR4['lat'], marker='.', facecolor = 'orangered', transform=ccrs.PlateCarree(), zorder=1, label='January 1935')
p555 = ax2.scatter(JtmpRR5['long'], JtmpRR5['lat'], marker='.', facecolor = 'rosybrown', transform=ccrs.PlateCarree(), zorder=1, label='January 1945')
p666 = ax2.scatter(JtmpRR6['long'], JtmpRR6['lat'], marker='.', facecolor = 'firebrick', transform=ccrs.PlateCarree(), zorder=1, label='January 1955')
#ax.scatter(JtmpRR7['long'], JtmpRR7['lat'], marker='.', facecolor = 'magenta', transform=ccrs.PlateCarree(), zorder=1, label='1965')
#ax.scatter(JtmpRR8['long'], JtmpRR8['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1975')
#ax.scatter(JtmpRR9['long'], JtmpRR9['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1985')
#ax.scatter(JtmpRR10['long'], JtmpRR10['lat'], marker='o', facecolor = 'grey', transform=ccrs.PlateCarree(), zorder=1, label='1995')


##FEBRUARY
p1111 = ax2.scatter(FtmpRR1['long'], FtmpRR1['lat'], marker='.', facecolor = 'green', transform=ccrs.PlateCarree(), zorder=1, label='February 1905')
p2222 = ax2.scatter(FtmpRR2['long'], FtmpRR2['lat'], marker='.', facecolor = 'darkgreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1915')
p3333 = ax2.scatter(FtmpRR3['long'], FtmpRR3['lat'], marker='.', facecolor = 'palegreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1925')
p4444 = ax2.scatter(FtmpRR4['long'], FtmpRR4['lat'], marker='.', facecolor = 'limegreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1935')
p5555 = ax2.scatter(FtmpRR5['long'], FtmpRR5['lat'], marker='.', facecolor = 'seagreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1945')
p6666 = ax2.scatter(FtmpRR6['long'], FtmpRR6['lat'], marker='.', facecolor = 'springgreen', transform=ccrs.PlateCarree(), zorder=1, label='February 1955')

p0 = ax2.plot([0], marker='None', linestyle='None', label='dummy-tophead')

leg=ax2.legend([p0,p1,p2,p3,p4,p5,p6,p0,
            p11,p22,p33,p44,p55,p66,p0,
            p111,p222,p333,p444,p555,p666,p0,
            p1111,p2222,p3333,p4444,p5555,p6666],
            [r'November'] + categories + [r'December'] + categories + [r'January'] + categories + [r'February'] + categories,
            bbox_to_anchor=(1.1,0.5), loc='center left',ncol=4, borderaxespad=0.1, prop=dict(size=14))
leg.set_title('   November       December         January           February ', prop = {'size':'x-large'})

ax2.coastlines(resolution='50m', color='k')
ax2.gridlines(color='lightgrey', linestyle='-')


gl = ax2.gridlines(linewidth = 0.5, color = 'grey', alpha = 0.3,draw_labels=True, xlocs=None, ylocs=None)
gl.n_steps = 90

#%%
plt.savefig("Decadal Whale Catches_Clusters_Sterographic", format = 'png', dpi = 350, bbox_inches='tight')

#%%
 




