import json
from kafka import KafkaConsumer
import time
#Kafka consumer from topic sales
def kafka_consumer():
    consumer = KafkaConsumer('sales',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        message = message.value
        time.sleep(1/100)
        print(message)

kafka_consumer()