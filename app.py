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
            messages=[{generate_prompt(text)}],
            temperature=0.6
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return """ Translate to 
        English, 
        Spanish,
        French, 
        German,
        Japanese""".format(text.capitalize())