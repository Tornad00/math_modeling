import const as co
import numpy as np

h = 100
a = co.PI / 3
B = 0.52
g = co.g

v = np.sqrt( (h * g * np.tan(B)**2) / (2 * np.cos(a)**2 * (1- np.tan(B) * np.tan(a))) )
print(v)

N