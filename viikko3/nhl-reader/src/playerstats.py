class PlayerStats:
    def __init__(self, players):
      self.players = players


    def top_scorers_by_nationality(self, nationality):
      finnish_players = []

      for player in self.players:
        if player.nationality == "FIN":
          finnish_players.append(player)

      finnish_players.sort(key=lambda x:x.points, reverse=True)

      return finnish_players

