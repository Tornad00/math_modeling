import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (0, 5, 0.01)

def Kol(N, t):
  dNdt = k * N
  return dNdt

N_0 = 10
k = 5

Bact = odeint (Kol, N_0, t)

plt.plot(t, Bact[:, 0], label = "сколько бактерий?")
plt.show()