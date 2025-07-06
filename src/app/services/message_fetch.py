from ..models.message import Message
from ..database import SessionLocal
from ..database.message_db import MessageDBModel

def fetch_unread(recipient: str) -> list[Message]:
    """
    Retrieves all unread messages for a given recipient.

    Args:
        recipient (str): The username of the message recipient.

    Returns:
        list[Message]: A list of unread messages.
    """
    db = SessionLocal()
    db_msgs = db.query(MessageDBModel).filter_by(recipient=recipient, read=False).all()
    db.close()
    return [msg.to_message() for msg in db_msgs]

def fetch_time(recipient: str, start: int = 0, stop: int = None) -> list[Message]:
    """
    Retrieves messages for a recipient ordered by timestamp, optionally paginated.

    Args:
        recipient (str): The username of the message recipient.
        start (int): The starting index for pagination (default is 0).
        stop (int | None): The stopping index for pagination (exclusive).

    Returns:
        list[Message]: A list of messages sorted by time.
    """
    db = SessionLocal()
    query = db.query(MessageDBModel).filter_by(recipient=recipient).order_by(MessageDBModel.timestamp)
    if stop is not None:
        query = query.offset(start).limit(stop - start)
    else:
        query = query.offset(start)
    db_msgs = query.all()
    db.close()
    return [msg.to_message() for msg in db_msgs]

def read_message(recipient: str, message_id: str) -> Message | None:
    """
    Marks a message as read and returns the updated message.

    Args:
        recipient (str): The username of the message recipient.
        message_id (str): The ID of the message to mark as read.

    Returns:
        Message | None: The updated message if found, else None.
    """
    db = SessionLocal()
    message = db.query(MessageDBModel).filter_by(id=message_id, recipient=recipient).first()
    if message:
        message.read = True
        db.commit()
        result = message.to_message()
        db.close()
        return result
    db.close()
    return None