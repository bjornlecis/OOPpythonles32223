class Persoon():

    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return "{} {}".format(self.naam,self.leeftijd)
    def voeg_auto_toe(self,auto):
        self.auto = auto
    def toon_auto_info(self):
        print(self.auto.__str__())


class Auto():

    def __init__(self,merk,model,bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
    def __str__(self):
        return "{} {} {}".format(self.merk,self.model,self.bouwjaar)

p = Persoon("Ben",30)
p2 = Persoon("Dario",23)
a = Auto("Fiat","500",1990)
a2 = Auto("Ferrari","Spider",2023)
p.voeg_auto_toe(a)
p.toon_auto_info()
p2.voeg_auto_toe(a2)
p2.toon_auto_info()
p2.voeg_auto_toe(a)
p2.toon_auto_info()


