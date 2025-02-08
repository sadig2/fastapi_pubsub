from pydantic import BaseModel


class Message(BaseModel):
    message: str
    metadata: dict = None  # Optional field