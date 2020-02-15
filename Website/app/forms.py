from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PlaceBetForm(FlaskForm):
    bet_id = HiddenField('Bet ID')
    team1 = HiddenField('Team 1')
    team2 = HiddenField('Team 2')
    bet = IntegerField('Bet Amount', validators=[DataRequired()])
    team = SelectField('Team, "Left" or "Right"', choices = [('left', 'Left'), ('right', 'Right')], validators=[DataRequired()])
    placeBet = SubmitField('Place Bet')
