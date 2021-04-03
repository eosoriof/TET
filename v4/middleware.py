#Aqui se deben: Crear, borrar y listar colas
#Se debe recibir y enviar los mensajes

colas = []
class Cola:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
    
    def pushMensaje(self, mensaje):
        self.mensajes.append(mensaje)
    
    def getMensajes(self):
        return self.mensajes


def crearCola(nombre):
    cola = Cola(nombre)
    colas.append(cola)
    file = open("colas.txt", "a")
    file.write(cola.nombre+"\n")
    file.close()

def listarColas():
    file = open("colas.txt", "r")
    i = 0
    for c in file:
        print(str(i) +" "+ c)
        i+=1
    file.close()

def recibirMensaje(colaSeleccionada, mensaje):
    file = open("tareasCola"+str(colaSeleccionada)+".txt", "a")

    print("Mensaje: " + mensaje +" ha sido recibido")
    colas[colaSeleccionada].pushMensaje(mensaje)
    file.write(mensaje + "\n")
    file.close()

def verMensajes(colaSeleccionada):
    #respuesta = colas[colaSeleccionada].getMensajes()
    respuesta = []
    file = open("tareasCola"+str(colaSeleccionada)+".txt", "r")
    for tarea in file:
        respuesta.append(tarea)
    file.close()
    return respuesta

        
    


