import numpy as np

a = -3
b = 0
n = 50

def name(a, b, n):
  x = np.linspace(a, b, n)
  y = x ** 2
  print(y)

name(a, b, n)