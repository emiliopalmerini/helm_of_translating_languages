import os
from flask import Flask, redirect, render_template, request, url_for
import openai
from flaskr.translator import OpenAiTranslator

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route('/')
	def index():
		if request.method == "POST":
			text = request.form["text"]
			languages = request.form["languages"]
	
			translator = OpenAiTranslator("gpt-3.5-turbo", text, languages)
			response = translator.generate_translation()

			return redirect(url_for("index", result=response.choices[0].text))

		result = request.args.get("result")
		return render_template("index.html", result=result)
	
	# from flaskr import db

	# db.init_app(app)

    # apply the blueprints to the app
	# from flaskr import auth, blog

	# app.register_blueprint(auth.bp)
	# app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
	# app.add_url_rule("/", endpoint="index")

	return app	
