import os.path
from os import path
import middleware

def main():
    print("Recibiendo mensajes: ")
    for cola in range(middleware.colas.__len__()):
        mensajes = middleware.verMensajes(cola)
        for mensaje in mensajes:
            print("Tarea a procesar: "+ mensaje)
    
    file = open("colas.txt", "r")
    colas = file.readlines()
    i = 0
    for cola in colas:
        if (path.exists("tareasCola"+str(i)+".txt")):
            mensajes = middleware.verMensajes(i)
            i +=1
            print("Mensajes de la cola: " + cola)
            for mensaje in mensajes:
                print(mensaje)
        else:
            pass
        
    



if __name__=='__main__':
    main()