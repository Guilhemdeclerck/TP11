class Duree:
    def __init__(self, heure, minute, seconde):
        self.__h = heure
        self.__m = minute
        self.__s = seconde

    def geth(self):
        return self.__h

    def getm(self):
        return self.__m

    def gets(self):
        return self.__s

    def sets(self):
        if self.__s >= 60 :
            self.__m = self.__m+1
            self.__s = self.__s -60
        return self.__m, self.__s

    def setm(self):
        if self.__m >= 60:
            self.__h = self.__h+1
            self.__m = self.__m-60
        return self.__h, self.__m


    def aff(self):
        print(self.__h,"h",self.__m,"m",self.__s,"s")

    def __add__(self, other):
        return Duree(self.__h + other.__h, self.__m + other.__m, self.__s + other.__s)

if __name__ == '__main__':
    d1 = Duree(3,2,1)
    d2 = Duree(0,3,61)
    d3 = d1 + d2
    d3.sets()
    print(str(d3.geth())+"h"+str(d3.getm())+"m"+str(d3.gets())+"s")
