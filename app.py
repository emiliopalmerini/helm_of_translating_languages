import os
from flask import Flask, redirect, render_template, request, url_for
import openai

from translator import OpenAiTranslator

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]

        translator = OpenAiTranslator(text, "gpt-3.5-turbo", language)
        translation = translator.translate()
        response = openai.ChatCompletion.create(
            model="{model}".format(model=translator.model),
            messages=translation,
        )
        # response['choices'][0]['message']['content']

        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)
