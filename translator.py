from chat_message import *


# class OpenAiBot:
#     def __init__(self, **kwargs):
#         self.model = kwargs.get('model')
#         self.prompt = kwargs.get('prompt')
#         self.set_temperature(kwargs.get('temperature'))

#     def set_temperature(self, temperature):
#         if temperature is not None or "":
# return float(temperature)


class OpenAiTranslator():
    def __init__(self, text, model, language=['English']):
        self.text = text
        self.model = model
        self.language = language

    def generate_system_message(self):
        return SystemMessage(
            """You are a super skilled translator who can translate any text to {language}.""".format(
                language=self.language),
        )

    def generate_behavior_message(self):
        return BehaviorMessage(
            """Shure, I can translate anything to {language}.""".format(language=self.language))

    def generate_translation_message(self):
        return UserMessage(
            """Translate this "{text}" to {language}""".format(
                text=self.text, language=self.language)
        )

    def translate(self):
        system = self.generate_system_message().to_message()
        behavior = self.generate_behavior_message().to_message()
        translation = self.generate_translation_message().to_message()

        messages = [
            {"role": system[0], "content": system[1]},
            {"role": behavior[0], "content": behavior[1]},
            {"role": translation[0], "content": translation[1]}
        ]

        return messages
