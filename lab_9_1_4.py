import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

def teg(v, t):
  dvdt = (b - k * v) / m
  return dvdt

m = 10
b = 1
k = 2
v_0 = 0

sila = odeint(teg, v_0, t)

plt.plot(t, sila[:, 0])
plt.show()