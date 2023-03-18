import pytest
from flaskr.translator import OpenAiTranslator


@pytest.fixture
def generate_translator():
    return OpenAiTranslator('Ciao Mondo', 'English, Franch, Chinese')


def test_generate_system_message():
    translator = generate_translator()
    translator.generate_system_message()

    assert translator.system_message == 'You are a super skilled translator who can translate any text to English, French, Chinese.'


def test_generate_behaviour_message():
    translator = generate_translator()
    translator.generate_behaviour_message()

    assert translator.behaviour_message == 'Shure, I can translate anything to English, French, Chinese.'


def test_generate_translated_message():
    translator = generate_translator()
    translator.generate_translated_text()

    assert translator.translated_message == 'Translate this "Ciao Mondo" to English, French, Chinese.'
