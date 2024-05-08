import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import animation

pontos = pd.read_csv("CORD.csv",sep=";")        
x = pontos.X
y = 300-pontos.Y

fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(0, 300))
line, = ax.plot([], [], "-r",lw=2)

xx = []
yy = []

def animate(i):
    xx.append(x[i])
    yy.append(y[i])
    line.set_data(xx, yy)
    return line,

anim = animation.FuncAnimation(fig, animate, frames=75, interval=80)
plt.show()

pp = anim.to_html5_video()
display.HTML(pp)
