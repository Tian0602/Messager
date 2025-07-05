from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Internal Used
class Message(BaseModel):
    id: Optional[int] = None
    sender: Optional[str]
    recipient: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    read: bool = False

# Incoming Request for Creation
class MessageCreate(BaseModel):
    sender: Optional[str]
    recipient: str
    content: str
