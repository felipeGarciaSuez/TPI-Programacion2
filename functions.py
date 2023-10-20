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