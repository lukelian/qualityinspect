import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(x),np.sin(x)
plt.plot(x,C)
plt.plot(x,S)
plt.show()