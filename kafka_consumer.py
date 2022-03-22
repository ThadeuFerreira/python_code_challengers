import json
from kafka import KafkaConsumer
import time
from typing import List

import postgresql

#Kafka consumer from topic sales
def kafka_consumer():
    consumer = KafkaConsumer('sales',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    sales = []
    #get at least 10 sales from topic sales and save on postgress
    for message in consumer:
        sale = message.value
        sales.append(sale)
        if len(sales) == 10:
            postgress_save(sales)
            sales = []

#Save sale on postgress
def postgress_save(sales: List[dict]):
    cursor, connection = postgresql.connect()
    #create table sales if not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS sales (id SERIAL PRIMARY KEY, date VARCHAR(50) NOT NULL, product VARCHAR(50) NOT NULL, amount INTEGER NOT NULL, price INTEGER NOT NULL, total INTEGER NOT NULL)")	
    for sale in sales:
        cursor.execute("INSERT INTO sales (date, product, amount, price, total) VALUES (%s, %s, %s, %s, %s)", (sale['date'], sale['product'], sale['amount'], sale['price'], sale['total']))
    print("{} sales added to table sales!".format(len(sales)))
    connection.commit()
kafka_consumer()