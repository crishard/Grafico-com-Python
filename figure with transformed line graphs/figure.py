import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.sin(t ** 2) + np.cos(t ** 2)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(t2*np.pi), 'r--')

plt.savefig('figure2.jpeg')
plt.show()