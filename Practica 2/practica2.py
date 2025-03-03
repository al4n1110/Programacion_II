import math
import matplotlib.pyplot as plt
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
        return f"{self.x},{self.y}"
class Linea:
    def __init__(self, p1:Punto ,p2:Punto):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f"Punto1 = {self.p1} , Punto2 = {self.p2}"
    def dibujarLinea(self):
        plt.plot([self.p1.x,self.p2.x],[self.p1.y,self.p2.y] ,linestyle = "-")
        plt.title('LINEA')
        plt.xlabel('Lado x')
        plt.ylabel('Lado y')
        plt.show()
class Circulo:
    def __init__(self,centro:Punto,radio:float):
        self.centro = centro
        self.radio = radio
    def __str__(self):
        return f"Centro:{self.centro} , Radio:{self.radio}"
    def dibujarCirculo(self):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((self.centro.x,self.centro.y), self.radio,fill= False))
        ax.plot(self.centro.x , self.centro.y,"bo")
        plt.title('CIRCULO')
        plt.xlabel('Lado x')
        plt.ylabel('Lado y')
        plt.show()
p1 = Punto(0,0)
p2 = Punto(-5,-5)
linea1 = Linea(p1,p2)
print(linea1.__str__())
print(linea1.dibujarLinea())

c = Punto(2,3)
r = 5
circulo1 = Circulo(c,r)
print(circulo1.__str__())
print(circulo1.dibujarCirculo())