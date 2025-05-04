class Ministerio:
    def __init__(self, nombre="", direccion="", nroEmpleados=0):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = nroEmpleados
        self.empleados = [["", "", ""] for _ in range(100)]  
        self.edades = [0] * 100
        self.sueldos = [0] * 100

    def leer(self):
        self.nombre = input("Ingrese el nombre del ministerio: ")
        self.direccion = input("Ingrese la dirección: ")
        self.nroEmpleados = int(input("Ingrese el número de empleados: "))
        for i in range(self.nroEmpleados):
            print(f"Empleado {i + 1}:")
            self.empleados[i][0] = input(" Nombre: ")
            self.empleados[i][1] = input(" Apellido paterno: ")
            self.empleados[i][2] = input(" Apellido materno: ")
            self.edades[i] = int(input(" Edad: "))
            self.sueldos[i] = float(input(" Sueldo: "))

    # b) 
    def eliminarEmpleadoPorEdadX(self, edad):
        i = 0
        print(f"Eliminando a los que tienen {edad}")
        while i < self.nroEmpleados:
            if self.edades[i] == edad:
                print(f"Eliminando empleado: {self.empleados[i]}")
                for j in range(i, self.nroEmpleados - 1):
                    self.empleados[j] = self.empleados[j + 1]
                    self.edades[j] = self.edades[j + 1]
                    self.sueldos[j] = self.sueldos[j + 1]
                # Limpiamos el último espacio
                self.empleados[self.nroEmpleados - 1] = ["", "", ""]
                self.edades[self.nroEmpleados - 1] = 0
                self.sueldos[self.nroEmpleados - 1] = 0
                self.nroEmpleados -= 1
            else:
                i += 1

    # c) 
    def __add__(self, otro):
        if self.nroEmpleados == 0:
            print("No hay empleados para transferir.")
            return otro

        index_origen = self.nroEmpleados - 1

        otro.empleados[otro.nroEmpleados] = self.empleados[index_origen]
        otro.edades[otro.nroEmpleados] = self.edades[index_origen]
        otro.sueldos[otro.nroEmpleados] = self.sueldos[index_origen]
        otro.nroEmpleados += 1

        self.empleados[index_origen] = ["", "", ""]
        self.edades[index_origen] = 0
        self.sueldos[index_origen] = 0
        self.nroEmpleados -= 1

        print(f"Empleado transferido: {otro.empleados[otro.nroEmpleados - 1]}")
        return otro
    
    # d) 
    def mostrarMenorEdad(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        menorEdad = min(self.edades[:self.nroEmpleados])
        print(f"Empleados con la menor edad ({menorEdad} años):")
        for i in range(self.nroEmpleados):
            if self.edades[i] == menorEdad:
                nombreCompleto = " ".join(self.empleados[i])
                print(f"{nombreCompleto} - Edad: {self.edades[i]}")

    # d) 
    def mostrarMenorSueldo(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        menorSueldo = min(self.sueldos[:self.nroEmpleados])
        print(f"Empleados con el menor sueldo ({menorSueldo} Bs):")
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == menorSueldo:
                nombreCompleto = " ".join(self.empleados[i])
                print(f"{nombreCompleto} - Sueldo: {self.sueldos[i]}")

    def __str__(self):
        result = f"Ministerio: {self.nombre}\n"
        result += f"Dirección: {self.direccion}\n"
        result += f"Número de empleados: {self.nroEmpleados}\n"
        result += "Lista de empleados:\n"
        for i in range(self.nroEmpleados):
            nombreCompleto = " ".join(self.empleados[i])
            result += f" {nombreCompleto} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return result

# Main

# a) Instanciar 2 objetos Ministerio de diferente forma
print("-------------------A-------------------")
# primera forma
ministerioSalud = Ministerio( "Ministerio de Salud", "Estación Central, Estación Cementerio, Estación 16 de Julio", 4)
ministerioSalud.empleados[0] = ["Pedro", "Rojas", "Luna"]
ministerioSalud.edades[0] = 35
ministerioSalud.sueldos[0] = 2500
ministerioSalud.empleados[1] = ["Lucy", "Sosa", "Rios"]
ministerioSalud.edades[1] = 43
ministerioSalud.sueldos[1] = 3250
ministerioSalud.empleados[2] = ["Ana", "Perez", "Rojas"]
ministerioSalud.edades[2] = 26
ministerioSalud.sueldos[2] = 2700
ministerioSalud.empleados[3] = ["Kevin", "Arce", "Calle"]
ministerioSalud.edades[3] = 26
ministerioSalud.sueldos[3] = 2500

# segunda forma
ministerioEducacion = Ministerio()
ministerioEducacion.leer()

# b) Eliminar empleados con edad X
print("-------------------B-------------------")
ministerioSalud.eliminarEmpleadoPorEdadX(26)

# c) Transferir empleado X del ministerioEducacion al ministerioSalud
print("-------------------C-------------------")
print("ANTES DE TRANSFERIR")
print("---- Ministerio Salud ----")
print(ministerioSalud)
print("---- Ministerio Educación ----")
print(ministerioEducacion)

print("\nTransfiriendo empleado...\n")
ministerioEducacion = ministerioSalud + ministerioEducacion  

print("DESPUÉS DE TRANSFERIR")
print("---- Ministerio Salud ----")
print(ministerioSalud)
print("---- Ministerio Educación ----")
print(ministerioEducacion)

# d) Mostrar menor edad y menor sueldo
print("-------------------D -------------------")
ministerioSalud.mostrarMenorEdad()
ministerioSalud.mostrarMenorSueldo()
