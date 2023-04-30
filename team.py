"""
    Team Class that holds data about a team
    Init:
    - name
    - shooting_stats
    - other_stats
    - combined_shooting_stats
    - combined_other_stats
    - players
    
    Str: Returns text prompt for a user to analyze a specific team
    _getitem_: allows for specific information to be returned from the Team Object

    Returns:
        _type_: _description_
"""

class Team:
    
    def __init__(self, name, shooting_stats, other_stats, combined_shooting_stats, combined_other_stats, players):
        self.name = name
        self.shooting_stats = shooting_stats
        self.other_stats = other_stats
        self.combined_shooting_stats = combined_shooting_stats
        self.combined_other_stats = combined_other_stats
        self.players = players
    
    def __str__(self):
        return f"\nCurrently Analyzing {self.name}\nPress 1 to get team stats\nPress 2 to get players\nPress 3 to print graphs"
    
    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'shooting_stats':
            return self.shooting_stats
        elif key == 'other_stats':
            return self.other_stats
        elif key == 'combined_shooting_stats':
            return self.combined_shooting_stats
        elif key == 'combined_other_stats':
            return self.combined_other_stats
        elif key == 'players':
            return self.players
    
    def printTeamStats(self):
        shooting_titles = ["FG%", "3P%", "FT%"]
        other_titles = ["Ws", "TOs", "Rebs"]
        print(self.name.rstrip(),"Stats: ")
        for i, stat in enumerate(self.combined_other_stats):
            print("    ", other_titles[i], ": ", stat)
        print(self.name,"Shooting Stats: ")
        for i, stat in enumerate(self.combined_shooting_stats):
            print("    ", shooting_titles[i], ": ", stat)
        print(self.name,"Home Stats: ")
        for i, stat in enumerate(self.other_stats):
            if i < 3:
                print("    ", other_titles[i - 3], ": ", stat)
        for i, stat in enumerate(self.shooting_stats):
            if i < 3:
                print("    ", shooting_titles[i - 3], ": ", stat)
        print(self.name,"Away Stats: ")
        for i, stat in enumerate(self.other_stats):
            if i >= 3:
                print("    ", other_titles[i - 3], ": ", stat)
        for i, stat in enumerate(self.shooting_stats):
            if i >= 3:
                print("    ", shooting_titles[i - 3], ": ", stat)
