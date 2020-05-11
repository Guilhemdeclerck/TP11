class Circle:
    def __init__(self, r):
        self.__rayon=r

    def getr(self):
        return self.__rayon

    def __add__(self, r1):
        return self.__rayon + r1.__rayon

    def __it__(self, r1):
        return self.__rayon < r1.__rayon

    def __gt__(self, r1):
        return self.__rayon > r1.__rayon

if __name__ == '__main__':
    c1 = Circle(2)
    print(isinstance(c1, Circle))
    c2 = Circle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c1 > c2
    print(c3)
    print(c4)
    print(c5)
