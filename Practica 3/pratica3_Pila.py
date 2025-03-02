class Pila:
    def __init__( self,n):
        self.__arreglo = [0]*n
        self.__top = -1
        self.__n = n
    def push(self,e):
        if not self.isFull():
            self.__top += 1
            self.__arreglo[self.__top] = e
        else:
            print("Pila llena")
    def pop(self):
        if not self.isEmpty():
            elemento = self.__arreglo[self.__top]
            self.__top -=1
            return elemento
    def peek(self):
        return self.__arreglo[self.__top]
    def isEmpty(self):
        return self.__top == -1
    def isFull(self):
        return self.__top == self.__n-1
#Main
pila1 = Pila(5)
pila1.push(3)
pila1.push(1)
pila1.push(5)
pila1.push(10)
print(pila1.peek())
print(pila1.isEmpty())
print(pila1.isFull())
print(pila1.pop())
