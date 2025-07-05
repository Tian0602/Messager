from ..database import SessionLocal
from ..database.message_db import MessageDBModel

def delete_message(recipient: str, message_id: int) -> bool:
    """
    Deletes a single message for a given recipient.

    Args:
        recipient (str): The username of the recipient.
        message_id (int): The message ID to be deleted.

    Returns:
        bool: True if the message was found and deleted, False otherwise.
    """
    db = SessionLocal()
    message = db.query(MessageDBModel).filter_by(id=message_id, recipient=recipient).first()
    if message:
        db.delete(message)
        db.commit()
        db.close()
        return True
    db.close()
    return False

def delete_messages(recipient: str, message_ids: list[int]) -> int:
    """
    Deletes multiple messages for a given recipient.

    Args:
        recipient (str): The username of the recipient.
        message_ids (list[int]): A list of message IDs to delete.

    Returns:
        int: The number of successfully deleted messages.
    """
    db = SessionLocal()
    count = 0
    for message_id in message_ids:
        if delete_message(recipient, message_id):
            count += 1
    db.commit()
    db.close()
    return count