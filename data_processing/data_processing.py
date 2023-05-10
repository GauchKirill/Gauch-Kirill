#https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
#https://cpp-python-nsu.inp.nsk.su/textbook/sec4/ch8
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

with open("settings.txt", "r") as settings:
    data_settings = np.array([float(i) for i in settings.read().split("\n")])
data_array = np.loadtxt("data.txt", dtype = int)

size = data_array.size
data_time = np.empty((size))
data_voltage = np.empty((size))
for i in range(size):
    data_voltage[i] = data_settings[0] * data_array[i]
    data_time[i] = i * data_settings[1]

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
ax.plot(data_time, data_voltage, 'r-', label = "V(t)", marker = '+', mec = 'b', mfc = 'w', markevery = 20, markersize = 10)
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
plt.xlabel('t, с', fontsize = 12)
plt.ylabel('V, мВ', fontsize = 12)
plt.title('Процесс зарядки и разрядки конденсатора в RC-цепочке')
ax.legend()
plt.savefig("figure.svg")
fig.savefig("figure.png")
plt.show()