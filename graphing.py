import numpy as np
import matplotlib.pyplot as plt

#<<<<<<< HEAD
data = [(0,5),(10,8.8),(20,1.4),(30,8),(40,18),(50,8.8), (60,10), (70,10), (80,30), (90,40), (100,60)]
data.sort()
#=======
class Graphing:
#>>>>>>> e3284bf981624e3f57b9eaadd26fbc3907213c4d

    '''
    data = [(3,5),(7,8.8),(2.5,1.4),(9,8),(13,18),(1.1,8.8), (6,10)]
    data.sort()

<<<<<<< HEAD
for i in range(size):
    (x[i], y[i]) = data[i]

plt.plot(x, y)
plt.title('La grafica papu')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las y')
plt.show()
=======
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
    '''
    def __init__(self, vsm):
        self.data = vsm

    def printGraph(self):
        print("HOLa papu")
#>>>>>>> e3284bf981624e3f57b9eaadd26fbc3907213c4d
