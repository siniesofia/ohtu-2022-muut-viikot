# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

def main():
    ostoskori = Ostoskori()
    maito = Tuote("maito", 5)
    piima = Tuote("piima", 6)

    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    ostoskori.tavaroita_korissa()
    print(ostoskori.tavaroita_korissa())
    ostoskori.lisaa_tuote(maito)
    print(ostoskori.tavaroita_korissa())
    ostoskori.lisaa_tuote(maito)
    ostoskori.lisaa_tuote(piima)
    ostoskori.lisaa_tuote(piima)
    print(ostoskori.tavaroita_korissa())





if __name__ == "__main__":
    main()
