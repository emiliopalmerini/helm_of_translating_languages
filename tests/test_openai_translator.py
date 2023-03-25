import pytest
from translator import OpenAiTranslator


@pytest.fixture
def generate_translator():
    return OpenAiTranslator('Ciao Mondo', 'English')


def test_generate_system_message(generate_translator):
    assert generate_translator.generate_system_message().to_message() == ' "role": "system", "content": "You are a super skilled translator who can translate any text to [\'English\']." '

def test_generate_behavior_message(generate_translator):
    assert generate_translator.generate_behavior_message().to_message() == ' "role": "assistant", "content": "Shure, I can translate anything to [\'English\']." '


def test_generate_translation_message(generate_translator):
    assert generate_translator.generate_translation_message().to_message() == ' "role": "user", "content": "Translate this "Ciao Mondo" to [\'English\']" '
