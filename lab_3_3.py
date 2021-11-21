import numpy as np
import const as co

x = float(input("введите значение X0 = "))
y = float(input("введите значение Y0 = "))
v = float(input("введите значение V0 = "))
t = np.arange(0, 6, 1)

while t == 5:
  x = x + v * t