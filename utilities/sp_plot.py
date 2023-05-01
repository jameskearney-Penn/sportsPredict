import matplotlib.pyplot as plt
import numpy as np

#Want to have ways to visualize the data so users can examine stats raw
"""
Function that plots the stats of a certain player from the players dataframe

Args:
    player, player_shooting_stats, player_other_stats

Returns:
    Saves a graph in stats folder as stats/{player_name}_stat.png
"""
def plot_player(player, player_shooting_stats, player_other_stats):
    fig, (ax1, ax2) = plt.subplots(2, 1)
    
    #plots shooting percentages
    y_ticks = np.arange(0, 1, 0.1)
    x_shooting_axis = ["FG%", "3P%", "2P%", "FT%"]
    y_shooting_axis = player_shooting_stats
    ax1.bar(x_shooting_axis, y_shooting_axis, label="{}'s Shooting Stats".format(player))
    ax1.set_yticks(y_ticks)
    
    #plots age, game and minute numbers
    y_ticks = np.arange(0, 85, 10)
    x_other_stats_axis = ["Age", "Games", "Games Started", "#Minutes"]
    y_other_stats_axis = player_other_stats
    ax2.bar(x_other_stats_axis, y_other_stats_axis, label="{}'s Game and Age Stats".format(player))
    ax2.set_yticks(y_ticks)
    
    #Attach legends and save figure
    ax1.legend()
    ax2.legend()
    fig.savefig("stats/{}_stat.png".format(player))
    print("Graph saved in stats folder as stats/{}_stat.png".format(player))

"""
Function that plots the stats of a certain team from the games dataframe

Args:
    team, team_shooting_data, team_other_data, combined_shooting_data, combined_other_data

Returns:
    Saves a graph in stats folder as stats/{team_name}_stat.png
"""
def plot_team(team, team_shooting_data, team_other_data, combined_shooting_data, combined_other_data):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    
    #plots shooting percentages
    y_ticks = np.arange(0, 1, 0.1)
    x_shooting_axis = ["hFG", "h3P", "hFT", "aFG", "a3P", "aFT"]
    y_shooting_axis = team_shooting_data
    ax1.bar(x_shooting_axis,y_shooting_axis, label="{}'s Shooting Stats".format(team))
    ax1.set_yticks(y_ticks)
    
    #plots age, game and minute numbers
    y_ticks = np.arange(0, 85, 10)
    x_other_stat_axis = ["H_Ws", "H_TOs", "H_Rebs", "A_Ws", "A_TOs", "A_Rebs"]
    y_other_stat_axis = team_other_data
    ax2.bar(x_other_stat_axis, y_other_stat_axis, label="{}'s Game and Age Stats".format(team))
    ax2.set_yticks(y_ticks)
    
    y_ticks = np.arange(0, 1, 0.1)
    x_other_stat_axis = ["FG%", "3P%", "FT%"]
    y_other_stat_axis = combined_shooting_data
    ax3.bar(x_other_stat_axis, y_other_stat_axis, label="{}'s Combined Shooting Stats".format(team))
    ax3.set_yticks(y_ticks)
    
    y_ticks = np.arange(0, 135, 15)
    x_other_stat_axis = ["Ws", "TOs", "Rebs"]
    y_other_stat_axis = combined_other_data
    ax4.bar(x_other_stat_axis, y_other_stat_axis, label="{}'s Combined Game and Age Stats".format(team))
    ax4.set_yticks(y_ticks)
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    fig.savefig("stats/{}_stat.png".format(team))
    print("Graph saved in stats folder as stats/{}_stat.png".format(team))