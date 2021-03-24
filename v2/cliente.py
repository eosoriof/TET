import requests
class Cliente:
    #tareas = []
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def mandarTareas(self):
        for i in range(0, 10):
            tarea = "tarea_"
            tarea+= str(i)
            #tareas.append(tarea)
            mensaje = {
                "queue_name" : "myqueue",
                "message" : tarea 
            }
            print(mensaje)
            requests.post("Ip middleware", mensaje)
            #mandar request a middleware

if __name__=="__main__":

    clienteUno = Cliente("cliente1", "cliente1@example.com")
    clienteUno.mandarTareas()

