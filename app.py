# Simple website practice using Python and Flask

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Cactus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(80), unique=True, nullable=False)
    family = db.Column(db.String(80), nullable=True)
    sub_family = db.Column(db.String(80), nullable=True)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Plant %r' % self.id


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
