from ..database import SessionLocal
from ..database.message_db import MessageDBModel

# Delete a single message
def delete_message(recipient: str, message_id: str) -> bool:
    db = SessionLocal()
    message = db.query(MessageDBModel).filter_by(id=message_id, recipient=recipient).first()
    if message:
        db.delete(message)
        db.commit()
        db.close()
        return True
    db.close()
    return False

# Delete messages
def delete_messages(message_ids: list[str]) -> int:
    db = SessionLocal()
    count = 0
    for message_id in message_ids:
        message = db.query(MessageDBModel).filter_by(id=message_id).first()
        if message:
            db.delete(message)
            count += 1
    db.commit()
    db.close()
    return count