from ..models.message import Message
from ..database import SessionLocal
from ..database.message_db import MessageDBModel

class DatabaseMessageStorage:
    def save(self, message: Message):
        db = SessionLocal()
        db.add(MessageDBModel.from_message(message))
        db.commit()
        db.close()

    def get(self, recipient: str, message_id: str) -> Message | None:
        db = SessionLocal()
        db_obj = db.query(MessageDBModel).filter_by(id=message_id, recipient=recipient).first()
        db.close()
        return db_obj.to_message() if db_obj else None