import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def diff_func(z, t):
  theta, omega = z
  dtheta_dt = omega
  domega_d = -b * omega - c * np.sin(theta)
  return dtheta_dt, domega_d

theta0 = np.pi - 0.1
omega0 = 0
z0 = theta0, omega0
b = 0.25
c = 5.0

sol = odeint(diff_func, z0, t)

plt.plot( sol[:, 1],sol[:, 0], "b", label="theta(omega)")

plt.legend()
plt.show()
