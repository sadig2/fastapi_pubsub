from fastapi import FastAPI, Body
from kafka import KafkaProducer
import json

from schemas import Message

app = FastAPI()

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


@app.post("/publish")
async def publish_message(message: Message):
    # Send message to 'messages' topic
    message_data = message.model_dump()
    print("miau", type(message_data))
    producer.send('messages', message_data)
    return {"status": "Message sent to Kafka"}
