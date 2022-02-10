import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arrange(0, 10 ** 6, 100)

def razm_fuction(a, t):
  a = k * p
  return kol

p = 2
k = 2

razm = odeint(razm_fuction, p, t)
plt. plot(t, razm[:, 0], label = 'число бактерий')
plt.xlabel ("прошедшее время")
plt.ylabel ("кол-во бактерий")
plt.legend

plt.show