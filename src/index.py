from varasto import Varasto

def luonnin_jalkeen():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(f"Mehuvarasto: {mehua}\nOlutvarasto: {olutta}")
    print(f"Olut getterit:\nsaldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")
    print("Mehu setterit: \nLisätään 50.7")
def lisaa_olutta():
    olutta = Varasto(100.0, 20.2)
    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def lisaa_mehua():
    mehua = Varasto(100.0)
    print(f"Mehuvarasto: {mehua}\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def virheet():
    print(f"Virhetilanteita:\nVarasto(-100.0);\n{Varasto(-100.0)}")
    print(f"Varasto(100.0, -50.7)\n {Varasto(100.0, -50.7)}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    luonnin_jalkeen()
    mehua.lisaa_varastoon(50.7)

    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    virheet()

    lisaa_olutta()

    lisaa_mehua()

    print(f"Olutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    print(f"saatiin {olutta.ota_varastosta(1000.0)} \nOlutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)")
    print(f"saatiin {mehua.ota_varastosta(-32.9)}\nMehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
    print("Maitoa ja leipää")