import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.1)

def diff_func(fuk, t):
  x, y = fuk
  dx_dt = 3 * x - 2 * y + (np.e ** (3*t)) / np.e ** t + 1 
  dy_dt = x - (np.e ** (3*t)) / np.e ** t + 1 
  return dx_dt, dy_dt
  
x0 = 5
y0 = -7
fuk0 = x0, y0

sol = odeint(diff_func, fuk0, t)

plt.plot(t, sol[:, 1], "b", label="y(t)")
plt.plot(t, sol[:, 0], "g", label="x(t)")
plt.legend()
plt.show()
