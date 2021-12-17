import const as ct 
import numpy as np 

def name_en(v, h, m):
  E = m * v ** 2 / 2 + m * ct.g * h
  print(E)
name_en(4, 9, 3)