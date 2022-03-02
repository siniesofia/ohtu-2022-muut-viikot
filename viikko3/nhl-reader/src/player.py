class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self.name = name
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.points = goals + assists


    def __str__(self):
        return f"{self.name:25}{self.nationality:5}{self.points}"
