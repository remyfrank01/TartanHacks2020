from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import *
from app.models import User
from random import randint
import sys
from app.database.main import *

# Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user, live_bets=live_bets)

# User System Pages
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Get the user from the database
        user = User(id='012345',username='peepee',password_hash='?')#User.query.filter_by(username=form.username.data).first()
        print(form.password.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Then login the user
        login_user(user, remember=form.remember_me.data)
        #flash('Login requested for user {}, password: {},remember_me={}'.format(
        #    form.username.data, form.password.data, form.remember_me.data))
        #id = randint(0,999999)
        #update_users({'user_id':id, 'username':form.username.data, 'total':10},
        #                'C://Users/kelti/Documents/GitHub/TartanHacks2020/website/app/database/data.json')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html', title="Signed Out")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    # Get the user from the database
    user = User(id='012345',username='peepee',password_hash='?')#User.query.filter_by(username=username).first_or_404()
    bets =  [
                {
                    "bet_id": "234798",
                    "team": "Duke",
                    "value": 50,
                    "winnings": 130.75,
                    "net": 80.75
                },
                {
                    "bet_id": "000001",
                    "team": "Clippers",
                    "value": 100,
                    "winnings": 0,
                    "net": -100,
                    "timestamp": 1581744828.133449
                }
            ]
    return render_template('user.html', user=user, bets=bets)

# Betting Divisions
@app.route('/nba', methods=['GET', 'POST'])
def nba():
    form = PlaceBetForm()
    live_bets = [
        {
         'bet_id' : "000001",
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'bet_id' : "000001",
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'bet_id' : "000001",
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'bet_id' : "000001",
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
        {
         'bet_id' : "000001",
         'team1' : 'Clippers',
         'team2' : 'Celtics',
         'line1' : 1,
         'line2' : -1,
         'odds1' : -110,
         'odds2' : -110
        },
    ]
    if form.validate_on_submit():
        flash('Bet of {} placed for {}'.format(
            form.bet.data, form.team.data))
        if form.team.data == 'left':
            team = form.team1.data
        else:
            team = form.team2.data
        new_user_bets({'user_id':"508234", 'bet_id':form.bet_id.data, 'team':team, 'value':form.bet.data},
                        'C://Users/kelti/Documents/GitHub/TartanHacks2020/website/app/database/data.json')
        return redirect(url_for('nba'))
    return render_template('nba.html', title='SafeBet - NBA', form=form, live_bets=live_bets)
