from unittest.mock import patch
import pika

def callback_func(channel, method, properties, body):
    print("Message consumed:", body)

@patch("pika.BlockingConnection", spec=pika.BlockingConnection)
def mock_publish(mock_conn):
    def side_effect_publish(exchange, routing_key, body):
        print(f"Message published to {routing_key}:", body)

    # reroute basic_publish call to side_effect_publish 
    mock_conn.return_value.channel.return_value.basic_publish.side_effect = side_effect_publish

    # execute publishing code
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.basic_publish(exchange="",
                    routing_key="QUEUE",
                    body="{ Hello World! }")
    connection.close()

@patch("pika.BlockingConnection", spec=pika.BlockingConnection)
def mock_consume(mock_conn):
    def side_effect_consume():
        callback_func(mock_conn.return_value.channel, None, None, "{ Hello World! }")

    # reroute start_consuming to side_effect_consume
    mock_conn.return_value.channel.return_value.start_consuming.side_effect = side_effect_consume

    # execute consuming code
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.basic_consume("QUEUE", on_message_callback=callback_func) # this on_message_callback does nothing
    channel.start_consuming()
    connection.close()

mock_publish()
mock_consume()