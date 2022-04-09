import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
second_in_year = 365 * 24 * 60 * 60
second_in_day = 24 * 60 * 60 
years = 2
t = np.linspace(0, years*second_in_year, frames)

def move_func(s,t):
  (x1, v_x1, y1, v_y1,
   x2, v_x2, y2, v_y2,
   x3, v_x3, y3, v_y3,
   x4, v_x4, y4, v_y4) = s

  dxdt1 = v_x1
  print(f'dxdt1: {dxdt1}')
  print(f'line1:{-G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5}')
  print(f'line2:{-G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5}')
  print (f'line3:{+ k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5}')
  print(f'line4:{+ k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5}')
  dv_xdt1 = (-G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             -G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
             + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            )
  print(f'dv_xdt1: {dv_xdt1}')
  dydt1 = v_y1
  print(f'dydt1: {dydt1}')
  dv_ydt1 = (-G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             -G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
             + k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            )
  print(f'dv_ydt1: {dv_ydt1}')
  dxdt2 = v_x2
  print(f'dxdt2: {dxdt2}')
  dv_xdt2 = (-G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             -G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
             + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
            )
  print(f'dv_xdt2: {dv_xdt2}')
  dydt2 = v_y2
  print(f'dydt2: {dydt2}')
  dv_ydt2 = (-G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             -G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
             + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
            )
  print(f'dv_ydt2: {dv_ydt2}')
  dxdt3 = v_x3
  print(f'dxdt3: {dxdt3}')
  dv_xdt3 = (-G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             -G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
             + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             + k * q3 * q1 / m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            )
  print(f'dv_xdt3: {dv_xdt3}')
  dydt3 = v_y3
  print(f'dydt3: {dydt3}')
  dv_ydt3 = (-G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             -G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
             + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            )
  dxdt4 = v_x4
  dv_xdt4 = - G * m1 * x4 / (x4 ** 2 + y4 ** 2) ** 1.5
  dydt4 = v_y4
  dv_ydt4 = - G * m1 * y4 / (x4 ** 2 + y4 ** 2) ** 1.5

  print(f'dv_ydt3: {dv_ydt3}')
  return (dxdt1, dv_xdt1, dydt1,dv_ydt1,
          dxdt2, dv_xdt2, dydt2,dv_ydt2,
          dxdt3, dv_xdt3, dydt3,dv_ydt3,
          dxdt4, dv_xdt4, dydt4,dv_ydt4)

x10 = 0
v_x10 = -4300
y10 = 0
v_y10 = -4368

x20 = -149 * 10**9 * 12.3
v_x20 = 0
y20 = 0
v_y20 = -6000

x30 = -149 * 10**9 * 11.63
v_x30 = 4000
y30 = 0
v_y30 = 0

x40 = 0.387 * 147 * 10 **9
v_x40 = 0
y40 = 0
v_y40 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40)

m1 = 1.06 * 10**30
q1 = 0

m2 = 0.96 * 10**30
q2 = 0

m3 = 0.68 * 10**30
q3 = 0

G = 6.67 * 10**(-11)
k = 9 * 10**9

sol = odeint(move_func, s0, t)

fig, ax =plt.subplots()

balls =[]
balls_lines = []

for i in range (4):
  balls.append(plt.plot([], [], 'o', color="r"))
  balls_lines.append(plt.plot([], [], '-', color = "r"))
                 
def animate(i):
  for j in range (4):
    balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
    balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])

ani = FuncAnimation(fig,
                 animate,
                 frames=frames,
                 interval=30)

plt.axis('equal')
edge = 1.5 * x20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save("poluchiloc.gif")