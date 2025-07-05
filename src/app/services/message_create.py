from ..models.message import Message, MessageCreate
from ..database import SessionLocal
from ..database.message_db import MessageDBModel
from sqlalchemy import func
from datetime import datetime

# Submit a message
def create_message(msg_data: MessageCreate) -> Message:
    db = SessionLocal()
    # Get current max message_id for this recipient
    max_id = db.query(func.max(MessageDBModel.id))\
               .filter_by(recipient=msg_data.recipient).scalar()

    next_id = (int(max_id) if max_id is not None else 0) + 1
    time_stamp = datetime.now()
    db_message = MessageDBModel(
        recipient=msg_data.recipient,
        id=next_id,
        sender=msg_data.sender,
        content=msg_data.content,
        timestamp = time_stamp
    )
    db.add(db_message)
    db.commit()
    db.close()

    return Message(
        id=next_id,
        recipient=msg_data.recipient,
        sender=msg_data.sender,
        content=msg_data.content,
        timestamp=time_stamp,
        read=False
    )