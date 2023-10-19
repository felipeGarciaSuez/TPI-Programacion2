class Curso():
    def __init__(self, nombre:str, contrasenia:str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia

    @property
    def nombre(self):
        return self.__nombre
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion

    def generar_contrasenia(self):
        pass
    def __str__(self):
        return f"Este curso es de {self.nombre}"
