from abc import ABC


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    def contrasenia(self):
        return self.__contrasenia

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def email(self):
        return self.__email

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia = nueva_contrasenia

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    def validar_credenciales(self, email: str, password: str) -> bool:
        user = False
        res = False
        if self.email == email:
            user = True
            if self.contrasenia == password:
                res = True
        return res, user

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} Contraseña: {self.contrasenia}"