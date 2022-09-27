from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    _halcones = 0
    _aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)

    def getNombre(self):
        return super().getNombre()
    def getEdad(self):
        return super().getEdad()
    def getHabitat(self):
        return super().getHabitat()
    def getColorPlumas(self):
        return self._colorPlumas

    def cantidadAves(self):
        return len(self._listado)
    def crearHalcon(self, nombre, edad, genero):
        self._halcones += 1
        return Ave(nombre, edad, "montanas", genero, "café glorioso")
    def crearAguila(self, nombre, edad, genero):
        self._aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
