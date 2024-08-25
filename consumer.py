from kafka import KafkaConsumer
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

# Documento representado como una lista de caracteres
document = deque()

def apply_change(document, change, position):
    if change['type'] == 'add' and 'char' in change:
        document.insert(position, change['char'])
    elif change['type'] == 'remove':
        if 0 <= position < len(document):
            del document[position]

def process_message(message):
    change = message.get('change', {})
    position = message.get('position', 0)
    apply_change(document, change, position)
    print(f"Updated document: {''.join(document)}")

# Procesar mensajes en orden de llegada
for message in consumer:
    process_message(message.value)
    print(f"Updated document: {''.join(document)}")
