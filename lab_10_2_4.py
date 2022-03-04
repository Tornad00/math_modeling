import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)

def diff_func(fuk, x):
  t, y = fuk
  dt_dx = t
  dy_dx = - ((x * t + (4 * x ** 2 + 0.5) * y) / x ** 2)
  return dt_dx, dy_dx
  
t0 = 0
y0 = 1
fuk0 = t0, y0

sol = odeint(diff_func, fuk0, x)

plt.plot( sol[:, 0], sol[:, 1], "b", label="y(t)")
plt.legend()
plt.show()
