class Student:

    def __init__(self,naam,leeftijd,punt):
        self.naam = naam
        self.leeftijd = leeftijd
        self.punt = punt

    def __str__(self):
        return "Student: {} is {} jaar en heeft {} % ".format(self.naam,self.leeftijd,self.punt)

    def toon_student_info(self):
        print(self.__str__())

    def toon_alle_leerlingen(self):
        leerlingen = klas_a + klas_b
        for leerling in leerlingen:
            print(leerling)
    def veranderpunt(self):
        punt = int(input("punt in"))
        if 0 < punt < 101:
            self.punt = punt

s = Student("Bert",22,85)
s2 = Student("Cindy",21,82)
s3 = Student("Dennis",24,75)
s4 = Student("Erika",20,68)
s5 = Student("Alex",21,76)
s6 = Student("Zoe",19,91)
s7 = Student("Guido",18,49)
s8 = Student("Lindsay",22,68)
#s7.veranderpunt()

klas_a = [s,s3,s5,s7]
klas_b = [s2,s4,s6,s8]

s.toon_alle_leerlingen()

def voeg_leerling_toe():
    naam = input("geef naam")
    leeftijd = int(input("geef de leeftijd"))
    punt = int(input("geef het punt in"))
    leerling = Student(naam,leeftijd,punt)
    klas = input("a of b")
    if klas == "a":
        klas_a.append(leerling)
    else:
        klas_b.append(leerling)

def verwijder_leerling():
    naam = input("geef de naam van de leerling")
    for leerling, eigenschap in enumerate(klas_a):
            if eigenschap.naam == naam:
                del klas_a[leerling]
                break
    for leerling, o in enumerate(klas_b):
            if o.naam == naam:
                del klas_b[leerling]
                break

#voeg_leerling_toe()
s.toon_alle_leerlingen()
verwijder_leerling()
s.toon_alle_leerlingen()
