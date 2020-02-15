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

DATABASE FORMAT: (retrieve_database() returns dict)
database (dict)
     "users" (dict)
        retrieve user using user_id in string form (dict)
          "username" (string)
          "total" (float)
          "total-history" (list of tuples -- (time, result))
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
          "timestamp" (int)

"""

import json, time, copy


def update_users(user, filepath):
    if user["user_id"] in data["users"]:
        return
    new_user = copy.deepcopy(user)
    new_user.pop("user_id")
    new_user["total-history"] = []
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        data["users"][user["user_id"]] = new_user
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def update_bets():
    new_data = scrape_update()
'''
retrieve bets -- update bet data and if winner determined,
calculate winnings and add to user total and total-history
'''

def new_user_bets(user_bet, filepath):
    bet = copy.deepcopy(user_bet)
    bet.pop("user_id")
    bet["timestamp"] = time.time()
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        if user_bet["user_id"] in data["user-bets"]:
            data["user-bets"][user_bet["user_id"]].append(bet)
        else:
            data["user-bets"][user_bet["user_id"]] = [bet]
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def retrieve_database(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        return data
