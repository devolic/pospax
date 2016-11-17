from flask import Flask, render_template, request
from flask_babel import Babel
from flask_mail import Mail
from flask_script import Manager
from flask_marshmallow import Marshmallow
from database import db

app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)
mail = Mail(app)
manager = Manager(app)
ma = Marshmallow(app)

db.init_app(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['th'])


@app.errorhandler
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


from werkzeug.utils import import_string

for module in app.config['BLUEPRINTS']:
    app.register_blueprint(import_string(module))
