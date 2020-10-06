from kafka import KafkaConsumer

consumer = KafkaConsumer('pylog')
for message in consumer:
    print(message)
