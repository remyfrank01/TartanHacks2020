"""
Database Functions

update_users(user)
/*@requires type(user) == dict &&
            len(user) == 3 &&
            type(user["user_id"]) == string &&
            type(user["username"]) == str &&
            type(user["total"]) == float @*/
//@ensures user in data.json

new_user_bets(user_bet)
/*@requires type(user_bet) == dict &&
            len(user_bet) ==  4&&
            type(user_bet["user_id"]) == string &&
            type(user_bet["bet_id"]) == string &&
            type(user_bet["team"]) == string &&
            type(user_bet["value"]) == float @*/
//@requires user_bet["team"] in (bet["bet_id"]["team1"], bet["bet_id"]["team2"])
//@ensures user_bet in data.json

update_bets()
//@ensures all data and bets are up to date

DATABASE FORMAT:
database (dict)
     "users" (dict)
        retrieve user using user_id in string form (dict)
          "username" (string)
          "total" (float)
     "user-bets" (dict)
        retrieve list of bets from each user using user_id in string form (list)
          for each element (dict):
            "bet_id" (str)
            "team" (str)
            "value" (float)
            "winnings" (float)
            "net" (float)
            "timestamp" (float)
     "bets" (dict)
        retrieve bet using bet_id in string form (dict)
          "team1" (string)
          "team2" (string)
          "line1" (float)
          "line2" (float)
          "odds1" (int)
          "odds2" (int)
          "winner" (string -- "None" if no winner yet)

"""

import json

def update_users(user):
    with open('data.json') as json_file:
        data = json.load(json_file)
        data["users"].append(user)

def update_bets():
    scrape_update()

def new_user_bets(user_bet):
    with open('data.json') as json_file:
        data = json.load(json_file)
        if user_bet["user_id"] in data["user-bets"]:
            
        else:
            data["user-bets"][user_bet["user_id"]] = []