from kafka import KafkaConsumer, KafkaProducer
import json
from collections import deque

# Configuración del consumidor
consumer = KafkaConsumer(
    'document-changes',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    group_id='document-group',
    auto_offset_reset='earliest'
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

clients = ['Client 1', 'Client 2']
#Copia del documento del servidor
document = ""

#Se leen los tópicos de los clientes
for message in consumer:
    change = message.value.get('change', {})
    #Se añade el caracter
    if change.get('type') == 'add':
        document = document + change.get('char')
        #se envía update a los clientes
        #if(message.value.get('client')) == 'Client 1':
        #    change['pos'] = len(document)
        #    producer.send('update', change)
    #Se elimina el caracter
    else:
        document = document[:-1]
    print("Copia del documento en servidor: " + document)