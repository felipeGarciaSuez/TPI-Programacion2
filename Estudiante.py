from Usuario import Usuario
from Carrera import Carrera
class Estudiante(Usuario):
    def __init__(self, name: str, surname: str, email: str, password: str, legajo: int, anio:int, carrera: Carrera):
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio
        self.__carrera = carrera
        self.__mis_cursos = []
        super().__init__(name, surname, email, password)

    @property
    def legajo(self):
        return self.__legajo
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera


    def matricular_en_curso(self, curso):
        pass
    def desmatricular_en_curso(self, curso):
        pass