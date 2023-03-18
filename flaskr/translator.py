from flaskr.chat_message import *
from openai import ChatCompletion


# class OpenAiBot:
#     def __init__(self, **kwargs):
#         self.model = kwargs.get('model')
#         self.prompt = kwargs.get('prompt')
#         self.set_temperature(kwargs.get('temperature'))

#     def set_temperature(self, temperature):
#         if temperature is not None or "":
# return float(temperature)


class OpenAiTranslator():
    def __init__(self, text, languages=['en']):
        self.text = text
        self.languages = languages

    def generate_system_message(self):
        return SystemMessage(
            """You are a super skilled translator who can translate any text to {language}.""".format(
                language=self.languages),
        )

    def generate_behaviour_message(self):
        return BehaviourMessage(
            """Shure, I can translate anything to {language}.""".format(language=self.languages))

    def generate_translated_text(self):
        return UserMessage(
            """Translate this "{text}" to {language}""".format(
                text=self.text, language=self.language)
        )

    def generate_translation(self):
        system = self.generate_system_message()
        behaviour = self.generate_behaviour_message()
        translation = self.generate_translated_text()
        return ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {system.to_message()},
                {behaviour.to_message()},
                {translation.to_message()},
            ],
        )
