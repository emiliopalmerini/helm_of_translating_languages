from flaskr.chat_message import ChatMessage


def test_to_json():
    obj = ChatMessage("test_role", "test_content")
    assert obj.to_message() == """ "role": "test_role", "content": "test_content" """
