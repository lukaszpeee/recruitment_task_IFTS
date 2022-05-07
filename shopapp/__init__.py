from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5a4a87cfd86446fabb3c8b134dbc2048'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopapp.db'
db = SQLAlchemy(app)

from shopapp import routes
