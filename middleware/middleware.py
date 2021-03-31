import pika
from database import *
from auth import *
from flask import Flask, request
import logging


RABBIT_HOST = '54.211.164.46'
app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
#CORS(app)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST,
                                                               heartbeat=600,
                                                               blocked_connection_timeout=300))
channel = connection.channel()


@app.route('/create_queue', methods=['POST'])
def create_queue():
    body = request.get_json(force=True)
    queue_name = body.get('queue_name', '')
    token = body.get('token', '')
    if not queue_name or not token:
        return '{}', 400
    try:
        owner_name = get_username_from_token(token)
    except Exception as e:
        return 'Can\'t create queue: invalid token', 403
    if register_queue(queue_name, owner_name):
        return 'Queue created: ' + queue_name, 200
        channel.queue_declare(queue=queue_name)
    return 'Queue already exists', 403


@app.route('/list_queues', methods=['GET'])
def list_queues():
    return json.dumps(get_queues(), sort_keys=True, indent=4, separators=(',', ': ')), 200


@app.route('/delete_queue', methods=['DELETE'])
def delete_queue():
    body = request.get_json(force=True)
    queue_name = body.get('queue_name', '')
    token = body.get('token', '')
    if not queue_name or not token:
        return 'Empty queue_name or empty/invalid token', 400
    try:
        username = get_username_from_token(token)
    except Exception as e:
        return 'Empty/invalid token', 401
    res = erase_queue(queue_name, username)
    if not res:
        return 'Cant delete: queue doesn\'t exists or user is not the owner of the queue', 401
    channel.queue_delete(queue=queue_name)
    return 'Queue deleted: ' + queue_name, 200


@app.route('/send_message', methods=['POST'])
def send_message():
    body = request.get_json(force=True)
    queue_name = body.get('queue_name', '')
    message = body.get('message', '')
    if not queue_name:
        return '{}', 400
    try:
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
    except Exception as e:
        'Queue doesnt exists', 404
    return f'Message sent to {queue_name}: {message}', 200


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json(force=True)
    username = body.get('username', '')
    password = body.get('password', '')

    if not password or not username:
        return 'Invalid credentials', 400
    user = login_user(username, password)
    if not user:
        return 'User not found', 403
    else:
        token = generate_token(user)
        return token, 200


@app.route('/register', methods=['POST'])
def register():
    body = request.get_json(force=True)
    username = body.get('username', '')
    password = body.get('password', '')

    if not password or not username:
        return 'Invalid credentials', 400
    success = register_user(username, password)
    if not success:
        return 'Username is taken', 403
    else:
        return 'User has been registered successfully', 200


@app.route('/consume', methods=['POST'])
def consume():
    body = request.get_json(force=True)
    queue_name = body.get('queue_name', '')
    timeout = body.get('timeout', 5)
    limit = body.get('limit', 10)


    queues = get_queues()
    queue_exist = False
    for q in queues:
        if q['queue_name'] == queue_name:
            queue_exist = True

    if not queue_name or not queue_exist:
        return 'Invalid queue_name', 400

    chnl = connection.channel()
    messages = []
    chnl.queue_declare(queue_name)
    for method_frame, properties, bdy in chnl.consume(queue_name, inactivity_timeout=timeout):
        if bdy:
            messages.append(str(bdy.decode('utf-8')))

        # Acknowledge the message
        try:
            chnl.basic_ack(method_frame.delivery_tag)
        except Exception as e:
            break

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == limit:
            break

    # Cancel the consumer and return any pending messages
    requeued_messages = chnl.cancel()

    print('Requeued %i messages' % requeued_messages)
    # Close the chnl and the connection
    chnl.close()

    return str(messages), 200


if __name__ == '__main__':
    app.run()
