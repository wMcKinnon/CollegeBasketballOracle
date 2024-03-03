# WTF
# using flask wt-forms
# activate the venv
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
# add SelectField
from wtforms import StringField, SubmitField, SelectField

class CbboForm(FlaskForm):
   name=StringField("Your Prediction")
   
   # the order here does not matter
   submit = SubmitField("Enter")
   
   # http://wtforms.simplecodes.com/docs/0.6.1/fields.html
   home_team = SelectField(u'Home Team', 
   choices=[('Colorado', 'Colorado Buffaloes'), ('Washington', 'Washington Huskies'), 
   ('Washington State', 'Washington State Cougers'), ('Oregon', 'Oregon Ducks'), 
   ('Oregon State', 'Oregon State Beavers'),  ('Stanford', 'Stanford Cardinal'), ('California', 'California Bears'), ('USC', 'USC Trojans'), 
   ('UCLA', 'UCLA Bruins'),  ('Arizona', 'Arizona Wildcats'),  ('Arizona State', 'Arizona State Sun Devils'),  ('Utah', 'Utah Utes')])

   away_team = SelectField(u'Away Team', 
   choices=[('Colorado', 'Colorado Buffaloes'), ('Washington', 'Washington Huskies'), 
   ('Washington State', 'Washington State Cougers'), ('Oregon', 'Oregon Ducks'), 
   ('Oregon State', 'Oregon State Beavers'),  ('Stanford', 'Stanford Cardinal'), ('California', 'California Bears'), ('USC', 'USC Trojans'), 
   ('UCLA', 'UCLA Bruins'),  ('Arizona', 'Arizona Wildcats'),  ('Arizona State', 'Arizona State Sun Devils'),  ('Utah', 'Utah Utes')])


   