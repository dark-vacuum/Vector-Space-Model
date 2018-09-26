import numpy as np
import matplotlib.pyplot as plt

data = [(3,5),(7,8.8),(2.5,1.4),(9,8),(13,18),(1.1,8.8), (6,10)]
data.sort()

size = len(data)
x = np.zeros(size)
y = np.zeros(size)

for i in range(len(x)):
    tuple = data[i]
    x[i] = tuple[0]

for i in range(len(y)):
    tuple = data[i]
    y[i] = tuple[1]

plt.plot(x, y)
plt.title('La grafica papu')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')
plt.show()
