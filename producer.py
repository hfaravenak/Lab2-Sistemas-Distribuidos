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

# Enviar cambios de documento
while True:
    client = random.choice(clients)
    change = {
        'type': random.choice(['add', 'remove']),
        'char': random.choice('abcdefghijklmnopqrstuvwxyz') if random.choice([True, False]) else None
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
    time.sleep(random.uniform(0.5, 2))
