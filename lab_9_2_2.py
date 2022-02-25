import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (1, 24, 1)

def rost(S, t):
  dsdt = k * np.sqrt(S / np.pi) * E * S * np.cos((np.pi / 12)*(t - 12 ))
  return dsdt

E = 1367
S_0 = 16
k = 340 * 10 **(-8)
padenii = odeint (rost, S_0, t)

plt.plot(t, padenii[:, 0])
plt.show()