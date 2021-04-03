registrado = False
acceso = False
colas = []
class Cola:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
    
    def pushMensaje(self, mensaje):
        self.mensajes.append(mensaje)
    
    def getMensajes(self):
        for mensaje in self.mensajes:
            print(mensaje)
        

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


def listarColas():
    i = 0
    for c in colas:
        print(str(i) +" "+ c.nombre)

def enviarTareas():
    print("Hola de nuevo")
    print("Seleccione una opción:")
    print("1. Crear cola")
    print("2. Enviar tarea a una cola")
    opcion = input()

    if (opcion == '1'):
        print("Ingrese el nombre de la cola: ")
        nombre = input()
        cola = Cola(nombre)
        colas.append(cola)
        enviarTareas()
    elif (opcion == '2'):
        if (colas.__len__() > 0):
            listarColas()
            print("Seleccione una cola: (ejm: 1)")
            colaSeleccionada = input()
            while(int(colaSeleccionada) > colas.__len__()):
                print("Esa cola no ha sido creada, por favor seleccione otra opcion")
                listarColas()
                print("Seleccione una cola: (ejm: 1)")
                colaSeleccionada = input()
            #Esto se debe hacer en el middleware

            
        else:
            print("Primero debe crear una cola")
            enviarTareas()
    else:
        enviarTareas()
    



def main():
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