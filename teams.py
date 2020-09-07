# TODO Create an empty list to maintain the player names
team_roster = []


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_players = input("Would you like to add a player to the roster? (Yes/No) ")
while add_players == 'yes':
    name = input("Enter the name of the player to add to the team: ")
    team_roster.append(name)
    add_players = input("Would you like to add another player? (Yes/No) ")

# TODO print the number of players on the team
print("There are {} players on the team".format(len(team_roster)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_num = 1
for player in team_roster:
    print("Player {}: {}".format(player_num, player))
    player_num += 1

# TODO Select a goalkeeper from the above roster
keeper = input("Please select the gaolkeeper by selecting the player number. 1-{} ".format(len(team_roster)))
keeper = int(keeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great!!! The goalkeeper for the game will be {}".format(team_roster[keeper - 1]))
