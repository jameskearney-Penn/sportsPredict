from .sp_plot import *

"""
Function that runs the team terminal that interacts with the user

Args:
    team (a Team Object)

Returns:
    None
"""
def analyzeTeamTerminal(team):
    while True:
        try:
            print(team)
            user_input = input("('back' or Control-D to return): ")
            if user_input == 'back':
                break
            elif user_input == '1':
                team.printTeamStats()
            elif user_input == '2':
                print(team['players'])
            elif user_input == '3':
                plot_team(team['name'], team['shooting_stats'], team['other_stats'], team['combined_shooting_stats'], team['combined_other_stats'])        
        except EOFError:  # triggered by Ctrl+D
            break

"""
Function that runs the player terminal that interacts with the user

Args:
    player (a Player Object)

Returns:
    None
"""
def analyzePlayerTerminal(player):
    while True:
        try:
            print(player)
            user_input = input("('back' or Control-D to return): ")
            if user_input == 'back':
                break
            elif user_input == '1':
                player.printTeamStats()
            elif user_input == '2':
                print(player['team'])
            elif user_input == '3':
                plot_player(player['name'], player['shooting_stats'], player['other_stats'])      
        except EOFError:  # triggered by Ctrl+D
            break
