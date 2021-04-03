import os.path
from os import path
import middleware

def main():
    print("Recibiendo mensajes: ")    
    file = open("colas.txt", "r")
    colas = file.readlines()
    i = 0
    for cola in colas:
        if (path.exists("tareasCola"+str(i)+".txt")):
            mensajes = middleware.verMensajes(i)
            print("Mensajes de la cola: " + cola)
            for mensaje in mensajes:
                print(mensaje)
        else:
            pass
        i +=1
        
    



if __name__=='__main__':
    main()