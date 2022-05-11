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
N = 65
O = 2
r = R/2

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
color2 = [0.67, 0.89, 0.894]
color3 = [0.94, 1, 1]
color4 = [0.826, 0.862, 0.509]
color5 = [0.967, 0.898, 0.02]
color6 = [0.988, 0.486, 0.109]
color7 = [1, 0.345, 0.345]

ax.set_xlim3d([-14e10, 14e10])
ax.set_xlabel('X')
 
ax.set_ylim3d([-14e10, 14e10])
ax.set_ylabel('Y')
 
ax.set_zlim3d([-14e10, 14e10])
ax.set_zlabel('Z')

for i in range(N):
  
  if T > 30000:
    ax.plot_surface(x, y, z, color = color1)

  elif T > 10000 and T < 30000:
    ax.plot_surface(x,y,z, color = color2)

  elif T > 7500 and T < 10000:
    ax.plot_surface(x,y,z, color = color3)

  elif T > 6000 and T < 7500:
    ax.plot_surface(x,y,z, color = color4)

  elif T > 5200 and T < 6000:
    ax.plot_surface(x,y,z, color = color5)

  elif T > 3700 and T < 5200:
    ax.plot_surface(x,y,z, color = color6)

  elif T > 2700 and T < 3700:
    ax.plot_surface(x,y,z, color = color7)
  else: 
    print("иди нафиг")

  if O <= 20:
    x = x * 1.03
    y = y * 1.03
    z = z * 1.03
    R = R * 1.03
    O += 1
  elif O >= 21 and O < 34:
    x = x / 2
    y = y / 2
    z = z / 2
    R = R / 2
    O += 1 
  elif O >= 34 and O <= 40:
    x = x * 50
    y = y * 50
    z = z * 50
    R = R * 50
    O += 1
  elif O > 41 and O < 52:
    x = x * 1e(-40)
    y = y * 1e(-40)
    z = z * 1e(-40)
    R = R * 1e(-40)
    O += 1
  elif r > R and O => 52 and O < 65:
    x = r * np.outer(np.sin(Q), np.cos(fi)) 
    y = r * np.outer(np.sin(Q), np.sin(fi))
    z = r * np.outer(np.cos(Q), np.ones(np.size(fi)))
    R = 3.5e10
    O += 1
    
    
  if color1[0] < 0.8: 
    color1[0] += 0.06
    color1[2] += -0.0637333333333333
    color1[1] += -0.0449333333333333
  else: 
    color1 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026]

  if color2[0] < 0.8:
    color2[0] += 0.01
    color2[1] -= 0.05
    color2[2] -= 0.05
  else:
    color2 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026]
  
  if color3[1] > 0.2:
    color3[0] += 0
    color3[1] -= 0.066
    color3[2] -= 0.066
  else:
    color3 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026]
  
  if color4[1] > 0.2:
    color4[0] += 0 
    color4[1] -= 0.057
    color4[2] -= 0.033
  else:
    color4 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026]
  
  if color5[1] > 0.2:
    color5[0] += 0
    color5[1] -= 0.59
    color5[2] += 0
  else:
    color5 = [0.967, 0.15, 0.02]
  
  if color6[1] > 0.2:
    color6[0] += 0 
    color6[1] -= 0.0324
    color6[2] += 0
  else:
    color6 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026]
  
  if color7[1] > 0.1:
    color7[0] += 0 
    color7[1] -= 0.001
    color7[2] += 0.001
  else:
    color7 = [1, 0.1, 0.1]

  

  plt.savefig(f'pic_{i}')
  
  #print(color1, " ")
  #print(color2, " ")
  #print(color3, " ")
  #print(color4, " ")
  #print(color5, " ")
  #print(color6, " ")
  #print(color7, " ")
  
images = []
filenames = [f'pic_{i}.png' for i in range(N)] 
for filename in filenames:
  images.append(imageio.imread(filename))
  os.remove(filename)
imageio.mimsave('movie.gif', images)