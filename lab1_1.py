import matplotlib.pyplot as plt
import numpy as np

f='Цикл.(c) или астр.(a)'

def grf(f,R):
  if f == 'c':
    t = np.arange (-4*np.pi, 4*np.pi, 0.01)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
  elif f == 'a':
    t = np.arange (-2*np.pi, 2*np.pi, 0.01)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
  plt.axis('equal')
  plt.show()
grf(f='c',R=3)
