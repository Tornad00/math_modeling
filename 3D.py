import numpy as np
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = plt3d.Axes3D(fig)

t = np.arange(0.01, 10 * np.pi, 0.01)
R = 5

x = R * np.cos(t)
y = R * np.sin(t)
z = R * t

ax.plot(x,y,z, label = "Dich")

ax.legend()

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("3D TEST")

plt.show()
