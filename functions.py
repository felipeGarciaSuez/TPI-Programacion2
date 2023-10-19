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

def validacion(lista):
    usuario = input("Ingrese su usuario: ")

    res = False
    for i in lista:
        if i.email == usuario:
            contrasenia = input("Ingrese su contraseña: ")
            if i.password == contrasenia:
                res = i
            else:
                print("Contraseña incorrecta.")
    if res:
        print("Bienvenido/a", res.name)
    else:
        print("Ese usuario no existe.")
    return res

