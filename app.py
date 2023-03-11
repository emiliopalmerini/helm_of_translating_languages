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
        language = request.form["language"]

        system = ChatMessage(
            "system",
            """You are a super skilled translator who can translate any text to {language}.""".format(
                language=language),
        )

        behaviour = ChatMessage(
            "assistant", """Shure, I can translate anything to {language}.""".format(language=language))

        translation = ChatMessage(
            "user",
            """ Translate this "{text}" to {language}""".format(
                text=text, language=language)
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {system.to_message()},
                {behaviour.to_message()},
                {translation.to_message()},
            ],
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
