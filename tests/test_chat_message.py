import pytest
from flaskr.chat_message import ChatMessage



def test_to_message():
    obj = ChatMessage("test_role", "test_content")
    assert obj.to_message() == """ "role": "test_role", "content": "test_content" """


@pytest.mark.parametrize("message", [
    ChatMessage(None, "test_content"),
    ChatMessage("test_role", None),
])
def test_to_message_exception(message):
    with pytest.raises(ValueError):
        message.to_message()
