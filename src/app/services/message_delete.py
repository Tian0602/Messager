from ..data.memory import storage

# Delete a single message
def delete_message(recipient: str, message_id: str) -> bool:
    message = storage.get(recipient, {}).get(message_id)
    if message:
        del storage[recipient][message_id]
        return True
    return False

# Delete messages
def delete_messages(message_ids: list[str]) -> int:
    count = 0
    for message_id in message_ids:
        if delete_message(message_id):
            count += 1
    return count