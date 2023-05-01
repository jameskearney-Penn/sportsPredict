# sportsPredict

## Description
sportsPredict allows users to quickly search up statistics about NBA teams and players. sportsPredict used data from Kaggle in order to build a terminal interface using Python that provides stastics on the 2022-23 NBA season. 

https://www.kaggle.com/datasets/vivovinco/20222023-nba-player-stats-regular?resource=download
https://www.kaggle.com/datasets/kalsangsherpa100/nba-2017-23-dataset




## Running sportsPredict
sportsPredict is run through the terminal

- Interactive console: 
```python 
python3.9 sports_predict.py
```
- With optional arguments:
```python 
python3.9 sports_predict.py -player_data -team_data -h
```
### Interactive console
- Welcome Terminal
```ubuntu 
Hello Welcome to Sports-Predict
Would you like to Analyze a player or team today?
Team or Player ('leave' or Control D- to exit):
```

- Player Terminal
```ubuntu 
Team or Player ('leave' or Control D- to exit): Player
Enter a player to get statistics about. Please provide the player's full name (ex: Joel Embiid): Joel Embiid
Loading Joel Embiid...

Currently Analyzing Joel Embiid
Press 1 to get player stats
Press 2 to show Joel Embiid's team
Press 3 to print graph
'back' or Control-D to return): 
```
### Optional Arguments
- -h, --help show this help message and exit
- -team_data, Provide a team to get statistics about. All teams should be supplied as their city abbreviation (ex: Sixers -> PHI)
{ATL,BOS,BKN,CHA,CHI,CLE,DAL,DEN,DET,GSW,HOU,IND,LAC,LAL,MEM,MIA,MIL,MIN,NOP,NYK,OKC,ORL,PHI,PHX,POR,SAC,SAS,TOR,UTA,WAS}
- -player_data, Provide a player to get statistics about. Please provide the player's full name (ex: Joel Embiid)


## Requirements
- One class definition (two dunder methods)
  - team.py
  - player.py
