import serial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import time
from datetime import datetime

def init_arduinos():
    sensor_1 = serial.Serial("/dev/ttyUSB0",9600)
    sensor_2 = serial.Serial("/dev/ttyUSB1",9600)
    return (sensor_1,sensor_2)

def read_value(arduinos):
    lines = []
    for arduino in arduinos:
        arduino:serial.Serial
        arduino.write(bytes('S'.encode("utf-8")))
        print("sending signal to A")
        reading = ""
        while "\n" not in reading:
            reading = reading + arduino.readline().decode("utf-8")
        lines.append(reading)
    try:
        file.write(lines[0].strip()+"|"+lines[1])
        file.flush()
    except Exception as e:
        print("Error",e)
    return lines

def parsing_data(lines):
    L = []
    R = []
    for line in lines:
        line:str
        values = line.split(",")
        if values[0] == "L":
            [L.append(int(i)) for i in values[1:]]
        else:
            [R.append(int(i)) for i in values[1:]]
    return L+R

def plt_data(fig,line,data):
    x = [i for i in range(12)]
    line.set_xdata(x)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()

def animate(i):
    data = read_value((s1,s2))
    data = parsing_data(data)

    x = [i for i in range(12)]
    index = 0
    for r in gra:
        r.set_height(data[index])
        index+=1
    return gra

def init():
    return gra

s1,s2 = init_arduinos()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim((0,255))
gra = ax.bar([i for i in range(12)],[i for i in range(12)])
now = datetime.now()
file_name = "%s_%s_%s:%s:%s_data.txt" %(now.year, now.month, now.day, now.hour, now.minute)
file = open("./"+file_name,"w+")
anim = animation.FuncAnimation(fig,animate,init_func=init,frames=200,interval=500,blit=False)
plt.show()

file.close()