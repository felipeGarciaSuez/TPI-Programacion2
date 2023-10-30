from datetime import datetime

class Archivo():
    def __init__(self, nombre: str, formato: str):
        self.__nombre = nombre
        self.__fecha = datetime.now()
        self.__formato = formato


    @property
    def nombre(self):
        return self.__nombre
    @property
    def formato(self):
        return self.__formato
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre} Fecha: {str(self.__fecha)} Formato: {self.formato}"
