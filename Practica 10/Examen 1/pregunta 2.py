class LineaTeleferico:
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=0):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = [["", "", ""] for _ in range(100)]  
        self.edades = [0] * 100
        self.sueldos = [0] * 100

    def leer(self):
        self.color = input("Ingrese el color: ")
        self.tramo = input("Ingrese el tramo: ")
        self.nroCabinas = int(input("Ingrese el numero de cabinas: "))
        self.nroEmpleados = int(input("Ingrese el numero de empleados: "))
        for i in range(self.nroEmpleados):
            print(f"Empleado {i + 1}:")
            self.empleados[i][0] = input(" Nombre: ")
            self.empleados[i][1] = input(" Apellido paterno: ")
            self.empleados[i][2] = input(" Apellido materno: ")
            self.edades[i] = int(input(" Edad: "))
            self.sueldos[i] = float(input(" Sueldo: "))

    # b) 
    def eliminarEmpleadoPorApellidoX(self, apellido):
        i = 0
        print(f"Eliminando los apellidos {apellido}")
        while i < self.nroEmpleados:
            if apellido in self.empleados[i][1] or apellido in self.empleados[i][2]:
                print(f"Eliminando empleado: {self.empleados[i]}")
                for j in range(i, self.nroEmpleados - 1):
                    self.empleados[j] = self.empleados[j + 1]
                    self.edades[j] = self.edades[j + 1]
                    self.sueldos[j] = self.sueldos[j + 1]

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
    def mostrarMayorEdad(self):
        if self.nroEmpleados == 0:
            print("No hay empleados")
            return
        mayorEdad = max(self.edades[:self.nroEmpleados])
        print(f"Empleados con mayor edad ({mayorEdad} años):")
        for i in range(self.nroEmpleados):
            if self.edades[i] == mayorEdad:
                nombreCompleto = " ".join(self.empleados[i])
                print(f"{nombreCompleto} - Edad: {self.edades[i]}")

    # d)
    def mostrarMayorSueldo(self):
        if self.nroEmpleados == 0:
            print("No hay empleados")
            return
        mayorSueldo = max(self.sueldos[:self.nroEmpleados])
        print(f"Empleados con mayor sueldo ({mayorSueldo} Bs):")
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == mayorSueldo:
                nombreCompleto = " ".join(self.empleados[i])
                print(f"{nombreCompleto} - Sueldo: {self.sueldos[i]}")

    def __str__(self):
        result = f"Linea de color: {self.color}\n"
        result += f"Tramo: {self.tramo}\n"
        result += f"Nro Cabinas: {self.nroCabinas}\n"
        result += f"Nro Empleados: {self.nroEmpleados}\n"
        result += "Lista de empleados:\n"
        for i in range(self.nroEmpleados):
            if self.empleados[i] != ["", "", ""]:
                nombreCompleto = " ".join(self.empleados[i])
                result += f" {nombreCompleto} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return result


# Main
# a) Instanciar 2 objetos LineaTeleferico
print("-------------------A-------------------")
# Primera forma:
lineaRoja = LineaTeleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20, 4)
lineaRoja.empleados[0] = ["Pedro", "Rojas", "Luna"]
lineaRoja.edades[0] = 35
lineaRoja.sueldos[0] = 2500
lineaRoja.empleados[1] = ["Lucy", "Sosa", "Rios"]
lineaRoja.edades[1] = 43
lineaRoja.sueldos[1] = 3250
lineaRoja.empleados[2] = ["Ana", "Perez", "Rojas"]
lineaRoja.edades[2] = 26
lineaRoja.sueldos[2] = 2700
lineaRoja.empleados[3] = ["Saul", "Arce", "Calle"]
lineaRoja.edades[3] = 29
lineaRoja.sueldos[3] = 2800

# Segunda forma:
lineaAzul = LineaTeleferico()
lineaAzul.leer()

# b) Eliminar empleados por apellido
print("-------------------B-------------------")
lineaRoja.eliminarEmpleadoPorApellidoX("Rojas")

# c) Transferir un empleado
print("-------------------C-------------------")
print("ANTES DE LA TRANSFERENCIA")
print("-----Linea Roja-----")
print(lineaRoja)
print("-----Linea Azul-----")
print(lineaAzul)

print("Transfiriendo empleado de la Línea Roja a la Línea Azul...\n")
lineaAzul = lineaRoja + lineaAzul

print("DESPUÉS DE LA TRANSFERENCIA")
print("-----Linea Roja-----")
print(lineaRoja)
print("-----Linea Azul-----")
print(lineaAzul)

# d) Mostrar mayor edad y mayor sueldo
print("-------------------D-------------------")
lineaRoja.mostrarMayorEdad()
lineaAzul.mostrarMayorSueldo()
