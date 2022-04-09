import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
second_in_year = 365 * 24 * 60 * 60
second_in_day = 24 * 60 * 60 
years = 0.5
t = np.linspace(0, years*second_in_year, frames)

def move_func(s,t):
  (x1, v_x1, y1, v_y1,
   x2, v_x2, y2, v_y2,
   x3, v_x3, y3, v_y3
   x4, v_x4, y4, v_y4) = s

  dxdt1 = v_x1
  dv_xdt1 = (-G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             -G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            )
  dydt1 = v_y1
  dv_ydt1 = (-G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
             -G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            )
  dxdt2 = v_x2
  dv_xdt2 = (-G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             -G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
            )
  dydt2 = v_y2
  dv_ydt2 = (-G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
             -G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
            )
  dxdt3 = v_x3
  dv_xdt3 = (-G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             -G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            )
  dydt3 = v_y3
  dv_ydt3 = (-G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
             -G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            )
  