from kafka import KafkaConsumer
consumer = KafkaConsumer('pyblog')
for message in consumer:
    print (message)