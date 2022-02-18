import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (0, 4, 0.5)

def invI, t):
  dNdt = -k * I * t
  return dNdt

I_0 = 1000
k = 0.8

Den = odeint (inv, I_0, t)

plt.plot(t, Den[:, 0], label = "Сколько денег?")
plt.show()