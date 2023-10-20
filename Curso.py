from Carrera import Carrera
import string, random

class Curso():
    def __init__(self, nombre:str,  carrera: Carrera):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__carrera = carrera

    @property
    def nombre(self):
        return self.__nombre
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    @property
    def carrera(self):
        return self.__carrera

    def __generar_contrasenia(self) -> str:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for i in range(5))

    def __str__(self):
        return f"Este curso es de {self.nombre}"
