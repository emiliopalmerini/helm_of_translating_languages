import os
from flask import Flask, redirect, render_template, request, url_for
import openai
from translator import OpenAiTranslator


openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        language = request.form["languages"]
        
        translator = OpenAiTranslator(text, "gpt-3.5-turbo", language)
        response = translator.generate_prompt()
        
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
