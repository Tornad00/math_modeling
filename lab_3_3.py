import numpy as np
import const as co

x = float(input("введите значение X0 = "))
y = float(input("введите значение Y0 = "))
v = float(input("введите значение V0 = "))


for t in range(6):
  x = x + v * t
  y = y + v * t - (co.g * t ** 2 / 2)
  print(f't = {t} x = {x} y = {y}')