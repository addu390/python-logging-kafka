from kafka import KafkaConsumer

"""
Python stand-alone consumer for testing
logs produced from Kafka Producer.
"""
consumer = KafkaConsumer('pylog')
for message in consumer:
    print(message)
