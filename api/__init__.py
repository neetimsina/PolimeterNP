from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xpzupniv:T9dyWSQc1cF3JRUCkSLYUU7j6aadQvsC@batyr.db.elephantsql.com/xpzupniv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Polimeter Nepal !!'

