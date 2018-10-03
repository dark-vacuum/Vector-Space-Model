import numpy as np
import matplotlib.pyplot as plt

#<<<<<<< HEAD
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
    def __init__(self, data):
        self.data = data

    def printGraph(self):
        size = len(self.data)
        x = np.zeros(size)
        y = np.zeros(size)
        q = np.zeros(size)
        for i in range(size):
            print(self.data[i])
            (q[i], x[i], y[i]) = self.data[i]

        
            plt.plot(x, y)
            plt.title('Presition & Recall graph')
            plt.xlabel('Recall')
            plt.ylabel('Presition')
            plt.show()
#>>>>>>> e3284bf981624e3f57b9eaadd26fbc3907213c4d
