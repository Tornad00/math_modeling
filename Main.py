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
Msol = 2 * 10
Rsol = 7 * 10

N = 100
theta = np.linspace(0, 2*np.pi, 100)  
phi = np.linspace(0, np.pi, 100)   
# Параметрическое задание пространственной кривой

x = np.sin(phi)*np.cos(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(phi)

if M > Msol * 60 and Rsol * 15 and T > 30000:
  
  ax.plot_surface(x, y, z, color = "#1CACF4")

elif M > Msol * 18 and M < Msol * 60 and Rsol > 7.5 * Rsol and R < Rsol * 15 and T > 10000:
  ax.plot_surface(x,y,z, color = "#ACE3E4")

elif M > Msol * 3.1 and M < Msol * 18 and Rsol > 2.1 * Rsol and R < Rsol * 7.5 and T > 7500:
  ax.plot_surface(x,y,z, color = "#DCECFC")

elif M > Msol * 1.7 and M < Msol * 3.1 and Rsol > 1.3 * Rsol and R < Rsol * 2.1 and T > 6000:
  ax.plot_surface(x,y,z, color = "#FCFC54")

elif M > Msol * 1.1 and M < Msol * 1.7 and Rsol > 1.1 * Rsol and R < Rsol * 1.3 and T > 5200:
  ax.plot_surface(x,y,z, color = "#F9E506")

elif M > Msol * 0.8 and M < Msol * 1.1 and Rsol > 0.9 * Rsol and R < Rsol * 1.1 and T > 3700:
  ax.plot_surface(x,y,z, color = "#FC7C1C")

elif M > Msol * 0.3 and M < Msol * 0.8 and Rsol > 0.4 * Rsol and R < Rsol * 0.9 and T > 2700:
  ax.plot_surface(x,y,z, color = "#DB4C23")

else:
  print("Иди нафиг")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

	
# Подпись графика
ax.set_title('3D Test')

plt.show()