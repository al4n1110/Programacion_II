##Herencia Multiple

La herencia múltiple es un concepto de la Programación Orientada a Objetos (POO) que permite que una clase hija herede atributos y métodos de dos o más clases padres al mismo tiempo.

Su principal ventaja es la reutilización de código, pero puede generar problemas de ambigüedad si las clases padres comparten atributos o métodos con el mismo nombre.

##Problema del Diamante
###Ejercicio propuesto en clase:
Este ejercicio trata de que dos clases manejan un mismo atributo y un mismo metodo que heredan a una clase hija.

Para resolver esto:

En Python los atributos heredados de dos o mas clases padres a una clase hija se sobreescribe la segunda clase.Los métodos tampoco se duplican

En Java la clase hija que hereda un atributo en comun de dos clases padre solamente hereda un atributo de las clases que se hereda dicho atributo. Al igual que en Python, los métodos tampoco se duplican



El problema del diamante ocurre cuando una clase hija hereda de dos clases padres que, a su vez, heredan de una misma clase base. Esto genera confusión porque no se sabe qué versión de los métodos o atributos debe utilizarse.

Este problema en concreto tiene diferentes formas de solucionarse segun el lenguaje de Programación a usar.

##¿Cómo se resuelve?
Principalmente en python y en java se resuelve de la siguiente manera:

Python:	Permite herencia múltiple directa. Resuelve el conflicto usando el MRO (Method Resolution Order), que define el orden de búsqueda de métodos y atributos.

Java: No permite herencia múltiple de clases. Lo resuelve utilizando composición (crear objetos de otras clases dentro de la clase hija) o  interfaces(que solo definen metodos sin atributos).