class Complex:
    def __init__(self, pr, pi):
        self.__partiereelle = pr
        self.__partieimaginaire = pi

    def getpr(self):
        return self.__partiereelle

    def getpi(self):
        return self.__partieimaginaire

    def __add__(self, other):
        return Complex(self.__partiereelle + other.__partiereelle, self.__partieimaginaire + other.__partieimaginaire)

    def __sub__(self, other):
        return Complex(self.__partiereelle - other.__partiereelle, self.__partieimaginaire - other.__partieimaginaire)

    def __mul__(self, other):
        return Complex(self.__partiereelle - other.__partiereelle, self.__partieimaginaire - other.__partieimaginaire)

    def __truediv__(self, other):
        return  Complex((self.__partiereelle)/(other.__partiereelle), (self.__partieimaginaire)/(other.__partieimaginaire))

    def __abs__(self, other):
        return abs(self.__partiereelle) and abs(self.__partieimaginaire)

    def __eq__(self, other):
        return self.__partiereelle == other.__partiereelle and self.__partieimaginaire == other.__partieimaginaire

    def __ne__(self, other):
        return self.__partiereelle != other.__partiereelle and self.__partieimaginaire != other.__partieimaginaire

if __name__ == '__main__':
    objet1 = Complex(4, 8)
    objet2 = Complex(2, 4)
    objet3 = objet1 + objet2
    print(isinstance(objet2, Complex))
    print("objet3("+str(objet3.getpr())+","+str(objet3.getpi())+")")
    objet4 = objet1 - objet2
    print("objet4("+str(objet4.getpr())+","+str(objet4.getpi())+")")
    objet6 = objet1/objet2
    print("objet6("+str(objet6.getpr())+","+str(objet6.getpi())+")")
    #print("objet7(", abs(objet1),",", abs(objet2)
    objet5 = objet1 == objet2
    print(objet5)
    objet6 = objet1 != objet2
    print(objet6)
