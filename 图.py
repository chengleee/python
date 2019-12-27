import matplotlib.pyplot as py
import numpy as np
x = np.linspace(0, 2*np.pi, 1024)
py.ylim(-4, 4)

py.plot(x, x, 'r')

py.plot(x, np.tan(x), 'b')

py.plot(x, np.sin(x), 'y')

py.show()
