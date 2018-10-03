import numpy as np
import matplotlib.pyplot as plt

class Graphing:

    def __init__(self, data, i):
        self.data = data
        self.graph_num = i + 1

    def printGraph(self):
        size = len(self.data)
        recall = np.zeros(size)
        precision = np.zeros(size)
        for i in range(size):
            (recall[i], precision[i]) = self.data[i]

        plt.plot(recall, precision)
        if (self.graph_num == 11):
            plt.title('Average')
        else:
            plt.title('Ranking ' + str(self.graph_num))
            
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.show()