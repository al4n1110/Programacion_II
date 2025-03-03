class Cola:
    def __init__(self,n):
        self.__n = n
        self.__arreglo = [0]*n
        self.__inicio = -1
        self.__fin = -1
    def insert(self, e):
        if not self.isFull():
            self.__fin +=1
            self.__arreglo[self.__fin] = e
        else:
            print("Cola llena")
    def remove(self):
        if self.isEmpty():
            print("Cola vacia")
            return -1
        else:
            self.__inicio += 1;
            elemento = self.__arreglo[self.__inicio]
            if self.isFull():
                self.__inicio = -1
                self.__fin = -1
            return elemento
    def peek(self):
        return self.__arreglo[self.__inicio+1]
    def isEmpty(self):
        return self.__inicio == self.__fin
    def isFull(self):
        return self.__fin == self.__n-1
    def size(self):
        return self.__fin+1
#Main
cola1 = Cola(5)
cola1.insert(64)
cola1.insert(20)
cola1.insert(44)
cola1.insert(10)
print(cola1.peek())
print(cola1.isEmpty())
print(cola1.isFull())
print(cola1.size())
print(cola1.remove())