import numpy as np

class Matrice:
    def __init__(self, data):
        self.__d = data

    def getd(self):
        return self.__d

    def __add__(self, other):
        return Matrice()


np.data = ([(1,0),(0,1)])
print(np.data)

list = [1, 2, 3]
print(list)