- One non-trivial first-party module (modules that come built-in with python
  - argparse, json
- Two non-trivial third-party modules (modules that need to be installed)
  - pandas, numpy, matplotlib
- In-line documentation and code style: each function should have proper documentation (similar to the docstrings we have provided in each assignment)
  - Check below and in python files

## Code Structure
### sports_predict.py
- `runUserInterface(games_df, players_df)`:
```ubuntu 
Function that runs the interactive window which introduces users and directs
them to a specific terminal

Args:
    games_df (NBA_GAME_DATAFRAME), players_df (NBA_PLAYER_STATS_DATAFRAME)

Returns:
    NONE
```

- `__main__`:
```ubuntu 
Function that loads data from csvs and handles optional arguments

Args:
    NONE

Returns:
    NONE (or create a new png if optional arguments provided)
    

optional arguments:
  - h, --help show this help message and exit
  - team_data {ATL,BOS,BKN,CHA,CHI,CLE,DAL,DEN,DET,GSW,HOU,IND,LAC,LAL,MEM,MIA,MIL,MIN,NOP,NYK,OKC,ORL,PHI,PHX,POR,SAC,SAS,TOR,UTA,WAS} 
    - Provide a team to get statistics about. All teams should be supplied as their city abbreviation (ex: Sixers -> PHI)
  - player_data PLAYER_DATA
    Provide a player to get statistics about. Please provide the player's full name (ex: Joel Embiid)
```


### Utilities
#### utils.py
- `getPlayerShootingStats(player, player_df):`:
```ubuntu 
Function that gets the shooting stats a certain player from the players datafra,e

Args:
    player (name of player to get), players_df (NBA_PLAYER_STATS_DATAFRAME)

Returns:
    The FG%", "3P%", "2P%", "FT% of the player as a ()
```

- `getPlayerOtherStats(player, player_df):`:
```ubuntu 
Function that gets the others stats of certain player from the players dataframe

Args:
    player (name of player to get), players_df (NBA_PLAYER_STATS_DATAFRAME)

Returns:
    The "Age", "G", "GS", "MP" of the player as a (pd.series)
```

- `getTeamPlayers(team, player_df):`:
```ubuntu 
Function that gets the others stats of certain player from the players dataframe

Args:
    team (name of team to get players from), games_df (NBA_GAME_DATAFRAME)

Returns:
    The subset of the players_df that play on a certain team
```

- `getTeamStats(team, games_df):`:
```ubuntu 
Function that gets the stats of a certain team from the games dataframe

Args:
    team (name of team to get players from), games_df (NBA_GAME_DATAFRAME)

Returns:
    team_shooting_data: "HOME_FG_PCT", "HOME_FG3_PCT", "HOME_FT_PCT", "AWAY_FG_PCT", "AWAY_FG3_PCT", "AWAY_FT_PCT"
    team_other_data: "W_HOME", "HOME_TURNOVERS", "HOME_TOT_REB", "W_AWAY", "AWAY_TURNOVERS", "AWAY_TOT_REB"
    combined_shooting_data: "FG_PCT", "FG3_PCT", "FT_PCT"
    combined_other_data: "W", "TURNOVERS", "TOT_REB"
```

- `createTeamObject(team, game_df, player_df):`:
```ubuntu 
Function that creates a Team Object from the Team Class

Args:
    team (name of team to get players from), players_df (NBA_PLAYER_STATS_DATAFRAME), games_df (NBA_GAME_DATAFRAME)

Returns:
    Team Object
```

- `createPlayerObject(player, player_df):`:
```ubuntu 
Function that creates a Player Object from the Player Class

Args:
    team (name of team to get players from), players_df (NBA_PLAYER_STATS_DATAFRAME)

Returns:
    Player Object
```

- `isPlayer(player, player_df):`:
```ubuntu 
Function that determines whether or not a player is in the players dataframe

Args:
    player (name of player to check), players_df (NBA_PLAYER_STATS_DATAFRAME)

Returns:
    Bool
```

#### sp_plot.py
- `plot_player(player, player_shooting_stats, player_other_stats):`:
```ubuntu 
Function that plots the stats of a certain player from the players dataframe

Args:
    player, player_shooting_stats, player_other_stats

Returns:
    Saves a graph in stats folder as stats/{player_name}_stat.png
```

- `plot_team(team, team_shooting_data, team_other_data, combined_shooting_data, combined_other_data):`:
```ubuntu 
Function that plots the stats of a certain team from the games dataframe

Args:
    team, team_shooting_data, team_other_data, combined_shooting_data, combined_other_data

Returns:
    Saves a graph in stats folder as stats/{team_name}_stat.png
```


#### terminals.py
- `analyzeTeamTerminal(team)`:
```ubuntu 
Function that runs the team terminal that interacts with the user

Args:
    team (a Team Object)

Returns:
    None
```

- `analyzePlayerTerminal(team)`:
```ubuntu 
Function that runs the player terminal that interacts with the user

Args:
    player (a Player Object)

Returns:
    None
```

### Classes
#### team.py
```python 
class Team:
```
```ubuntu 
Team Class that holds data about a team
    Init:
    - name
    - shooting_stats
    - other_stats
    - combined_shooting_stats
    - combined_other_stats
    - players
    
    __str__: Returns text prompt for a user to analyze a specific team
    
    _getitem_: allows for specific information to be returned from the Team Object

    printTeamStats(): prints the stats about a certain team for the user
```

#### player.py
```python 
class Player:
```
```ubuntu
Player Class that holds data about a player
    Init:
    - name
    - age
    - games
    - games_started
    - minutes_per_game
    - fg
    - 3fg
    - 2fg
    - ft
    
    __str__: Returns text prompt for a user to analyze a specific player
    
    _getitem_: allows for specific information to be returned from the Player Object

    printPlayerStats(): prints t
```
