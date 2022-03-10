from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self.ostoskori:
            lukumaara += ostos.lukumaara()
        return lukumaara

    def hinta(self):
        hinta = 0
        for ostos in self.ostoskori:
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return 
        self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoskori.remove(ostos)


    def tyhjenna(self):
        self.ostoskori = []
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
