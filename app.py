import os
from flaskr.chat_message import ChatMessage

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        languages = request.form["languages"]

        system = ChatMessage(
            "system",
            "You are a super skilled translator who can translate any text to any language.",
        )
        behaviour = ChatMessage("assistant", "Shure, I can translate in any language.")
        translation = ChatMessage(
            "user",
            """ Translate this "{text}" to {languages}""".format(
                text=text, languages=", ".join(languages)
            ),
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {system.print_to_json()},
                {behaviour.print_to_json()},
                {translation.print_to_json()},
            ],
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    # TODO: handle result
    return render_template("index.html", result=result)


# def generate_system():
#     return {
#         "role": "system",
#         "content": "You are a super skilled translator who can translate any text to any language.",
#     }


# def generate_behaviour():
#     return {"role": "assistant", "content": "Shure, I can translate in any language."}


# def generate_translation(text, languages):
#     return {
#         "role": "user",
#         "content": """ Translate this "{text}" to {languages}""".format(
#             text=text, languages=", ".join(languages)
#         ),
#     }
