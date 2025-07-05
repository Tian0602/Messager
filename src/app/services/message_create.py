from ..models.message import Message, MessageCreate
from ..database import SessionLocal
from ..database.message_db import MessageDBModel


# Submit a message
def create_message(msg_data: MessageCreate) -> Message:
    message = Message(**msg_data.dict())
    db = SessionLocal()
    db_message = MessageDBModel.from_message(message)
    db.add(db_message)
    db.commit()
    db.close()
    return message