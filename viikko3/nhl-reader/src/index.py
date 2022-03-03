from playerreader import PlayerReader
from playerstats import PlayerStats

def sorting(player):
    return player.points

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
