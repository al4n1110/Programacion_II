#Fila A
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
    def __init__(self,titulo, material, b=Anunco(0,0)):
        self.titulo = titulo
        self.material = material
        self.anuncio = b
        self.artistas = []
        
    def agregarArtista(self, artista):
        self.artistas.append(artista)
        
    def masAñosExperiencia(self, artistaX):
        for artista in self.artistas:
            if artista.getAñosExperiencia() > artistaX.getAñosExperiencia(): 
                return artista
            else:
                return artistaX
            
    def agregarAnuncio(self,anuncio):
            self.anuncio = anuncio
        
    def monto_total_de_pinturas(self, precio_2):
            total = 0
            precio_1 = self.anuncio.getPrecio()
            total= precio_1 + precio_2
            return total
    
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
pintura_1 = Pintura("La noche estrellada", "Óleo sobre lienzo", Anunco(1, 1000), "Postimpresionismo")
pintura_2 = Pintura("La persistencia de la memoria", "Óleo sobre lienzo", Anunco(0,0),  "Surrealismo")

pintura_1.agregarArtista(Artista("Vincent van Gogh", "12345678", 10))
pintura_2.agregarArtista(Artista("Salvador Dalí", "87654321", 15))
#b)
print("-------------------B------------------------")
print("Artista con más años de experiencia: ")
print(pintura_1.masAñosExperiencia(pintura_2.artistas[0]))
#c)
print("-------------------C------------------------")
print("Precio total de las pinturas: ")
pintura_2.agregarAnuncio(Anunco(2, 2000))
print(pintura_1.monto_total_de_pinturas(pintura_2.getAnuncio().getPrecio()))
