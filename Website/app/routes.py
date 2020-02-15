from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import *
from random import randint
import sys
#sys.path.append('/database')
from app.database.main import *

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
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Get the user from the database
        #user = User.query.filter_by(username=form.username.data).first()
        #if user is None or not user.check_password(form.password.data):
        #    flash('Invalid username or password')
        #    return redirect(url_for('login'))
        # Then login the user
        # login_user(user, Remember=form.remember_me.data)
        flash('Login requested for user {}, password: {},remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data))
        id = randint(0,999999)
        update_users({'user_id':id, 'username':form.username.data, 'total':10},
                        'C://Users/kelti/Documents/GitHub/TartanHacks2020/website/app/database/data.json')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

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
