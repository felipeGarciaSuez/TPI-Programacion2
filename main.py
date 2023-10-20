from functions import *

from Usuario import Usuario
from Estudiante import Estudiante
from Curso import Curso
from Profesor import Profesor
from Carrera import Carrera

alumnos = []
profesores = []
cursos = []

carrera1 = Carrera("Tecnicatura en Programacion", 2)

alumno1 = Estudiante("Agustin", "Cordoba", "aguscordoba@gmail.com", "1234", 1234, 2021, carrera1)
alumno2 = Estudiante("Felipe", "Garcia", "felipegarcia@gmail.com", "1234", 1235, 2021, carrera1)
profesor1 = Profesor("Mercedes", "Valoni", "mechi@gmail.com", "1234", "Ingeniera en Sistemas", 2020)

alumnos.append(alumno1)
alumnos.append(alumno2)
profesores.append(profesor1)

cursos = carga_cursos(carrera1)

def main():
    opt = 0

    while opt != 4:
        opt = menu()
        if opt == 1:
            res = validacion(alumnos)


        elif opt == 2:
            res = validacion(profesores)

        elif opt == 3:
            print("You chose option 3")
        elif opt == 4:
            print("Gracias por usar el sistema.")
        else:
            print("Invalid option")
            opt = 0

main()