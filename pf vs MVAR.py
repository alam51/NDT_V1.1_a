import numpy as np
import matplotlib.pyplot as plt

pf = np.arange(start=1.0, stop=0.75, step=-.0001)
print(pf)
P = 100
a = pf**-2
Q = P * np.sqrt(pf**-2 - 1)
b = 5
plt.plot(pf, Q)
plt.grid(True)
plt.show()
