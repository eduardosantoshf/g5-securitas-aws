from kombu import Exchange, Producer
import kombu
import json



def send_message_to_broker(broker_url, broker_username, broker_password, exchange_name, queue_name, camera_id):
    # Create Connection String
    connection_string = f"amqp://{broker_username}:{broker_password}" \
        f"@{broker_url}/"        
    print(f"Connecting to {connection_string}")
    
    try:
        # Kombu Connection
        kombu_connection = kombu.Connection(
            connection_string,
            ssl=True
        )
        kombu_channel = kombu_connection.channel()
    except Exception as e:
        print(f"Error connecting to message broker: {e}")
        return False

    # Kombu Exchange
    kombu_exchange = Exchange(
        name=exchange_name,
        type="direct",
        delivery_mode=1
    )

    # Kombu Producer
    kombu_producer = Producer(
        exchange=kombu_exchange,
        channel=kombu_channel
    )

    # Kombu Queue
    kombu_queue = kombu.Queue(
        name=queue_name,
        exchange=kombu_exchange
    )
    kombu_queue.maybe_bind(kombu_connection)
    kombu_queue.declare()
    
    print("aqui")
    
    try:
        kombu_producer.publish(
            body=json.dumps({"camera_id": camera_id}),
            content_type="application/json",
            headers={
                "camera_id": camera_id
            }
        )                
        return True
    except Exception as e:
        print(f"Error sending message to message broker: {e}")
        return False