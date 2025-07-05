from ..models.message import Message
from ..database import SessionLocal
from ..database.message_db import MessageDBModel

# Fetch unread messages
def fetch_unread(recipient: str) -> list[Message]:
    db = SessionLocal()
    db_msgs = db.query(MessageDBModel).filter_by(recipient=recipient, read=False).all()
    db.close()
    return [msg.to_message() for msg in db_msgs]

# Fetch messages ordered by time
def fetch_time(recipient: str, start: int = 0, stop: int = None) -> list[Message]:
    db = SessionLocal()
    query = db.query(MessageDBModel).filter_by(recipient=recipient).order_by(MessageDBModel.timestamp)
    if stop is not None:
        query = query.offset(start).limit(stop - start)
    else:
        query = query.offset(start)
    db_msgs = query.all()
    db.close()
    return [msg.to_message() for msg in db_msgs]

# Mark a message as read
def read_message(recipient: str, message_id: str) -> bool:
    db = SessionLocal()
    message = db.query(MessageDBModel).filter_by(id=message_id, recipient=recipient).first()
    if message:
        message.read = True
        db.commit()
        db.close()
        return True
    db.close()
    return False