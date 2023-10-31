from functions import *


from Estudiante import Estudiante
from Archivo import Archivo
from Profesor import Profesor
from Carrera import Carrera

alumnos = []
profesores = []
cursos = []

carrera1 = Carrera("Tecnicatura en Programacion", 2)

alumno1 = Estudiante("Agustin", "Cordoba", "aguscordoba@gmail.com", "1234", 1234, 2021, carrera1)
alumno2 = Estudiante("Felipe", "Garcia", "felipegarcia@gmail.com", "1234", 1235, 2021, carrera1)
profesor1 = Profesor("Mercedes", "Valoni", "mechivaloni@gmail.com", "1234", "Ingeniera en Sistemas", 2020)
profesor2 = Profesor("Profesor", "Girafales", "profejira@gmail.com", "1234", "Ingeniera en Sistemas", 2020)

alumnos.append(alumno1)
alumnos.append(alumno2)
profesores.append(profesor1)
profesores.append(profesor2)

cursos.append(carga_cursos(carrera1, "Ingles I"))
cursos.append(carga_cursos(carrera1,"Ingles II"))
cursos.append(carga_cursos(carrera1,"Laboratorio I"))
cursos.append(carga_cursos(carrera1,"Laboratorio II"))
cursos.append(carga_cursos(carrera1,"Programacion I"))
cursos.append(carga_cursos(carrera1,"Programacion II"))


for curso in cursos:
    curso.agregar_archivo(Archivo("Main file", "PDF"))
    profesor1.dictar_curso(curso)

for curso in cursos:
    print(curso.nombre)
    print(curso.contrasenia_matriculacion)

def main():
    opt = 0

    while opt != 4:
        opt = menu()
        if opt == 1:
            alumno = validacion(alumnos)
            if alumno:
                opt2 = 0
                while opt2 != 4:
                    menu_alumno()
                    opt2 = int(input("Ingrese una opcion: "))
                    if opt2 == 1:
                        matriculacion(alumno, cursos)
                    elif opt2 == 2:
                        desmatriculacion(alumno, cursos)
                    elif opt2 == 3:
                        mostrar_cursos_alumno(alumno)
                    elif opt2 == 4:
                        print("Volviendo al menu principal...")
                    else:
                        print("Opcion incorrecta")
                        opt2 = 0

        elif opt == 2:
            profesor = validacion(profesores)
            if profesor:
                opt2 = 0
                while opt2 != 3:
                    menu_profesor()
                    opt2 = int(input("Ingrese una opcion: "))
                    if opt2 == 1:
                        curso = dictar_curso_menu(profesor, carrera1)
                        if not curso:
                            print("No se pudo dictar el curso")
                        else:
                            cursos.append(curso)
                    elif opt2 == 2:
                        mostrar_cursos_profesor(profesor)
                    elif opt2 == 3:
                        print("Volviendo al menu principal...")
                    else:
                        print("Opcion incorrecta")
                        opt2 = 0

        elif opt == 3:
            mostrar_cursos(cursos)
        elif opt == 4:
            print("Gracias por usar el sistema.")
        else:
            print("Invalid option")
            opt = 0

main()