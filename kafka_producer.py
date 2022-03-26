from kafka import KafkaProducer
import json
import time
import random
import datetime

#Kafka Producer to topic sales
#sale has todays date, product, amount, price
def kafka_producer(sale):
    topic_name = 'sales'
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.send(topic_name, json.dumps(sale).encode('utf-8'))


list_of_itens =[{'name': 'Book', 'price': 10},{'name': 'Video Game', 'price': 20},{'name': 'Computer', 'price': 30}, {'name': 'T-Shirt', 'price': 40}]
#produce a sale every 2 seconds and send it to topic sales 
#total produced should be 10
def main():
    topic_name = 'sales_v2'
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    i = 0
    while i < 1000000:
        i += 1
        item = random.choice(list_of_itens)
        amount = random.randint(1,10)
        sale = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'product': item['name'],
            'amount': amount,
            'price': item['price'],
            'total': amount * item['price']
        }
        producer.send(topic_name, json.dumps(sale).encode('utf-8'))
        time.sleep(5/10)

main()
