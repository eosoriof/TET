import middleware

registrado = False
acceso = False
userName = ''

        

def comprobarRegistro():
    global registrado
    registrado = True

def acceder():
    global acceso
    acceso = True

def registrar(email, password):
    file = open("users.txt", "a")
    file.write(email+","+password+"\n")
    file.close()
    print("Gracias por registrarse")
    comprobarRegistro()
    main()
    
def iniciarSesion(email, password):
    exito = False
    file = open("users.txt", "r")
    for user in file:
        e,p = user.split(',')
        p = p.strip()
        if (e == email and p == password):
            exito = True
            break
    file.close()
    if(exito):
        print("Iniciando sesion ...")
        acceder()
        enviarTareas()
    else:
        print("Email o contraseña incorrectos o el usuario no está registrado")
        main()


def mandarMensaje(colaSeleccionada):
    print("Para mandar tarea escriba 1, para volver al menu anterior 2, para salir 3")
    opcion = input()
    if (opcion == '1'):
        print("Escriba su tarea a ser procesada")
        tarea = input()
        middleware.recibirMensaje(colaSeleccionada, tarea)
        mandarMensaje(colaSeleccionada)
    elif (opcion == '2'):
        enviarTareas()
    elif (opcion == '3'):
        exit()
    else:
        mandarMensaje(colaSeleccionada)
    
    

def enviarTareas():
    print("Hola de nuevo")
    print("Seleccione una opción:")
    print("1. Crear cola")
    print("2. Enviar tarea a una cola")
    print("3. Eliminar cola")
    opcion = input()

    if (opcion == '1'):
        print("Ingrese el nombre de la cola: ")
        nombre = input()
        cola = middleware.crearCola(nombre, userName)
        enviarTareas()
    elif (opcion == '2'):
        if (middleware.colas.__len__() > 0):
            middleware.listarColas()
            print("Seleccione una cola: (ejm: 1)")
            colaSeleccionada = input()
            print("Cola seleccionada: " + colaSeleccionada)
            while(int(colaSeleccionada) > middleware.colas.__len__()):
                print("Esa cola no ha sido creada, por favor seleccione otra opcion")
                middleware.listarColas()
                print("Seleccione una cola: (ejm: 1)")
                colaSeleccionada = input()
                print("Cola seleccionada: " + colaSeleccionada)
            mandarMensaje(int(colaSeleccionada))
        else:
            print("Primero debe crear una cola")
            enviarTareas()
    elif (opcion=='3'):
        middleware.eliminarCola(userName)
    else:
        enviarTareas()
    



def main():
    global userName
    print("Seleccione una opción:")
    print("1. Registro")
    print("2. Iniciar sesión")
    print("3. Enviar tarea a cola") #Aqui deberia haber otras opciones
    opcion = input()
    print("Usted ha seleccionado la opción: " + opcion)
    if (opcion == '1'):
        print("-----------Bienvenido al registro--------------")
        email = input("Ingrese su email: ")
        password = input("Ingrese una contraseña: ")
        registrar(email, password)
    elif (opcion == '2'):
        print("-------------Iniciar sesión---------------")
        email = input("Ingrese su email: ")
        userName = email
        password = input("Ingrese su contraseña: ")
        iniciarSesion(email, password)
    elif (opcion == '3'):
        if (acceso):
            enviarTareas()
        else:
            print("Primero debe iniciar sesión")
            main()
    else:
        main()


if __name__ == "__main__":
    main()