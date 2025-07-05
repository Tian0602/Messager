from ..models.message import Message

# recipient -> {message_id -> Message}
storage: dict[str, dict[str, Message]] = {}
