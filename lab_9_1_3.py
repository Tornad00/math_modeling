import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (0, 5, 0.01)

def skr(v, t):
  dvdt = F / m - gamma * v ** 2 / m
  return dvdt

v_0 = 10
gamma = 0.1
F = 1
m = 5

padenii = odeint (skr, v_0, t)

plt.plot(t, padenii[:, 0])
plt.show()