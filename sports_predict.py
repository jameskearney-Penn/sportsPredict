import argparse
import json
import csv
import argparse
import pandas as pd
from sp_plot import *
from utils import *
from terminals import *

#First need to determine the encoding of the csv file because pandas was having issues
# The data is from: 
# https://www.kaggle.com/datasets/vivovinco/20222023-nba-player-stats-regular?resource=download
# https://www.kaggle.com/datasets/kalsangsherpa100/nba-2017-23-dataset

# Open the CSV file and read the data

player_df = pd.read_csv('data/encoded-22_23_data.csv')
game_df = pd.read_csv('data/encoded-game_scores.csv')

#We only want games from the 2022-23 seasons to go along with the player stats
two_three_games_df = game_df[game_df["SEASON"] == "2022-23"]

#Now we need to match all the player data to the match data
#The players data has team abbreviation, while the match data has full names
#Using json file found online to match them
# https://github.com/bttmly/nba/blob/master/data/teams.json
f = open('data/teams_json.json', "r")
json_of_teams = json.loads(f.read())
team_dict = {}
for team in json_of_teams:
    team_dict[team["simpleName"]] = team["abbreviation"]
f.close()
for team in team_dict:
    #replace values in pandas df
    two_three_games_df.loc[two_three_games_df["HOME"] == team, "HOME"] = team_dict[team]
    two_three_games_df.loc[two_three_games_df["AWAY"] == team, "AWAY"] = team_dict[team]
team_names = [team_dict[x] for x in team_dict]

#Runs interactive window which introduces users and direfts them to a specific terminal
def runUserInterface():
    while True:
        try:
            print('Hello Welcome to Sports-Predict')
            print("Would you like to Analyze a player or team today?")
            user_input = input("Team or Player ('leave' or Control D- to exit): ")
            
            #If team send to team terminal
            #If player send to player terminal
            #Else run script again
            if user_input == 'leave':
                break
            elif user_input.lower() == "team":
                team = input("Enter in a team to analyze (must be city abbreviation (PHI): ")
                #ensure correct input
                if team not in team_names:
                    print("Team not available. Available teams: ")
                    print(team_names)
                else:
                    #Creates team object and sends to tean terminal
                    print("Loading {}...".format(team))
                    team_obj = createTeamObject(team, two_three_games_df, player_df)
                    analyzeTeamTerminal(team_obj)
            elif user_input.lower() == "player":
                player = input("Enter a player to get statistics about. Please provide the player's full name (ex: Joel Embiid): ")
                #ensure correct input
                if not isPlayer(player, player_df):
                    print("Sorry that player was not found\n")
                else:
                    #Creates team object and sends to tean terminal
                    print("Loading {}...".format(player))
                    player_obj = createPlayerObject(player, player_df)
                    analyzePlayerTerminal(player_obj)
                
        except EOFError:  # triggered by Ctrl+D
            break

"""
optional arguments:
  -h, --help show this help message and exit
  -team_data {ATL,BOS,BKN,CHA,CHI,CLE,DAL,DEN,DET,GSW,HOU,IND,LAC,LAL,MEM,MIA,MIL,MIN,NOP,NYK,OKC,ORL,PHI,PHX,POR,SAC,SAS,TOR,UTA,WAS}
    Provide a team to get statistics about. All teams should be supplied as their city abbreviation (ex: Sixers -> PHI)
  -player_data PLAYER_DATA
    Provide a player to get statistics about. Please provide the player's full name (ex: Joel Embiid)
Returns:

""" 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line access to sportsPredict")
    parser.add_argument("-team_data", type=str, choices=team_names, help="Provide a team to get statistics about. All teams should be supplied as their city abbreviation (ex: Sixers -> PHI)")
    parser.add_argument("-player_data", type=str, help="Provide a player to get statistics about. Please provide the player's full name (ex: Joel Embiid)")
    args = parser.parse_args()
    #print(args.max_fib)

    if args.team_data:
        try:
            team_shooting_data, team_other_data, combined_shooting_data, combined_other_data = getTeamStats(args.team_data, two_three_games_df)
            plot_team(args.team_data, team_shooting_data, team_other_data, combined_shooting_data, combined_other_data)
        except Exception as e:
            print(e)
            print("Could not find data on {}".format(args.team_data))
            print("Enter option -h for help")
    elif args.player_data:
        try:
            player = args.player_data
            player_shooting_stats = getPlayerShootingStats(player, player_df)
            player_other_stats = getPlayerOtherStats(player, player_df)
            plot_player(player, player_shooting_stats, player_other_stats)
        except Exception as e:
            print(e)
            print("Could not find data on {}".format(args.player_data))
            print("Enter option -h for help")
    else:
        runUserInterface()