import numpy as np
import matplotlib.pyplot as plt

data = [(0,5),(10,8.8),(20,1.4),(30,8),(40,18),(50,8.8), (60,10), (70,10), (80,30), (90,40), (100,60)]
data.sort()

size = len(data)
x = np.zeros(size)
y = np.zeros(size)

for i in range(size):
    (x[i], y[i]) = data[i]
    
plt.plot(x, y)
plt.title('La grafica papu')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')
plt.show()
