from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Komentotehdas:
    def __init__(self):
        # self.io = io

        self.komennot = {
            "summa": Summa(self.io),
            "erotus": Erotus(self.io),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

        # return Tuntematon(self.io)

class Summa:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
        # self.io = io

    def suorita(self):
        self._sovellus.plus(self._arvo)

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            # Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            # Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            # Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }
    
    # ...
    def hae(self, komento):
        if komento in self._komennot:
            return self._komennot[komento]

        # return Tuntematon(self.io)

    def _lue_syote(self):
        return self._syote_kentta.get()



    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)

# class Kayttoliittyma:
#     def __init__(self, sovellus, root):
#         self._sovellus = sovellus
#         self._root = root

#     def kaynnista(self):
#         self._tulos_var = StringVar()
#         self._tulos_var.set(self._sovellus.tulos)
#         self._syote_kentta = ttk.Entry(master=self._root)

#         tulos_teksti = ttk.Label(textvariable=self._tulos_var)

#         summa_painike = ttk.Button(
#             master=self._root,
#             text="Summa",
#             command=lambda: self._suorita_komento(Komento.SUMMA)
#         )

#         erotus_painike = ttk.Button(
#             master=self._root,
#             text="Erotus",
#             command=lambda: self._suorita_komento(Komento.EROTUS)
#         )

#         self._nollaus_painike = ttk.Button(
#             master=self._root,
#             text="Nollaus",
#             state=constants.DISABLED,
#             command=lambda: self._suorita_komento(Komento.NOLLAUS)
#         )

#         self._kumoa_painike = ttk.Button(
#             master=self._root,
#             text="Kumoa",
#             state=constants.DISABLED,
#             command=lambda: self._suorita_komento(Komento.KUMOA)
#         )

#         tulos_teksti.grid(columnspan=4)
#         self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
#         summa_painike.grid(row=2, column=0)
#         erotus_painike.grid(row=2, column=1)
#         self._nollaus_painike.grid(row=2, column=2)
#         self._kumoa_painike.grid(row=2, column=3)

#     def _suorita_komento(self, komento):
#         arvo = 0
#         try:
#             arvo = int(self._syote_kentta.get())
#         except Exception:
#             pass


#         if komento == Komento.SUMMA:
#             self._sovellus.plus(arvo)
#         elif komento == Komento.EROTUS:
#             self._sovellus.miinus(arvo)
#         elif komento == Komento.NOLLAUS:
#             self._sovellus.nollaa()
#         elif komento == Komento.KUMOA:
#             pass

#         self._kumoa_painike["state"] = constants.NORMAL

#         if self._sovellus.tulos == 0:
#             self._nollaus_painike["state"] = constants.DISABLED
#         else:
#             self._nollaus_painike["state"] = constants.NORMAL

#         self._syote_kentta.delete(0, constants.END)
#         self._tulos_var.set(self._sovellus.tulos)
