import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import imageio
import os

# T = float(input('Температура: '))
# M = float(input("Macca: "))
# R = float(input("Радиус: "))
# omega = float(input("Угол: "))

T = 50000
M = 3e35
R = 7e10
omega = 10
N = 10

fig = plt.figure()
ax = plt3d.Axes3D(fig)

fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
Msol = 1.9885 * 10 ** 30
Rsol = 6.9551 * 10 ** 8
Msol1 = Msol * 60
Rsol1 = Rsol * 15

x = R * np.outer(np.sin(Q), np.cos(fi)) 
y = R * np.outer(np.sin(Q), np.sin(fi))
z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

color1 = [0.109, 0.674, 0.956]

for i in range(N):
  ax.set_xlim3d([-2*R, 2*R])
  ax.set_xlabel('X')
 
  ax.set_ylim3d([-2*R, 2*R])
  ax.set_ylabel('Y')
 
  ax.set_zlim3d([-2*R, 2*R])
  ax.set_zlabel('Z')
  
  if T > 30000:
    ax.plot_surface(x, y, z, color = color1)

  elif T > 10000 and T < 30000:
    ax.plot_surface(x,y,z, color = (172, 227, 228))

  elif T > 7500 and T < 10000:
    ax.plot_surface(x,y,z, color = (220, 236, 252))

  elif T > 6000 and T < 7500:
    ax.plot_surface(x,y,z, color = (252, 252, 84))

  elif T > 5200 and T < 6000:
    ax.plot_surface(x,y,z, color = (249, 229, 6, 1))

  elif T > 3700 and T < 5200:
    ax.plot_surface(x,y,z, color = (252, 124, 28, 1))

  elif T > 2700 and T < 3700:
    ax.plot_surface(x,y,z, color = (219, 76, 35, 1))
  else: 
    print("иди нафиг")

  plt.savefig(f'pic_{i}')
  color1[0] += 0.03
  color1[2] += -0.02
  color1[1] += -0.01
    
images = []
filenames = [f'pic_{i}.png' for i in range(N)] 
for filename in filenames:
  images.append(imageio.imread(filename))
  os.remove(filename)
imageio.mimsave('movie.gif', images)