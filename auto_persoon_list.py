class Persoon():

    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
        self.autos = []
    def __str__(self):
        return "{} {}".format(self.naam,self.leeftijd)
    def voeg_auto_toe(self,auto):
        self.autos.append(auto)
    def toon_autos_info(self):
        for auto in self.autos:
            print(auto)
    def voeg_nieuwe_auto(self):#Hier wordt een nog niet bestaande instantie van auto
                               # aangemaakt en toevoegd
        merk = input("geef het merk")
        model = input("geef het model")
        bouwjaar = int(input("geef het bouwjaar"))
        nieuwe_auto = Auto(merk,model,bouwjaar)
        self.voeg_auto_toe(nieuwe_auto)


class Auto():

    def __init__(self,merk,model,bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
    def __str__(self):
        return "{} {} {}".format(self.merk,self.model,self.bouwjaar)


p2 = Persoon("Dario",23)
a = Auto("Fiat","500",1990)
a2 = Auto("Ferrari","Spider",2023)
a3 = Auto("Audi","RS 6",2023)
p2.voeg_auto_toe(a)
p2.voeg_auto_toe(a2)
p2.voeg_auto_toe(a3)
p2.voeg_nieuwe_auto()
p2.toon_autos_info()
print("einde")
