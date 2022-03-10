import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        self.assertEqual(kori.hinta(), 0)
        self.assertEqual(kori.tavaroita_korissa(), 0)
    def test_yhden_tuotteen_lisaamisen_jalkeen_yksi_tavara(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.tavaroita_korissa(), 1)
    def test_kahden_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.tavaroita_korissa(), 2)

