import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 15, frames) 

def move_function(z, t):
    y, v_y = z
    dydt = v_y
    dv_ydt = v_y + F
    return dydt, dv_ydt

g = 9.8
v = 0
m = 0.5
F = m * g
g = 9.98
a = 8000/92.5

x0 = 0
x_0_0 = 0
y0 = 0
v_y0 = v * a 

z0 = y0, v_y0

sol = odeint(move_function, z0, t)

plt.plot(t,sol[:, 0], "b", label="y(l)")
plt.plot(t, sol[:, 1], "g", label="z(x)")
plt.legend()
plt.show()