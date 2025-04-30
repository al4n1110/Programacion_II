import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
from PIL import Image, ImageTk

class Boleto(ABC):
    def __init__(self,numero):
        self._numero = numero
        self._precio = 0.0
        
    @abstractmethod
    def obtener_info(self):
        pass
    
class Palco(Boleto):
    def __init__(self,numero):
        super().__init__(numero)
        self._precio = 100.0
        
    def obtener_info(self):
        return f"Numero: {self._numero}, Precio: {self._precio}"
    
class Platea(Boleto):
    def __init__(self,numero, cantDiasevento):
        super().__init__(numero)
        if cantDiasevento >= 10:
            self._precio = 50.0
        else:
            self._precio = 60.0
    def obtener_info(self):
        return f"Numero: {self._numero}, Precio: {self._precio}"

class Galeria(Boleto):
    def __init__(self,numero, cantDiasevento):
        super().__init__(numero)
        if cantDiasevento >= 10:
            self._precio = 25.0
        else:
            self._precio = 30.0
            
    def obtener_info(self):
        return f"Numero: {self._numero}, Precio: {self._precio}"
    
def vender_boleto():
    numero_boleto = input_nombre.get()  # Obteniendo el número del boleto
    cant_dias = input_cantDias.get()  # Obteniendo la cantidad de días de anticipación
    
    # Validando que el número y los días de anticipación sean válidos
    try:
        numero_boleto = int(numero_boleto)  # Convertir el número a entero
        cant_dias = int(cant_dias)  # Convertir los días a entero
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")
        return
    
    # Creando el boleto según el tipo seleccionado
    if checkbox_1_var.get() == 1 and checkbox_2_var.get() == 0 and checkbox_3_var.get() == 0:  # Palco seleccionado
        nuevo_boleto = Palco(numero_boleto)
    elif checkbox_2_var.get() == 1 and checkbox_1_var.get() == 0 and checkbox_3_var.get() == 0:  # Platea seleccionada
        nuevo_boleto = Platea(numero_boleto, cant_dias)
    elif checkbox_3_var.get() == 1 and checkbox_2_var.get() == 0 and checkbox_1_var.get() == 0:  # Galeria seleccionada
        nuevo_boleto = Galeria(numero_boleto, cant_dias)
    else:
        messagebox.showerror("Error", "Por favor seleccione un tipo de boleto.")
        return
    
    # Limpiando el text_box antes de agregar nueva información
    text_box.delete(1.0, tk.END)  # Limpiando el contenido anterior
    # Insertar la nueva información del boleto
    text_box.insert(tk.END, nuevo_boleto.obtener_info())
    
#GUI
    
#Ventana principal
ventana = tk.Tk()
ventana.title("Teatro Municipal")
ventana.geometry("800x490+250+100")

ventana.config(bg="#f0f0f0")
ventana.option_add("*Font","Arial 12")
ventana.resizable(1, 1)

#Header frame_1
frame_1 = tk.Frame(ventana, bg="white")
frame_1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

#Header titulo
label_1 = tk.Label(frame_1, text="Teatro Municipal", font=("Arial", 30), bg="white")
label_1.pack(side="left" ,padx=100)

img = Image.open("img.png")
img_redimensionada = img.resize((200,100)) 
img_1 = ImageTk.PhotoImage(img_redimensionada)
label_img = tk.Label(frame_1,image= img_1 )
label_img.image = img_1
label_img.pack(side="right", padx=10, pady=2)

#fielset_1 datos del boleto
fieldset_1 = tk.LabelFrame(ventana, text="Datos del Boleto", bg="white")
fieldset_1.pack(side=tk.TOP, fill="x", padx=10, pady=10)

#checkboxs
checkbox_1_var = tk.IntVar()
checkbox_2_var = tk.IntVar()
checkbox_3_var = tk.IntVar()

checkbox_1 = tk.Checkbutton(fieldset_1, text="Palco", bg="white",variable=checkbox_1_var)
checkbox_1.grid(row=0, column=0, padx=10, pady=10)

checkbox_2 = tk.Checkbutton(fieldset_1, text="Platea", bg="white", variable=checkbox_2_var)
checkbox_2.grid(row=0, column=1, padx=10, pady=10)

checkbox_3 = tk.Checkbutton(fieldset_1, text="Galeria", bg="white", variable=checkbox_3_var)
checkbox_3.grid(row=0, column=2, padx=10, pady=10)

#fieldset_1 DATOS DEL BOLETO
label_nombre = tk.Label(fieldset_1, text="Numero:", bg="white")
label_nombre.grid(row=1, column=0, padx=10, pady=10)

input_nombre = tk.Entry(fieldset_1, width=30)
input_nombre.grid(row=1, column=1, padx=10, pady=10)

label_cantDias= tk.Label(fieldset_1, text="CantDias paara el evento:", bg="white")
label_cantDias.grid(row=2, column=0, padx=10, pady=10)

input_cantDias= tk.Entry(fieldset_1, width=30)
input_cantDias.grid(row=2, column=1, padx=10, pady=10)

#botones
boton_vender = tk.Button(fieldset_1, text="Vender Boleto", bg="white", command=vender_boleto, width=10)
boton_vender.grid(row=3, column=0, padx=10, pady=10)

boton_salir = tk.Button(fieldset_1, text="Salir", bg="white",width=10, command=ventana.quit) 
boton_salir.grid(row=3, column=1, padx=10, pady=10)

#Fielset_2 info
fieldset_2 = tk.LabelFrame(ventana, text="Informacion", bg="white")
fieldset_2.pack(side=tk.TOP, fill="x", padx=10, pady=10)

text_box = tk.Text(fieldset_2, width=50, height=2, bg="white",font=("Arial", 20))
text_box.grid(row=0, column=0, padx=10, pady=10)


ventana.mainloop()
