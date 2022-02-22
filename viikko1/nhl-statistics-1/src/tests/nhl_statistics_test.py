import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub().get_players()
        )

    def test_search_returns_none(self):
        self.assertEqual(self.statistics.search("Gretky"), None)

    def test_search_returns_player(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_top_scorers(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")

    def test_team(self):
        self.assertEqual(self.statistics.team("PIT")[0].name, "Lemieux")
