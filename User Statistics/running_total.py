# This method is meant to add up the running total for a player

# userID is a string to access the database
# database is dictionary, userID is the user's ID
def running_total(userID, database):
    total = 0;
    lst = database["user-bets"][userID]
    for i in range(len(lst)):
        total += lst[i]["winnings"]
    return total

