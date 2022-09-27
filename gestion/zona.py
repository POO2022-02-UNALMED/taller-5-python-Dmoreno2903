class Zona():
    _animales = []
    def __init__(self, nombre, *args):
        self._nombre = nombre
        for i in args:
            self._zoo = i
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def setNombre(self, nombre):
        self._nombre = nombre
    def setZoo(self, zoologico):
        self._zoo = zoologico

    
