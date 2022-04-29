import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def nachalo():
  T = input("Напишите температуру звезды в кельвинах: ")
  M = input("Напишите массу звезды: ")
  R = input ("Напишите радиус звезды: ")
  omega = input("Напишите угловое вращение звезды: ")
  return (T, M, R, omega)

if T > 30000 and M > 60 * Msol and R > 15 * Msol:
  