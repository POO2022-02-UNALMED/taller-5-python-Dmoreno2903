from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    _salmones = 0
    _bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)

    def getNombre(self):
        return super().getNombre()
    def getEdad(self):
        return super().getEdad()
    def getHabitat(self):
        return super().getHabitat()
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls._salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls._bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
