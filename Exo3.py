class Rational :
    def __init__(self, n, d):
        self.__numerateur = n
        self.__denominateur =d

    def getn(self):
        return self.__numerateur

    def getd(self):
        return self.__denominateur

    def __eq__(self, other):
        return self.__numerateur == other.__numerateur and self.__denominateur == other.__denominateur

    def __ne__(self, other):
        return  self.__numerateur != other.__numerateur and self.__denominateur != other.__denominateur

    def __add__(self, other):
        if isinstance(other, Rational) == True :
         return Rational((self.__numerateur*other.__denominateur) + (other.__numerateur*self.__denominateur), (self.__denominateur*other.__denominateur))

    def __sub__(self, other):
        return Rational((self.__numerateur*other.__denominateur) - (other.__numerateur*self.__denominateur), (self.__denominateur*other.__denominateur))

    def __mul__(self, other):
        return Rational(self.__numerateur * other.__numerateur, self.__denominateur * other.__denominateur)

    def __truediv__(self, other):
        return Rational(self.__numerateur*other.__denominateur, self.__denominateur*other.__numerateur)


if __name__ == '__main__':
    r1 = Rational(1,2)
    r2 = Rational(2,3)
    print(isinstance(r2,Rational))
    r5 = r1 == r2
    print(r5)
    r3 = r1 + r2
    print("objet3("+str(r3.getn())+"/"+str(r3.getd())+")")
    r4 = r3 - r2
    print("objet4("+str(r4.getn())+"/"+str(r4.getd())+")")
    r6 = r3 == r4
    print(r6)
    r7 = r2*r4
    print("objet7("+str(r7.getn())+"/"+str(r7.getd())+")")
    r8 = r1/r2
    print("objet8("+str(r8.getn())+"/"+str(r8.getd())+")")

