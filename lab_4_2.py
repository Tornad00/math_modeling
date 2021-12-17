import numpy as np

m = np.zeros (5)

m[0] = input("первое ")
m[1] = input("второе ")
m[2] = input("третье ")
m[3] = input("четвёртое ")
m[4] = input("пятый ")

def name_mn(m):
  e = len(m)
  ee = 2
  for i in range(e):
    ee *= m[i]
  print (ee*e)  

name_mn(m)