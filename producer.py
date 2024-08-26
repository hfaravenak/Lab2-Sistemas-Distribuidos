from kafka import KafkaProducer
import json
import time
import random

# Configuración del productor
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulación de clientes
clients = ['Client 1', 'Client 2']
n = 10
# Enviar cambios de documento
while n > 0:
    client = random.choice(clients)
    #Se escoge un tipo de cambio para enviar al "servidor", un caracter y un "cliente" remitente
    change = {
        'type': random.choice(['add', 'remove']),
        'char': random.choice('abcdefghijklmnopqrstuvwxyz'),
        'pos': 0
    }
    position = random.randint(0, 10) if change['type'] == 'add' else random.randint(0, 10)
    message = {
        'client': client,
        'change': change,
        'position': position,
        'timestamp': int(time.time())
    }
    print(f"{client} is sending: {message}")
    producer.send('document-changes', message)
    n = n - 1
#Se espera a que se envíen los tópicos
time.sleep(5)