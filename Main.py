import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as plt3d

T = 0
R = 0 
M = 0
omega = 0

fig = plt.figure()
ax = plt3d.Axes3D(fig)


T = float(input("Напишите температуру звезды в кельвинах: "))
M = float(input("Напишите массу звезды: "))
R = float(input("Напишите радиус звезды: "))
omega = float(input("Напишите угловое вращение звезды: "))
Msol = 2 * 10 ** 30
Rsol = 7 * 10 ** 8

N = 100
Q = np.linspace(0, 2*np.pi, 100)  
fi = np.linspace(0, np.pi, 100)   
# Параметрическое задание пространственной кривой

x = R * np.outer(np.sin(Q), np.cos(fi))
y = R * np.outer(np.sin(Q), np.sin(fi))
z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

if T > 30000:
  ax.plot_surface(x, y, z, color = "#1CACF4")
  print (z)

elif T > 10000:
  ax.plot_surface(x,y,z, color = "#ACE3E4")

elif T > 7500:
  ax.plot_surface(x,y,z, color = "#DCECFC")

elif T > 6000:
  ax.plot_surface(x,y,z, color = "#FCFC54")

elif T > 5200:
  ax.plot_surface(x,y,z, color = "#F9E506")

elif T > 3700:
  ax.plot_surface(x,y,z, color = "#FC7C1C")

elif T > 2700:
  ax.plot_surface(x,y,z, color = "#DB4C23")

else:
  print("Иди нафиг")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

	
# Подпись графика
ax.set_title('3D Test')

plt.show()