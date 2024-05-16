import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
arduino = serial.Serial('COM10', 9600, timeout=1)  
temp_ranges = [20, 25, 30, 35, 40, 45]  
colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red']
cmap = LinearSegmentedColormap.from_list('custom_cmap', list(zip(np.linspace(0, 1, len(temp_ranges)), colors)))
fig, ax = plt.subplots()
img = ax.imshow(np.zeros((8, 8)), cmap=cmap, interpolation='bilinear')  
cbar = plt.colorbar(img, ax=ax)
cbar.set_label('Temperature (°C)', fontsize=12)
cbar.set_ticks(np.linspace(0, 1, len(temp_ranges)))  
cbar.set_ticklabels(['Cold', 'Cool', 'Moderate', 'Warm', 'Hot', 'Very Hot']) 
cbar.ax.tick_params(labelsize=10) 
cbar.ax.yaxis.set_tick_params(width=1) 
def update_plot(thermal_data):
    ax.clear()
    ax.set_xticks(np.arange(-0.5, 8.5, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8.5, 1), minor=True)
    ax.grid(which='minor', color='k', linestyle='-', linewidth=2)
    img = ax.imshow(thermal_data, cmap=cmap, interpolation='bilinear')
    plt.pause(0.01)
while True:
    data = arduino.readline().decode().strip()
    data = data.rstrip(',')
    if data:
        try:
            thermal_data = np.array(data.split(','), dtype=float).reshape((8, 8))
            update_plot(thermal_data)
        except ValueError:
            print("Error converting data:", data) 
arduino.close()

plt.show() 
