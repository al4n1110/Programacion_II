import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def coord_cartesianas(self):
        return f"Coordenadas: {self.x} , {self.y}"
    def coord_polares(self):
        radio = "{:.2f}".format(math.sqrt(self.x**2+self.y**2))
        angulo = math.degrees(math.atan2(self.y,self.x))
        return f"Radio = {radio} , Angulo = {angulo}"
    def __str__(self):
        return f"Punto = {self.x},{self.y}"
    def toString(self):
        return self.__str__()

p1= Punto(5,5)

print(p1.coord_cartesianas())
print(p1.coord_polares())
print(p1.toString())


