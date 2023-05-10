#https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
#https://cpp-python-nsu.inp.nsk.su/textbook/sec4/ch8
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
from textwrap import wrap

with open("settings.txt", "r") as settings:
    data_settings = np.array([float(i) for i in settings.read().split("\n")])
data_array = np.loadtxt("data.txt", dtype = int)

size = data_array.size
data_time = np.empty((size))
data_voltage = np.empty((size))
for i in range(size):
    data_voltage[i] = data_settings[0] * data_array[i]
    data_time[i] = i * data_settings[1]

data_on = data_time[np.where(data_voltage == data_voltage.max())][0]
data_off = data_time[-1] - data_on

fig, ax = plt.subplots(figsize=(16, 10), dpi=500)

ax.axis([data_time.min(), data_time.max() + 1, data_voltage.min(), data_voltage.max() + 0.2])

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

ax.set_title("\n".join(wrap('Процесс зарядки и разрядки конденсатора в RC-цепочке')), loc = 'center')

ax.grid(which='major', color = 'k')
ax.grid(which='minor', color = 'b', linestyle = ':')

ax.set_xlabel('t, с', fontsize = 16)
ax.set_ylabel('V, В', fontsize = 16)

ax.plot(data_time, data_voltage, 'r-', label = "V(t)", marker = '+', mec = 'b', mfc = 'w', markevery = 20, markersize = 15)
ax.legend(shadow = False, loc = 'upper right', fontsize = 20)

ax.text(6, 2.6, "Време зарядки - {:.2f} s".format(float(data_on)), fontsize = 14)
ax.text(6, 2.3, "Время разрядки - {:.2f} s".format(float(data_off)), fontsize = 14)

plt.savefig("figure.svg")
fig.savefig("figure.png")
plt.show()