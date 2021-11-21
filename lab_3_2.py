import const as co
import numpy as np
import math as mt

h = 100
a = co.PI / 3
B = 0.52
g = co.g
T = 200 
eps = 300

v = np.sqrt( (h * g * np.tan(B)**2) / (2 * np.cos(a)**2 * (1- np.tan(B) * np.tan(a))) )
print(v)

n=(2/np.sqrt(co.PI))*(co.h/np.sqrt((co.k*T)**(3)))*(eps**-1)*(eps**(T/2))
##так как стпень: (-eps/(co.k*T)) = -1.086445577405988e+23, имеет слишком много знаков после запятой представим ее как -1, округлим. Иначе у нас получится ноль и вся формула будет равна нулю##
print(n)