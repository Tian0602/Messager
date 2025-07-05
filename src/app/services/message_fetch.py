from ..models.message import Message
from ..data.memory import storage

# Fetch unread messages
def fetch_unread(recipient: str) -> list[Message]:
    messages = storage.get(recipient, {})
    return [msg for msg in messages.values() if not msg.read]

# Fetch messages ordered by time
def fetch_time(recipient: str, start: int = 0, stop: int = None) -> list[Message]:
    messages = storage.get(recipient, {})
    sorted_msgs = sorted(messages.values(), key=lambda msg: msg.timestamp)
    return sorted_msgs[start:stop]

# Mark a message as read
def read_message(recipient: str, message_id: str) -> bool:
    message = storage.get(recipient, {}).get(message_id)
    if message:
        message.read = True
        return True
    return False