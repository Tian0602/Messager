from ..models.message import Message, MessageCreate
from ..data.memory import storage


# Submit a message
def create_message(msg_data: MessageCreate) -> Message:
    message = Message(**msg_data.dict())
    recipient = message.recipient
    if recipient not in storage:
        storage[recipient] = {}
    storage[recipient][str(message.id)] = message
    return message