from Usuario import Usuario
from Carrera import Carrera
from Curso import Curso
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
    @property
    def carrera(self):
        return self.__carrera
    @property
    def mis_cursos(self):
        return self.__mis_cursos



    def matricular_en_curso(self, curso: Curso, contrasenia):
        if curso in self.__mis_cursos:
            print("Ya estas matriculado en este curso")
        else:
            if curso.contrasenia_matriculacion == contrasenia:
                self.__mis_cursos.append(curso)
                print(f"Te has matriculado a {curso.nombre}")
            else:
                print("Contraseña incorrecta")
    def desmatricular_en_curso(self, curso: Curso):
        if curso in self.__mis_cursos:
            self.__mis_cursos.remove(curso)
        else:
            print("No estas matriculado en este curso")