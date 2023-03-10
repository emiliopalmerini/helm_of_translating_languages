import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {generate_system()},
                {generate_behaviour()},
                {
                    generate_translation(
                        text,
                        [
                            "English",
                            "German",
                            "Spanish",
                            "French",
                            "Japanese",
                            "Chinese",
                        ],
                    )
                },
            ],
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_system():
    return {
        "role": "system",
        "content": "You are a super skilled translator who can translate any text to any language.",
    }


def generate_behaviour():
    return {"role": "assistant", "content": "Shure, I can translate in any language."}


def generate_translation(text, languages):
    return {
        "role": "user",
        "content": """ Translate this "{text}" to {languages}""".format(
            text=text, languages=", ".join(languages)
        ),
    }
