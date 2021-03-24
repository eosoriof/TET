import requests
import json
class Cliente:
    #tareas = []
    def __init__(self, username, email, token=''):
        self.username = username
        self.email = email
        response = requests.post("http://127.0.0.1:5000/register", json.dumps({"username":username, "password": "pass"}))
        response = requests.post("http://127.0.0.1:5000/login", json.dumps({"username":username, "password": "pass"}))
        self.token = response.text
        
    def crearCola(self):
    	response = requests.post("http://127.0.0.1:5000/create_queue",json.dumps({"queue_name":"colaEjemplo", "token":self.token}))
    
    def mandarTareas(self):
        for i in range(0, 10):
            tarea = "tarea_"
            tarea+= str(i)
            #tareas.append(tarea)
            mensaje = {
                "queue_name" : "colaEjemplo",
                "message" : tarea 
            }
            print(mensaje)
            response = requests.post("http://127.0.0.1:5000/send_message", json.dumps(mensaje))
            print(response.text)
            #mandar request a middleware
            

if __name__=="__main__":

    clienteUno = Cliente("cliente1", "cliente1@example.com")
    clienteUno.crearCola()
    clienteUno.mandarTareas()

