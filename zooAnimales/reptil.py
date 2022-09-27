from zooAnimales.animal import Animal
import this

class Reptil(Animal):
    _listado = []
    _iguanas = 0
    _serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(this)

    def getNombre(self):
        return super().getNombre()
    def getEdad(self):
        return super().getEdad()
    def getHabitat(self):
        return super().getHabitat()
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    
    def cantidadReptiles(self):
        return len(self._listado)
    def crearIguana(self, nombre, edad, genero):
        Reptil(nombre, edad, "humedal", genero, "verde", 3)
        self._iguanas += 1
    def crearSerpiente(self, nombre, edad, genero):
        Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        self._serpientes += 1