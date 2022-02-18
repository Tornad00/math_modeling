import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (0, 4, 0.5)

def inv(A, t):
  dNdt = -k * A * t
  return dNdt

A_0 = 1000
k = 0.8

Den = odeint (inv, A_0, t)

plt.plot(t, Den[:, 0], label = "Сколько денег?")
plt.show()