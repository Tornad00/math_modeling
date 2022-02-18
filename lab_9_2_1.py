
m = 10
h = 20
v_0 = 0

sila = odeint(pad, v_0, t)

plt.plot(t, sila[:, 0])
plt.show()