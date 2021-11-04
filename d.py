class Flervalg:
    def __init__(self, spørsmål, alternativ, svar):
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.svar = svar

    def __str__(self):
        spm = self.spørsmål + "\n"
        for i, string in enumerate(self.alternativ):
            spm += str(i+1) + ": " + string + "\n"
        return spm


    def sjekk_svar(self, svaret):
        svar_bruker = svaret-1
        svar = int(self.svar)
        if svar_bruker == svar:
            return "Riktig \n"
        else:
            return "Feil \n"


    def poeng(self, svaret):
        poeng = 0
        svar = int(self.svar)
        svar_bruker = svaret-1
        if svar_bruker == svar:
            poeng = 1
        return poeng



    def korrekt_svar_tekst(self):
        riktig_svar_nr = int(self.svar)
        svarene = self.alternativ
        return "\nRiktig svar er svaralternativ " + str(riktig_svar_nr) + ": " + (svarene[riktig_svar_nr]) + ".\n"


if __name__== "__main__":
    alternativ = []
    spiller1_poeng = 0
    spiller2_poeng = 0

    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fila:
        for linje in fila:
            ordene = linje.replace(',',':').replace("[","").replace("]","").split(":")
            spørsmål = ordene[0]
            lengde = len(ordene)
            svar = ordene[1]
            for i in range(2, lengde):
                alternativ.append(ordene[i])
            print1 = Flervalg(spørsmål, alternativ, svar)
            print(print1)
            spiller1_svar = int(input("Spiller 1. Nr: "))
            spiller2_svar = int(input("Spiller 2. Nr: "))
            print(print1.korrekt_svar_tekst())
            print("Spiller 1: " + print1.sjekk_svar(spiller1_svar))
            print("Spiller 2: " + print1.sjekk_svar(spiller2_svar))
            spiller1_poeng += print1.poeng(spiller1_svar)
            spiller2_poeng += print1.poeng(spiller2_svar)
            spørsmål = 0
            svar = 0
            alternativ.clear()
            lengde = 0
            ordene.clear()

    print(f"Poengsummen for spiller 1 er: {spiller1_poeng}.")
    print(f"Poengsummer for spiller 2 er: {spiller2_poeng}.")
    fila.close()
