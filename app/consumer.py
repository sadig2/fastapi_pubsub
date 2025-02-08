from kafka import KafkaConsumer
import json

print("Starting Kafka consumer...")

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received message: {message.value}")