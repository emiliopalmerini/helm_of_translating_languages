from app import generate_translation
import pytest

def generate_translation_should_generate():
    assert generate_translation("Hello World", "English") == {
        "role": "user",
        "content": """Translate this "{text}" to English""".format(text="Hello World"),
    }
