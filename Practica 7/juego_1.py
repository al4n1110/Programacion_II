import random


class Juego:
    def __init__(self, numeroDeVidas = 3): 
        self._numeroDeVidas = numeroDeVidas
        self.__record = 0
    
    def reiniciaPartida(self):
        self._numeroDeVidas = 3
    
    def actualizarRecord(self):
        if self._numeroDeVidas > self.__record:
            self.__record = self._numeroDeVidas
            print("Nuevo record")
            return self.__record

    def quitaVida(self):
        self._numeroDeVidas -= 1
        return self._numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.__numeroAAdivinar = 0
        
    def juega(self):
        self.reiniciaPartida()
        self.__numeroAAdivinar = random.randint(1, 10)
        print("Adivina el numero entre 1 y 10")
        while self._numeroDeVidas > 0 :
            intento = int(input("Tu intento:"))
            if not self.validaNumero(intento):
                print("Numero fuera de rango (1-10)")
                continue
            
            if intento  == self.__numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else:
                print("incorrecto.")
                if self.quitaVida():
                    print(f"Te quedan {self._numeroDeVidas} vidas")
                else:
                    print("Perdiste todas las vidas")
                    print(f"El numero era {self.__numeroAAdivinar}")
                    break
    def validaNumero(self, n):
        return 0 <= n <= 10

#Juego 2
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, intento):
        if intento  % 2 == 0 and intento >= 0 and intento <= 10:
            return True
        else:
            print("Error ")
            return False
        
    def juega(self):
        self.reiniciaPartida()
        self.__numeroAAdivinar = random.randrange(0, 10, 2)
        print("Adivina el numero entre 0 y 10")
        while self._numeroDeVidas > 0 :
            intento = int(input("Tu intento:"))
            if not self.validaNumero(intento):
                print("Ingresa un numero par del 0 al 10")
                continue
            
            if intento  == self.__numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else:
                print("incorrecto.")
                if self.quitaVida():
                    print(f"Te quedan {self._numeroDeVidas} vidas")
                else:
                    print("Perdiste todas las vidas")
                    print(f"El numero era {self.__numeroAAdivinar}")
                    break
                
        

        
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 != 0 and  numero >= 0 and numero <= 10  :
            return True
        else:
            print("Error ")
            return False
    
    
    def juega(self):
        self.reiniciaPartida()
        self.__numeroAAdivinar = random.randrange(1,10, 2)
        print("Adivina el numero entre 0 y 10")
        while self._numeroDeVidas > 0 :
            intento = int(input("Tu intento:"))
            if not self.validaNumero(intento):
                print("Ingresa un numero impar del 0 al 10")
                continue
            
            if intento  == self.__numeroAAdivinar:
                print("Acertaste!!")
                self.actualizarRecord()
                break
            else:
                print("incorrecto.")
                if self.quitaVida():
                    print(f"Te quedan {self._numeroDeVidas} vidas")
                else:
                    print("Perdiste todas las vidas")
                    print(f"El numero era {self.__numeroAAdivinar}")
                    break
    

    
#Main
juego1 = JuegoAdivinaNumero(3)
juego2 = JuegoAdivinaPar(3)
juego3 = JuegoAdivinaImpar(3)

print("---------Juego 1---------")
juego1.juega()

print("---------Juego 2---------")
print("Adivina un numero par")
juego2.juega()

print("---------Juego 3---------")
print("Adivina un numero impar")
juego3.juega()