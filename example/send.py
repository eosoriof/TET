import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('54.211.164.46'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='prueba!')
print(" [x] Sent 'Hello World!'")

connection.close()