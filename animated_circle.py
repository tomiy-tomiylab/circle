import numpy as np
import matplotlib.pyplot as plt
import math
import time

class circle():

    def __init__(self):
        self.circle_plt = plt
        self.ax, self.fig = self.circle_plt.subplots()
        self.fig.set_aspect('equal')
        self.x = np.array([])
        self.y = np.array([])

        for i in np.linspace(0, 2 * np.pi, 1000):
            self.x = np.append(self.x, math.cos(i))
            self.y = np.append(self.y, math.sin(i))

    def plot(self, cx, cy, r):

        x_plot = self.x * r + cx
        y_plot = self.y * r + cy
        red = "#ff0000"
        cyan = "#00ffff"
        black = "#000000"
        self.fig.grid()
        self.fig.set_xlim(-2, 8)
        self.fig.set_ylim(-2, 8)
        self.fig.hlines(y=0, xmin=-2, xmax=8, color=black)
        self.fig.vlines(x=0, ymin=-2, ymax=8, color=black)
        self.fig.plot(x_plot, y_plot, color=red)
        self.fig.plot(cx, cy, marker='.', color=cyan)
        plt.pause(.001)
        self.fig.cla()


    def close(self):
        self.circle_plt.close()


circle = circle()

start_time = time.time()
while True:
    for a in np.linspace(1, 2, 100, endpoint=True):
        x = a
        y = a * 2
        r = (5 * (a ** 2 - 2 * a + 2)) ** 0.5
        circle.plot(x, y, r)
    for b in np.linspace(1, 2, 100, endpoint=True):
        a = 3 - b
        x = a
        y = a * 2
        r = (5 * (a ** 2 - 2 * a + 2)) ** 0.5
        circle.plot(x, y, r)

    now_time = time.time()
    if now_time - start_time > 30:
        circle.close()
        break
