from Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, name: str, surname: str, email: str, password: str, titulo: str, anio:int):
        self.__titulo = titulo
        self.__anio_egreso = anio
        self.__mis_cursos = []
        super().__init__(name, surname, email, password)

    @property
    def titulo(self):
        return self.__titulo
    @property
    def anio_egreso(self):
        return self.__anio_egreso

    def dictar_curso(self, curso):
        pass
