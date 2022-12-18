import kombu
from kombu.mixins import ConsumerMixin

class Consumer(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(queues=self.queues, callbacks=[self.on_message]),
        ]

    def on_message(self, body, message):
        print("Alarm triggered!")
        message.ack()

class Alarm:
    kombu_connection = None
    kombu_exchange = None
    kombu_channel = None
    kombu_producer = None
    kombu_queue = None

    def __init__(self, alarm_id):
        self.alarm_id = alarm_id

    def attach_to_message_broker(self, broker_url, broker_username,
                                 broker_password, exchange_name, queue_name):
        # Create Connection String
        connection_string = f"amqp://{broker_username}:{broker_password}" \
            f"@{broker_url}/"

        # Kombu Connection
        self.kombu_connection = kombu.Connection(
            connection_string,
            ssl=True
        )
        self.kombu_connection.connect()
        print("Successfully connected to the broker!")

        self.kombu_channel = self.kombu_connection.channel()

        # Kombu Exchange
        self.kombu_exchange = kombu.Exchange(
            name=exchange_name,
            type="direct",
            delivery_mode=1
        )

        # Kombu Queue
        self.kombu_queue = kombu.Queue(
            name=queue_name,
            exchange=self.kombu_exchange
        )
        self.kombu_queue.maybe_bind(self.kombu_connection)
        self.kombu_queue.declare()

    
    def listen_to_notifications(self):
        # Start Human Detection Workers
        self.cameras_worker = Consumer(
            connection=self.kombu_connection,
            queues=self.kombu_queue
        )
        self.cameras_worker.run()
