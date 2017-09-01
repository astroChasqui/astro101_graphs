import matplotlib.pyplot as mpl
import matplotlib.ticker as ticker
import numpy as np

### Generate Mock Data

freqDays1 = 0.5
freqDays2 = 1
freqDays3 = 2

days = np.arange(1,50,0.05)
appMagnitude1 = 5000*np.sin(freqDays1*days/np.pi)+10000
appMagnitude2 = 500*np.sin(freqDays2*days/np.pi)+1000
appMagnitude3 = 50*np.sin(freqDays3*days/np.pi)+100

k = 70
k2 = 80
k3=5
error = 5e3
periods = np.logspace(-0.5,1.75,250)
luminosity_curve1 = 300*periods[k+k2:]
luminosity_points1 = 300*periods[k+k2:]+np.random.normal(0,luminosity_curve1/2.0,size=periods[k+k2:].size)
luminosity_error1 = 0.5 * 300*periods[k+k2:]

luminosity_curve2 = 300*periods[k+k3:k+k2-k3]
luminosity_points2 = 300*periods[k+k3:k+k2-k3]+np.random.normal(0,luminosity_curve2/2.0,size=periods[k+k3:k+k2-k3].size)
luminosity_error2= 0.6*300*periods[k+k3:k+k2-k3]

luminosity_curve3 = 300*periods[:k]
luminosity_points3 = 300*periods[:k]+np.random.normal(0,luminosity_curve3/2.0,size=periods[:k].size)
luminosity_error3 = 0.75 * 300*periods[:k]

### Design Plots

ColorLum1 = 'SteelBlue'
ColorMagPeriod1 = ColorLum1

ColorLum2 = 'ForestGreen'
ColorMagPeriod2 = ColorLum2

ColorLum3 = 'Crimson'
ColorMagPeriod3 = ColorLum3

### Plotting

fig,ax = mpl.subplots(1,2,figsize=(14,6))
fig.subplots_adjust(wspace=0.5)

ax[1].plot(days,appMagnitude1,'-',color=ColorMagPeriod1)
ax[0].plot(periods[k+k2:],luminosity_curve1,'-',color=ColorLum1)
ax[0].plot(periods[k+k2:],luminosity_points1,'o',color=ColorLum1)
ax[0].fill_between(periods[k+k2:],luminosity_curve1-luminosity_error1,luminosity_curve1+luminosity_error1,color=ColorLum1,alpha=0.10)

ax[1].plot(days,appMagnitude2,'-',color=ColorMagPeriod2)
ax[0].plot(periods[k+k3:k+k2-k3],luminosity_curve2,'-',color=ColorLum2)
ax[0].plot(periods[k+k3:k+k2-k3],luminosity_points2,'o',color=ColorLum2)
ax[0].fill_between(periods[k+k3:k+k2-k3],luminosity_curve2-luminosity_error2,luminosity_curve2+luminosity_error2,color=ColorLum2,alpha=0.10)

ax[1].plot(days,appMagnitude3,'-',color=ColorMagPeriod3)
ax[0].plot(periods[:k],luminosity_curve3,'-',color=ColorLum3)
ax[0].plot(periods[:k],luminosity_points3,'o',color=ColorLum3)
ax[0].fill_between(periods[:k],luminosity_curve3-luminosity_error3,luminosity_curve3+luminosity_error3,color=ColorLum3,alpha=0.10)

ax[1].set_xlabel('Time [days]', fontsize=18)
ax[1].set_ylabel(r'Luminosity $[\mathrm{L_\odot}]$', fontsize=18)
ax[0].set_xlabel('Period [days]', fontsize=18)
ax[0].set_ylabel(r'Luminosity $[\mathrm{L_\odot}]$', fontsize=18)

ax[0].loglog()
ax[0].xaxis.set_major_formatter(ticker.ScalarFormatter())
ax[0].yaxis.set_major_formatter(ticker.ScalarFormatter())
ax[0].set_ylim(10,5e4)
ax[0].set_xlim(0.1,100)

TICKS = [0.3,0.5,1,3,5,10,30,50,100]
TICK_LABELS =[]
for t in TICKS:
    if t<1:
        TICK_LABELS.append("%.1f"%t)
    else:
        TICK_LABELS.append("%i"%t)
ax[0].set_xticks(TICKS)
ax[0].set_xticklabels(TICK_LABELS)
ax[0].tick_params(labelsize=14)
ax[0].minorticks_off()

ax[1].semilogy()
ax[1].yaxis.set_major_formatter(ticker.ScalarFormatter())
ax[1].set_ylim(10,50000)
ax[1].tick_params(labelsize=14)
ax[1].minorticks_off

fig.savefig("PL_relation.png")
mpl.show()
