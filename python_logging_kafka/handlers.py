from logging import StreamHandler
from kafka import KafkaProducer


class KafkaHandler(StreamHandler):

    def __init__(self, broker, topic):
        StreamHandler.__init__(self)
        self.broker = broker
        self.topic = topic

        self.kafka_broker = MyKafka(broker)

    def emit(self, record):
        message = self.format(record)
        self.kafka_broker.send(message, self.topic)


class MyKafka(object):

    def __init__(self, kafka_brokers, json=False):
        self.json = json
        if not json:
            self.producer = KafkaProducer(bootstrap_servers=kafka_brokers)
        else:
            self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                          bootstrap_servers=kafka_brokers)

    def send(self, data, topic):
        if self.json:
            result = self.producer.send(topic, key=b'log', value=data)
        else:
            result = self.producer.send(topic, bytes(data, 'utf-8'))
        print("kafka send result: {}".format(result.get()))
