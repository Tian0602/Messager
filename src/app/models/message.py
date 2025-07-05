"""
This module defines the Pydantic model for message-related API operations.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    """
    Represents a message stored in the system.

    Attributes:
        id (Optional[int]): Unique message ID scoped per recipient.
        sender (Optional[str]): Username of the sender.
        recipient (str): Username of the recipient.
        content (str): The body of the message.
        timestamp (datetime): Time when the message was created.
        read (bool): Flag indicating if the message has been read.
    """
    id: Optional[int] = None
    sender: Optional[str]
    recipient: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    read: bool = False

class MessageCreate(BaseModel):
    """
    Schema for incoming message creation requests.

    Attributes:
        sender (Optional[str]): Username of the sender.
        recipient (str): Username of the recipient.
        content (str): The body of the message to be created.
    """
    sender: Optional[str]
    recipient: str
    content: str
