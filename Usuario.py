from abc import ABC


class Usuario(ABC):
    def __init__(self, name: str, surname: str, email: str, password: str) -> None:
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def email(self):
        return self.__email

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    def validar_credenciales(self, email: str, password: str) -> bool:
        return self.__email == email and self.__password == password

    def __str__(self) -> str:
        pass