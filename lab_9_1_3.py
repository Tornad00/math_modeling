import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (0, 5, 0.01)

def Kol(v, t):
  dvdt = a_0 - ((y * v**2)/m)
  return dvdt

v_0 = 0
y = 10
m = 10

Bact = odeint (Kol, N_0, t)

plt.plot(t, Bact[:, 0], label = "сколько бактерий?")
plt.show()