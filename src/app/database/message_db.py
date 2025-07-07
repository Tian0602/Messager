from __future__ import annotations
"""
This module defines the SQLAlchemy database model for storing messages.
"""
from sqlalchemy import Column, String, DateTime, Boolean, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from ..models.message import Message

Base = declarative_base()

class MessageDBModel(Base):
    """
    SQLAlchemy ORM model for the messages table.

    Each message is uniquely identified by a composite key: (recipient, id),
    where `id` is an integer scoped per recipient.
    """
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
        """
        Converts this SQLAlchemy model instance to a Pydantic Message object.
        """
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
        """
        Creates a SQLAlchemy MessageDBModel from a Pydantic Message.
        """
        return MessageDBModel(
            id=message.id,
            sender=message.sender,
            recipient=message.recipient,
            content=message.content,
            timestamp=message.timestamp,
            read=message.read
        )