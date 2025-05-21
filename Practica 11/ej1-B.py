#Fila B
#1)
class Anunco:
    def __init__(self,numero,precio):
        self.numero = numero
        self.precio = precio
        
    def getNumero(self):
        return self.numero
    def setNumero(self,numero):
        self.numero = numero
        
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio = precio
    
class Artista:
    def __init__(self,nombre,ci,añosExperiencia):
        self.nombre = nombre
        self.ci = ci
        self.añosExperiencia = añosExperiencia
    
    def __str__(self):
        return f"-----------Artista--------------\nNombre: {self.nombre}\nCI: {self.ci}\nAños de experiencia: {self.añosExperiencia}"
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getCi(self):
        return self.ci
    def setCi(self,ci):
        self.ci = ci
        
    def getAñosExperiencia(self):
        return self.añosExperiencia
    def setAñosExperiencia(self,añosExperiencia):
        self.añosExperiencia = añosExperiencia
        
class Obra:
    def __init__(self,titulo, material, b):
        self.titulo = titulo
        self.material = material
        self.anuncio = b
        self.artistas = []
        
    def agregarArtista(self, artista):
        self.artistas.append(artista)
    
    def promedioAñosExperiencia(self, artistaX):
        for artista in self.artistas:
                promedio = (artista.getAñosExperiencia() + artistaX.getAñosExperiencia()) / 2
                return promedio
    
    def incrementar_precio_artistaX(self, artistaX, nuevo_precio):
        for artista in self.artistas:
                if artista.getNombre() == artistaX.getNombre():
                    self.anuncio.setPrecio(nuevo_precio)
                    print(f"Se incrementño el precio de la obra {self.titulo} a {nuevo_precio} por el artista {artistaX.getNombre()}")
    
    def getTitulo(self):
        return self.titulo
    def setTitulo(self,titulo):
        self.titulo = titulo
    
    def getMaterial(self):
        return self.material
    def setMaterial(self,material):
        self.material = material
        
    def getAnuncio(self):
        return self.anuncio
    def setAnuncio(self,anuncio):
        self.anuncio = anuncio
        
    def getArtistas(self):
        return self.artistas
    def setArtistas(self,artistas):
        self.artistas = artistas
    
class Pintura(Obra):
    def __init__(self,titulo,material,b,genero):
        super().__init__(titulo, material, b)
        self.genero = genero
    
    def getGenero(self):
        return self.genero
    def setGenero(self,genero):
        self.genero = genero

#Main
#a)
pintura_1 = Pintura("La noche estrellada", "Óleo sobre lienzo", Anunco(1, 1000), "Impresionismo")
pintura_2 = Pintura("La persistencia de la memoria", "Óleo sobre lienzo", Anunco(2, 1500), "Surrealismo")

pintura_1.agregarArtista(Artista("Pablo Picasso", "12345678", 10))
pintura_2.agregarArtista(Artista("Vincent van Gogh", "87654321", 5))

#b)
print("----------------B----------------------")
print("El promedio de años de experiencia es: ")
print(pintura_1.promedioAñosExperiencia(pintura_2.artistas[0]))
#c)
print("----------------C----------------------")
pintura_1.incrementar_precio_artistaX(pintura_1.artistas[0], 1500)

