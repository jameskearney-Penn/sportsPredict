import pandas as pd
from team import Team
from player import Player

def getPlayerShootingStats(player, player_df):
    return player_df[player_df["Player"] == player][["FG%", "3P%", "2P%", "FT%"]].iloc[0]

def getPlayerOtherStats(player, player_df):
    return player_df[player_df["Player"] == player][["Age", "G", "GS", "MP"]].iloc[0]

def getTeamPlayers(team, player_df):
    return player_df[player_df["Tm"] == team]

def getTeamStats(team, games_df):
    #Stats when team was home team
    team_home = games_df[games_df["HOME"] == team][[
        "W_HOME",
        "HOME_FG_PCT",
        "HOME_FG3_PCT",
        "HOME_FT_PCT",
        "HOME_TURNOVERS",
        "HOME_TOT_REB"
    ]]
    team_home_wins = team_home[["W_HOME"]].agg(sum)
    team_home_data = team_home[["HOME_FG_PCT", "HOME_FG3_PCT", "HOME_FT_PCT", "HOME_TURNOVERS", "HOME_TOT_REB"]].agg("mean")
    
    #Stats when team was away team
    team_away = games_df[games_df["AWAY"] == team][[
        "W_AWAY",
        "AWAY_FG_PCT",
        "AWAY_FG3_PCT",
        "AWAY_FT_PCT",
        "AWAY_TURNOVERS",
        "AWAY_TOT_REB"
    ]]
    team_away_wins = team_away[["W_AWAY"]].agg(sum)
    team_away_data = team_away[["AWAY_FG_PCT", "AWAY_FG3_PCT", "AWAY_FT_PCT", "AWAY_TURNOVERS", "AWAY_TOT_REB"]].agg("mean")
    
    #Split up data into shooting data and other information
    team_shooting_data = pd.concat([team_home_data[["HOME_FG_PCT", "HOME_FG3_PCT", "HOME_FT_PCT"]], team_away_data[["AWAY_FG_PCT", "AWAY_FG3_PCT", "AWAY_FT_PCT"]]])
    team_other_data = pd.concat([team_home_wins, team_home_data[["HOME_TURNOVERS", "HOME_TOT_REB"]], team_away_wins, team_away_data[["AWAY_TURNOVERS", "AWAY_TOT_REB"]]])
    
    #create combined stats 
    total_wins = team_away_wins[["W_AWAY"]].iloc[0] + team_home_wins[["W_HOME"]].iloc[0]
    total_fg = (team_away_data[["AWAY_FG_PCT"]].iloc[0] + team_home_data[["HOME_FG_PCT"]].iloc[0]) / 2
    total_fg3 = (team_away_data[["AWAY_FG3_PCT"]].iloc[0] + team_home_data[["HOME_FG3_PCT"]].iloc[0]) / 2
    total_ft = (team_away_data[["AWAY_FT_PCT"]].iloc[0] + team_home_data[["HOME_FT_PCT"]].iloc[0]) / 2
    total_turnovers = team_away_data[["AWAY_TURNOVERS"]].iloc[0] + team_home_data[["HOME_TURNOVERS"]].iloc[0]
    total_reb = team_away_data[["AWAY_TOT_REB"]].iloc[0] + team_home_data[["HOME_TOT_REB"]].iloc[0]
    combined_other_data = [total_wins, total_turnovers, total_reb]
    combined_shooting_data = [total_fg, total_fg3, total_ft]

    return team_shooting_data, team_other_data, combined_shooting_data, combined_other_data

def createTeamObject(team, game_df, player_df):
    team_shooting_data, team_other_data, combined_shooting_data, combined_other_data = getTeamStats(team, game_df)
    players = getTeamPlayers(team, player_df)
    return Team(
        name=team,
        shooting_stats = team_shooting_data,
        other_stats = team_other_data,
        combined_shooting_stats = combined_shooting_data,
        combined_other_stats = combined_other_data,
        players = players
    )

def isPlayer(player, player_df):
    if player_df[player_df["Player"] == player].empty:
        return False
    return True

def createPlayerObject(player, player_df):
    player_shooting_data = getPlayerShootingStats(player, player_df)
    player_other_data = getPlayerOtherStats(player, player_df)
    team = player_df[player_df["Player"] == player][["Tm"]].iloc[0]
    return Player(
        name=player,
        shooting_stats = player_shooting_data,
        other_stats = player_other_data,
        team = team,
    )