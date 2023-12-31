from Carrera import Carrera
from Archivo import Archivo
import string, random

class Curso():
    __prox_cod = int(0)
    def __init__(self, nombre:str,  carrera: Carrera):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__carrera = carrera
        self.__codigo = self.prox_cod
        self.__archivos = []


    @property
    def prox_cod(self):
        Curso.__prox_cod = self.__prox_cod + 1
        return Curso.__prox_cod
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    @property
    def carrera(self):
        return self.__carrera
    @property
    def archivos(self):
        return self.__archivos



    def __generar_contrasenia(self) -> str:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for i in range(5))

    def __str__(self):
        return f"Este curso es de {self.nombre}"

    def agregar_archivo(self, archivo: Archivo):
        self.__archivos.append(archivo)
