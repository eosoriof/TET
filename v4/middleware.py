colas = []
class Cola:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
    
    def pushMensaje(self, mensaje):
        self.mensajes.append(mensaje)
    
    def getMensajes(self):
        return self.mensajes


def crearCola(nombre, userName):
    cola = Cola(nombre)
    colas.append(cola)
    file = open("colas"+userName+".txt", "a")
    file.write(cola.nombre+"\n")
    file.close()
    file2 = open("colas.txt","a")
    file2.write(cola.nombre+","+userName+"\n")
    file2.close()

def listarColas():
    file = open("colas.txt", "r")
    i = 0
    for c in file:
        print(str(i) +" "+ c)
        i+=1
    file.close()

def listarColasUsuario(userName):
    file = open("colas"+userName+".txt", "r")
    i = 0
    for c in file:
        print(str(i) +" "+ c)
        i+=1
    file.close()


def eliminarCola(userName):
    print("Ingrese la cola que desea eleminar: ")
    listarColasUsuario(userName)
    colaEliminar = input()
    file = open("colas"+userName+".txt", "r+")
    lines = file.readlines()
    file.truncate(0)
    file.close()
    eliminada = lines.pop(int(colaEliminar)).replace('\n', '')
    print(eliminada)
    newLines = lines
    file = open("colas"+userName+".txt", "a")
    for newLine in newLines:
        file.write(newLine)
    file.close()
    #Eliminar de la lista general de colas
    file = open("colas.txt", "r+")
    lines = file.readlines()
    tempList = []
    file.truncate(0)
    file.close()
    colaEliminada = eliminada+","+userName
    print(colaEliminada)
    for line in lines:
        if (colaEliminada in line):
            line = line.replace(colaEliminada, '')
            line = line.replace('\n', '')
        tempList.append(line)
    file = open("colas.txt", "a")
    for line in tempList:
        file.write(line)
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

        
    


