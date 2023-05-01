"""
    Team Class that holds data about a player
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

    printPlayerStats(): prints the stats about a certain player for the user
    
    Returns:
        _type_: _description_
"""

class Player:
    def __init__(self, name, shooting_stats, other_stats, team):
        self.name = name
        self.shooting_stats = shooting_stats
        self.other_stats = other_stats
        self.team = team
    
    def __str__(self):
        return f"\nCurrently Analyzing {self.name}\nPress 1 to get player stats\nPress 2 to show {self.name}'s team\nPress 3 to print graph"
    
    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'shooting_stats':
            return self.shooting_stats
        elif key == 'other_stats':
            return self.other_stats
        elif key == 'team':
            for team in self.team:
                return team
    
    def printPlayerStats(self):
        for name in self.name:
            print(name)
        for stat in self.other_stats:
            print(stat)
        for stat in self.shooting_stats:
            print(stat)