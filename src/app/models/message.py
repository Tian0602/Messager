from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

# Internal Used
class Message(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    sender: Optional[str]
    recipient: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    read: bool = False

# Incoming Request for Creating
class MessageCreate(BaseModel):
    sender: Optional[str]
    recipient: str
    content: str

# Incoming Request for Openning and Deleting
class MessageIDRequest(BaseModel):
    message_ids: list[str]