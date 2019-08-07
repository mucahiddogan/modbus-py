try:
    import Tkinter as tk
except:
    import tkinter as tk

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "REMOTEIPADRESI"
SERVER_PORT = 502

c = ModbusClient()

c.host(SERVER_HOST)
c.port(SERVER_PORT)

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def toggle(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        t_btn.config(text='False')
        is_ok = c.write_single_coil(0, tog[0])
        print(tog[0])
    else:
        t_btn.config(text='True')
        is_ok = c.write_single_coil(0, tog[0])
        print(tog[0])

def animate(i):
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    if c.is_open():
        regs = c.read_holding_registers(0, 2)
        if regs:
            print("a")
    veri = open('veri.txt', 'a')
    print(regs)
    reg = str(regs)
    reg = reg.replace("[", "").replace("]", "")
    veri.write(reg)
    veri.write("\n")
    graph_data = open('veri.txt', 'r').readlines()
    #lines = graph_data.split('\n')
    lines = graph_data[-15:]
    print(lines)
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
        ax1.clear()
        ys.sort()
        ax1.plot(xs, ys)

t_btn = tk.Button(text="True", width=12, command=toggle)
t_btn.pack(pady=5)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
# root.mainloop()

time.sleep(1)

