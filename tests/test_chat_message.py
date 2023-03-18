import pytest
from flaskr.chat_message import ChatMessage, UserMessage, SystemMessage 

def test_ChatMessage_to_message():
    obj = ChatMessage("test_role","test_content")
    assert obj.to_message() == """ "role": "test_role", "content": "test_content" """


@pytest.mark.parametrize("message", [
    ChatMessage(None, None),
    ChatMessage(None, "test_content"),
    ChatMessage("test_role", None),
    ChatMessage(None, ""),
    ChatMessage("", None),
    ChatMessage("", "test_content"),
    ChatMessage("test_role", ""),
    ChatMessage("",""),
])
def test_ChatMessage_to_message_exception(message):
    with pytest.raises(ValueError):
        message.to_message()

def test_UserMessage_to_message():
    obj = UserMessage("test_content")
    assert obj.to_message() == """ "role": "user", "content": "test_content" """


@pytest.mark.parametrize("message", [
    UserMessage(None),
    UserMessage(""),
])
def test_ChatMessage_to_message_exception(message):
    with pytest.raises(ValueError):
        message.to_message()

def test_BehaviorMessage_to_message():
    obj = BehaviorMessage("test_content")
    assert obj.to_message() == """ "role": "assistant", "content": "test_content" """


@pytest.mark.parametrize("message", [
    BehaviorMessage(None),
    BehaviorMessage(""),
])
def test_ChatMessage_to_message_exception(message):
    with pytest.raises(ValueError):
        message.to_message()

def test_SystemMessage_to_message():
    obj = SystemMessage("test_content")
    assert obj.to_message() == """ "role": "system", "content": "test_content" """


@pytest.mark.parametrize("message", [
    SystemMessage(None),
    SystemMessage(""),
])
def test_ChatMessage_to_message_exception(message):
    with pytest.raises(ValueError):
        message.to_message()