class Carrera():
    def __init__(self, nombre: str, anios: int):
        self.__nombre = nombre
        self.__cant_anios = anios

    @property
    def nombre(self):
        return self.__nombre
    @property
    def cant_anios(self):
        return self.__cant_anios
    def __str__(self):
        return f"{self.nombre} - {self.cant_anios} años"


