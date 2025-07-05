from fastapi import APIRouter, HTTPException
from ..models.message import Message, MessageCreate, MessageIDRequest
from ..services.message_create import create_message

from ..services.message_delete import delete_message, delete_messages
from ..services.message_fetch import fetch_unread, fetch_time, read_message

router = APIRouter()

# Submit a message
@router.post("/messages/submit", response_model=Message)
def submit_message(msg: MessageCreate):
    return create_message(msg)

# Get unread messages
@router.get("/messages/{recipient}/unread", response_model=list[Message])
def get_unread(recipient: str):
    msgs = fetch_unread(recipient)
    return msgs

# Open(Read) a message
@router.get("/messages/{recipient}/open/{message_id}")
def open_message(recipient: str, message_id: str):
    if not read_message(recipient, message_id):
        raise HTTPException(status_code=404, detail="Message not found")
    return {"status": "read"}

# Get all messages by time
@router.get("/messages/{recipient}")
def get_all(recipient: str, start: int = 0, stop: int = None):
    return fetch_time(recipient, start, stop)

# Delete a message
@router.delete("/messages/{recipient}/delete/{message_id}")
def delete_one(recipient: str, message_id: str):
    if not delete_message(recipient, message_id):
        raise HTTPException(status_code=404, detail="Message not found")
    return {"status": "deleted"}

# Delete several messages
@router.delete("/messages/{recipient}/delete")
def delete_multiple(req: MessageIDRequest):
    deleted_count = delete_messages(req.message_ids)
    return {"deleted": deleted_count}