import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 50, frames) 

def move_function(fuk, t):
  x, y = fuk
  dxdt = (m - x - y) * k1
  dydt = (m - x - y) * k2
  return dxdt, dydt


v = 15
m = 10
k1 = 0.2
k2 = 0.5
x0 = 0
y0 = 0

fuk0 = x0, y0

sol = odeint(move_function, fuk0, t)

plt.plot(t,sol[:, 1], "b", label="y(x)")
plt.plot(t, sol[:, 0], "g", label="z(x)")
plt.legend()
plt.show()