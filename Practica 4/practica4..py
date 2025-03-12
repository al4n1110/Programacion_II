import math

class Figura_Geometrica:
    def area(self, *args):
        if len(args) == 1:
            return math.pi * math.pow(args[0], 2)  #Area del Circulo
        elif len(args) == 2:
            return args[0] * args[1]  #Area del rectangulo y del triangulo rectangulo
        elif len(args) == 3:
            return ((args[0] + args[1]) * args[2]) / 2  #Area del trapecio
        elif len(args) == 2:
            return (args[0] * args[1]) / 2  #Area del pentagono
        else:
            raise ValueError("Número de argumentos inválido para calcular el área")

# Prueba de la clase
figura = Figura_Geometrica()
print("Área del círculo:", figura.area(12))
print("Área del rectángulo:", figura.area(4.4, 10.5))
print("Área del triángulo rectángulo:", figura.area(4.3, 6) / 2)
print("Área del trapecio:", figura.area(8, 4, 5))
print("Área del pentágono:", figura.area(12.4, 7))
