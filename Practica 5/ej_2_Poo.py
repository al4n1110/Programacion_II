import math
#Clase
class Estadistica:
    def __init__(self, numeros ):
        self.numeros = numeros
    
    def promedio(self):
        suma = 0;
        for i in range(len(self.numeros)):
            suma += self.numeros[i]
        return suma / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        s = sum((x - prom)**2 for x in self.numeros)
        divisor = len(self.numeros) -1
        return math.sqrt(s / divisor)
#main
numeros = []
for i in range(10):
    num = float(input(f"Ingrese un numero ({i+1}/10):"))
    numeros.append(num)

#Instanciando el objeto Estadistica
estadistica1 = Estadistica(numeros)
print(f"El promedio es: {estadistica1.promedio():.2f}")
print(f"La desviacion estandard es:{estadistica1.desviacion():.4f}")