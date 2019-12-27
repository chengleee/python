import matplotlib.pyplot as plt
import numpy as np
x = np.arange( - np.pi/4,np.pi/4)
plt.plot(x,pow(x,8),color = 'r')
plt.plot(x,pow(np.sin(x),8),color = 'b')
plt.show()
