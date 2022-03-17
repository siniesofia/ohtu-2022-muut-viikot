KAPASITEETTI = 5
OLETUSKASVATUS = 5

def arvon_asetus(tarkistettava_arvo, oletuksena_tallennettava_arvo):
    if tarkistettava_arvo is None:
        return oletuksena_tallennettava_arvo
    elif not isinstance(tarkistettava_arvo, int) or tarkistettava_arvo < 0:
        raise Exception("Ei käy")  
    else:
        return tarkistettava_arvo


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = arvon_asetus(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = arvon_asetus(kasvatuskoko, OLETUSKASVATUS)
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono:
            return True

        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                uusi_ljono = self.ljono[:]
                self.ljono = uusi_ljono
                for i in (0, self.alkioiden_lkm):
                    uusi_ljono.append(0)
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False



    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in range(0, len(a_taulu)):
            z.lisaa(a_taulu[luku])

        for luku in range(0, len(b_taulu)):
            z.poista(b_taulu[luku])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
