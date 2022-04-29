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

def nachalo(T, M, R, omega):
  T = input("Напишите температуру звезды в кельвинах: ")
  M = input("Напишите массу звезды: ")
  R = input ("Напишите радиус звезды: ")
  omega = input("Напишите угловое вращение звезды: ")
  return (T, M, R, omega)
  
nachalo(T, M, R, omega)

fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
Msol = 1.9885 * 10 ** 30
Rsol = 6,9551 * 10 ** 8

if T > 30000 and M > 60 * Msol and R > 15 * Rsol:
  x = R * np.outer(np.sin(Q), np.cos(fi))
  y = R * np.outer(np.sin(Q), np.sin(fi))
  z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

  ball, = ax.plot(x, y, z, 'o', color='b') # Сферический объект
  line, = ax.plot(x, y, z, '-', color='b') # Линия
 
# Функция подстановки координат в анимируемые объекты
  def animate(i):
      ball.set_data(x[:i], y[:i])
      ball.set_3d_properties(z[:i])
 
      line.set_data(x[i], y[i])
      line.set_3d_properties(z[i])
 
# Украшательсвта и масштабирование
  ax.set_xlim3d([-1.0, 1.0])
  ax.set_xlabel('X')
 
  ax.set_ylim3d([-1.0, 1.0])
  ax.set_ylabel('Y')
 
  ax.set_zlim3d([-1.0, 1.0])
  ax.set_zlabel('Z')
 
  ani = FuncAnimation(fig, animate, N, interval=50)
 
  ani.save('Класс О.gif')