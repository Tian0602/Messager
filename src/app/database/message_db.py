from __future__ import annotations
from sqlalchemy import Column, String, DateTime, Boolean, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
from ..models.message import Message

Base = declarative_base()

class MessageDBModel(Base):
    __tablename__ = "messages"

    id = Column(Integer, nullable=False)
    sender = Column(String, nullable=True)
    recipient = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    read = Column(Boolean, default=False)

    __table_args__ = (
        PrimaryKeyConstraint('recipient', 'id'),
    )
    def to_message(self):
        
        return Message(
            id=self.id,
            sender=self.sender,
            recipient=self.recipient,
            content=self.content,
            timestamp=self.timestamp,
            read=self.read
        )

    @staticmethod
    def from_message(message: Message) -> MessageDBModel:
        return MessageDBModel(
            id=message.id,
            sender=message.sender,
            recipient=message.recipient,
            content=message.content,
            timestamp=message.timestamp,
            read=message.read
        )