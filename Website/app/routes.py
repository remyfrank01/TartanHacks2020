from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import sys
from random import randint

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'keltin42'}
    live_bets = [
        {
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        }
    ]
    # import bet data
    return render_template('index.html', title='Home', user=user, live_bets=live_bets)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password: {},remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data))
        id = randint(0,2^10)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
