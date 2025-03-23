import math
#Metodos
def promedio( numeros):
    suma = 0
    for i in numeros:
        suma += i
    if suma == 0:
        return None
    else:
        return suma /len(numeros)

def desviacion(numeros):
    prom = promedio(numeros)
    s = 0
    s = sum((x - prom)**2 for x in numeros)
    divisor = len(numeros) -1
    return math.sqrt( s / divisor)
    
#Main
numeros = []
for i in range(10):
    num = float(input(f"Ingrese un numero ({i+1}/10):"))
    numeros.append(num)
print(f"El promedio es:","{:.2f}".format(promedio(numeros)))
print(f"La desviacion estandard es:","{:.4f}".format(desviacion(numeros)))