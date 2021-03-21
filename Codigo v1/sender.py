try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

class MetaClass(type):
    _instance = {}
    
    def __call__(cls, *args, **kwargs):
        """Singleton Design Pattern"""
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class RabbitmqConfigure(metaclass=MetaClass):
    def __init__(self, queue='hello', host='localhost', routingKey='hello', exchange=''):
        self.host=host
        self.queue = queue
        self.routingKey = routingKey
        self.exchange = exchange


class RabbitMq():
    def __init__(self, server):
        self.server = server

        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)
    
    def publish(self, payload = {}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routingKey, body=str(payload))
        print('Published messsage: {}'.format(payload))
        self._connection.close()

if __name__ == "__main__":
    """ server = RabbitmqConfigure(queue='hello', host='localhost', routingKey='hello', exchange='')
    rabbitmq = RabbitMq(server)
    rabbitmq.publish(payload={"Data":"Hello World!"}) """

    #Ensayo usando IP de Middleware en EC2
    server = RabbitmqConfigure(queue='hello', host='54.211.164.46', routingKey='hello', exchange='')
    rabbitmq = RabbitMq(server)
    rabbitmq.publish(payload={"Data":"Hello World!"})




