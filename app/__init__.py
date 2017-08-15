from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
session = defaultdict()

from app import view, model
db.create_all()