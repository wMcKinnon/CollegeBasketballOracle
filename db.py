#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CollegeRatings.sqlite3'

db = SQLAlchemy(app)
class CollegeRatings(db.Model):
    id = db.Column("College_ID", db.integer, primary_key=True)
    name = db.Column(db.String(20))
    netRank = db.Column(db.Integer)
    kenpomRating = db.Column(db.Float)
    barttorvikRating = db.Column(db.Float)

def __repr__(self):
    return f"({self.name} {self.netRank} {self.kenpomRating} {self.barttovikRating})"