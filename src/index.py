from varasto import Varasto


def tiedot_varastosta(varasto: Varasto):
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def status_tulostus(lista: list):
    for tup in lista:
        print(f"{tup[0]}: {tup[1]}")


def varaston_muokkaus(varasto, muokkaus, maara, varaston_nimi):
    if muokkaus == "lisaa":
        varasto.lisaa_varastoon(maara)
        print(f"Lisätään {maara}")
    elif muokkaus == "ota":
        varasto.ota_varastosta(maara)
        print(f"Otetaan {maara}")
    print(f"{varaston_nimi}: {varasto}")


def tulosta_varasto(alku, lisays=0):
    varasto = Varasto(alku, lisays)
    tuloste = f"Varasto({alku}"
    if lisays:
        tuloste += f", {lisays}"
    tuloste += ")"
    if not lisays:
        tuloste += ";"
    print(tuloste)
    print(varasto)


def tulosta_virhetilanteet():
    print("Virhetilanteita:")
    tulosta_varasto(-100.0)
    tulosta_varasto(100.0, -50.7)


def olut1(olutta: Varasto):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


def mehu1(mehua: Varasto):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def olut2(olutta: Varasto):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def mehu2(mehua: Varasto):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    status_tulostus([("Mehuvarasto", mehua), ("Olutvarasto", olutta)])
    print("Olut getterit:")
    tiedot_varastosta(olutta)

    print("Mehu setterit:")
    varaston_muokkaus(mehua, "lisaa", 50.7, "Mehuvarasto")
    varaston_muokkaus(mehua, "ota", 3.14, "Mehuvarasto")
    tulosta_virhetilanteet()
    olut1(olutta)
    mehu1(mehua)
    olut2(olutta)
    mehu2(mehua)


if __name__ == "__main__":
    main()
