from Curso import Curso

# MENU
def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")
    opt = int(input("Ingrese una opcion: "))
    return opt

def menu_alumno():
    print("1 - Matricularse a un curso")
    print("2 - Ver curso")
    print("3 - Volver al menú principal")

def menu_profesor():
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3 - Volver al menú principal")

# FIN MENU

# VALIDACION
def validacion(lista):
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    res = False

    for usuario in lista:
        res, user = usuario.validar_credenciales(email, password)
        print(res, user)
        if user:
            if res:
                print(f'Bienvenido/a {usuario.nombre}!')
                res = usuario
            else:
                print('Contraseña incorrecta.')
            break
    print(res)
    if not user:
        print("Ese usuario no existe.")
        print("Si considera esto un error, comuniquese con alumnado para la verificacion de su cuenta")

    return res


# CURSOS
def carga_cursos(carrera):
    cursos = []

    cursos.append(Curso("Ingles I", carrera))
    cursos.append(Curso("Ingles II", carrera))
    cursos.append(Curso("Laboratorio I", carrera))
    cursos.append(Curso("Laboratorio II", carrera))
    cursos.append(Curso("Programacion I", carrera))
    cursos.append(Curso("Programacion II", carrera))

    return cursos

def mostrar_cursos(cursos):
    for curso in cursos:
        print(f'Materia: {curso.nombre}           Carrera:{curso.carrera.nombre}')


def mostrar_curso_en_lista(cursos):
    for i, curso in enumerate(cursos):
        print(f'{i+1} - {curso.nombre}')

# FIN CURSOS

# ALUMNOS

def matriculacion(alumno, cursos):
    mostrar_curso_en_lista(cursos)
    curso_id = int(input("Ingrese el id del curso: "))
    while curso_id > len(cursos) or curso_id <= 0:
        curso_id = int(input("ERROR! Ingrese un id valido: "))
    constrasenia = input("Ingrese la contraseña de matriculacion: ")
    alumno.matricular_en_curso(cursos[curso_id - 1], constrasenia)

def mostrar_cursos_alumno(alumno):
    if alumno.mis_cursos:
        mostrar_curso_en_lista(alumno.mis_cursos)
        curso_id = int(input("Ingrese el id del curso que desea ver: "))
        while curso_id > len(alumno.mis_cursos) or curso_id < 1:
            curso_id = int(input("ERROR! Ingrese un numero valido: "))
        print(f'Nombre: {alumno.mis_cursos[curso_id - 1].nombre}')
    else:
        print("No estas matriculado en ningun curso")