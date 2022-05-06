import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm     #import package to calculate spherical harmonics

theta = np.linspace(0, 2*np.pi, 100)   #setting range for theta
phi = np.linspace(0, np.pi, 100)       #setting range for phi
phi, theta = np.meshgrid(phi, theta)   #setting the grid for phi and theta

#Setting the cartesian coordinates of the unit sphere
#Converting phi, theta, z to cartesian coordinates
x = np.sin(phi)*np.cos(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(phi)

m, l = 4, 4   #m and l control the mode of pulsation and overall appearance of the figure

#Calculating the spherical harmonic Y(l,m) and normalizing it
figcolors = sph_harm(m, l, theta, phi).real
figmax, figmin = figcolors.max(), figcolors.min()
figcolors = (figcolors-figmin)/(figmax-figmin)

#Setting the aspect ratio to 1 which makes the sphere look spherical and not elongated
fig = plt.figure(figsize=plt.figaspect(1.))    #aspect ratio
axes = fig.add_subplot(111, projection='3d')   #sets figure to 3d

#Sets the plot surface and colors of the figure where seismic is the color scheme
axes.plot_surface(x, y, z,  rstride=1, cstride=1,  facecolors=cm.autumn(figcolors))
#yellow zones are cooler and compressed, red zones are warmer and expanded

axes.set_axis_off()
fig.suptitle('m=4   l=4', fontsize=18, x=0.52, y=.85)

for idx, angle in enumerate(np.linspace(0, 360, 10)):

    axes.view_init(30, angle)
    plt.draw()

    #Turn off the axis planes so only the sphere is visible


    plt.savefig('m4_l4-%04d.png' % idx)          #saves a .png file of my figure
plt.show()  