from abc import ABC, abstractmethod
import random
import math

#interfaz
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self):
        pass

#Clase abstracta
class Figura(ABC):
    def __init__(self,color):
        self.__color = color
    
    def setColor(self,color):
        self.__color = color
    
    def getcolor(self):
        return self.__color
    
    def __str__(self):
        return f"Color: {self.__color}"
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

#clase cuadrado
class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.__lado = lado
    
    def area(self):
        return self.__lado ** 2
    
    def perimetro(self):
        return 4 * self.__lado
    
    def comoColorear(self):
        return f"Colorear los cuatro lados"
    
    def __str__(self):
        return f"Cuadrado: {super().__str__()} , lado: {self.__lado} "

#clase circulo
class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.__radio = radio
        
    def area(self):
        return math.pi * (self.__radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.__radio
    
    def __str__(self):
        return f"Circulo: {super().__str__()} , radio: {self.__radio} "

#main
class main():
    figuras = []
    colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
    
    for i in range(5):
        tipo = random.randint(1,2) #1:cuadrado , 2:circulo
        color = random.choice(colores)
        valores = random.uniform(1.0, 10.0)
        if tipo == 1:
            figura = Cuadrado(valores, color)
        else:
            figura = Circulo(valores, color) 
        figuras.append(figura)
        
    #mostrando resultados
    print("----------FIGURAS----------")
    for figura in figuras:
        print(figura)
        print(f" Area: {figura.area()}")
        print(f" Perimetro: {figura.perimetro()}")
        if isinstance(figura, Cuadrado):
            print(f"Cómo colorear: {figura.comoColorear()}")
        print("-" * 30)