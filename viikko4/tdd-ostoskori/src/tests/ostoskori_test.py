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
    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_sama_kuin_tuotteen_hinta(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.hinta(), 5)
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        piima = Tuote("piima", 3)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(piima)
        self.assertEqual(kori.tavaroita_korissa(), 2)
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_sama_kuin_tuotteiden_hintojen_summa(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        piima = Tuote("piima", 3)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(piima)
        self.assertEqual(kori.hinta(), 8)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.tavaroita_korissa(), 2)
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_sama_kuin_2_x_tuotteen_hinta(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.hinta(), 10)
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_tuote(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        self.assertEqual(len(kori.ostokset()), 1)
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_ostos_jolla_sama_nimi_ja_lukumaara_1(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.ostokset()[0].tuotteen_nimi(), "maito")
        self.assertEqual(kori.ostokset()[0].lukumaara(), 1)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        self.assertEqual(len(kori.ostokset()), 1)
        self.assertEqual(kori.ostokset()[0].lukumaara(), 2)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_sama_nimi_kuin_tuotteella(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        self.assertEqual(kori.ostokset()[0].lukumaara(), 2)
        self.assertEqual(kori.ostokset()[0].tuotteen_nimi(), "maito")
    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_ostos_jossa_tuotetta_1_kpl(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.lisaa_tuote(maito)
        kori.poista_tuote(maito)
        self.assertEqual(kori.ostokset()[0].lukumaara(), 1)
    def test_jos_koriin_lisätty_tuote_poistetaan_on_kori_tyhja(self):
        kori = Ostoskori()
        maito = Tuote("maito", 5)
        kori.lisaa_tuote(maito)
        kori.poista_tuote(maito)
        self.assertEqual(len(kori.ostokset()), 0)
        self.assertEqual(kori.tavaroita_korissa(), 0)


