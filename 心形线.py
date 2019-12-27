import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,2 * np.pi,1024)
plt.axes(polar = True)
plt.plot(t,1.0 + np.cos(t),color = 'r')
plt.show()
