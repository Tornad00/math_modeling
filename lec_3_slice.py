import numpy as np

a = [1, 5, 3, 6]
slise = a[0:2:1]
print(slise)

slise = a[3:0:-1]
print(slise)

slise = a[::-1]
print(slise)

b = np.array([a, np.array(a)*3])
print(b)

slise =  [::, 1]
print(slise)

slise = b[1,2:3:1]
print(slise)

slise = b[1, 2::1]
print(slise)