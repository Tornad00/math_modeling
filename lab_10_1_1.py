import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def diff_func(fuk, x):
  y, z = fuk
  dy_dx = y ** 2 * z 
  dz_dx = z / x - y * z**2
  return dy_dx, dz_dx

y0 = 1
z0 = -3
fuk0 = y0, z0

sol = odeint(diff_func, fuk0, x)

plt.plot( x,sol[:, 1], "b", label="y(x)")
plt.plot(x, sol[:, 0], "g", label="z(x)")
plt.legend()
plt.show()
