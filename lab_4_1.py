import numpy as np 

a = np.zeros (3)

a[0] = input("введите первое значение ")
a[1] = input("введите второе значение ")
a[2] = input("введите третье значение ")

def task(a):
  s = len(a)
  ss = 0
  for i in range (s):
    ss += a[i]
  print (ss/s)

task(a)