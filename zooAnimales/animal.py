class Animal():
    _zona = []
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getHabitat(self):
        return self._habitat
    def getGenero(self):
        return self._genero
    def getZona(self):
        return self._zona[0] if len(self._zona)>0 else None