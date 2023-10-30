class Carrera():
    def __init__(self, nombre: str, anios: int):
        self.__nombre = nombre
        self.__cant_anios = anios
        self.__materias = []
        self.__estudiantes = []

    @property
    def nombre(self):
        return self.__nombre
    @property
    def cant_anios(self):
        return self.__cant_anios
    @property
    def materias(self):
        return self.__materias
    @property
    def estudiantes(self):
        return self.__estudiantes


    def get_cant_materias(self):
        return len(self.__materias)

    def __str__(self):
        return f"{self.nombre} - {self.cant_anios} años"


