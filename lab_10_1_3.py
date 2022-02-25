import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def diff_func(fuk, x):
  f, y = fuk
  df_dx = f
  dy_dx = np.sin(x) + np.cos(x) * f
  return df_dx, dy_dx
  
f0 = 0
y0 = 3
fuk0 = f0, y0

sol = odeint(diff_func, fuk0, x)

plt.plot(x, sol[:, 1], "b", label="y(t)")
plt.legend()
plt.show()
