from kauppa import Kauppa
from kirjanpito import Kirjanpito
# from viitegeneraattori import Viitegeneraattori
# from varasto import Varasto
# from pankki import Pankki

from kirjanpito import kirjanpito as default_kirjanpito
# from pankki import pankki as default_pankki
# from viitegeneraattori import viitegeneraattori as default_viitegeneraattori
# from varasto import varasto as default_varasto




def main(kirjanpito=default_kirjanpito):
    # kauppa = Kauppa(
    #     Varasto.get_instance(),
    #     Pankki.get_instance(),
    #     Viitegeneraattori.get_instance()
    # )
    # viitegeneraattori = Viitegeneraattori()
    # kirjanpito = Kirjanpito()
    # varasto = Varasto(kirjanpito)
    # pankki = Pankki(kirjanpito)
    # kauppa = Kauppa(varasto, pankki, viitegeneraattori)
    kauppa = Kauppa()





    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    for tapahtuma in kirjanpito.tapahtumat:
        print(tapahtuma)


if __name__ == "__main__":
    main()
