import requests
from player import Player

def sorting(player):
    return player.points

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    finnish_players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['goals'],
                player_dict['assists']
            )

            finnish_players.append(player)


    print("Players from FIN:")

    lista = []

    for player in finnish_players:
        print(player.points)

    for player in finnish_players:
        lista.append((player.points, player.name))

    lista.sort(reverse=True)

    for player in lista:
        print(player)


if __name__ == "__main__":
    main()
