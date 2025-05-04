# Primera pregunta-Fila_B
## Abstracción
En la primera parte de abstracción coloque las clases de Planta, Clima y Suelo.
## Clase Planta
En esta clase puse los atributos de:
### Atributos
- nombre (string): Es el nombre de la especie.
- familia (string): La familia botánica a la que pertenece.
- altura (float): La altura promedio de la platna en metros.
- region (string):Es la región geográfica donde la planta es nativa.
### Métodos
- esAdecuadaParaClima(temperatura:float): Devuelve un valor booleano para ver si la planta es adecuada para el clima y se le manda como argumentos una temperatura de tipo float.
- cambiarRegion(nuevaRegion:String):Devuelve un String mostrando a qué región se cambió la planta, y para todo aquello se le envia como argumento una nuevaRegion de tipo String.
## Clase Clima
En esta clase se me ocurrió:
### Atributos
- temperatura(float): Se almacena la temperatura que hace en dicho clima.
- humedad(float): Se coloca un número de tipo float para que indique cuál es la humedad que hay en determinado clima.
- estacion(String): Se coloca la estacion del año en el que se encuentra.
- region(String): Se coloca la región en el que está el clima.
### Métodos
- esEstacionFavorable(estacion:String): Devuelve un booleano para ver si la estacion es favorable o no, también se manda como argumento una estación de tipo String.
- esFrio(): Devuelve un booleano también para ver si el clima es frio o no.
## Clase Suelo
Aquí coloqué:
### Atributos
- tipo(String): Este atributo dice el tipo de suelo.
- region(String): Se almacena la región en la que se encuentra el suelo.
- humedad(float): Se coloca el porcentaje de humedad que tiene el suelo.
- nutrientes(float): Se inserta el porcentaje de nutrientes que aporta el suelo.
### Métodos
+ esFertil(): Devuelve un booleano para ver si la tierra es fertil o no.
+ necesitaMejoras(): Devuelve un booleano indicando si el suelo necesita mejoras o no para ello usa los atributos instanciados.