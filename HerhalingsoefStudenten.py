class Student:

    def __init__(self,naam,leeftijd,punt):
        self.naam = naam
        self.leeftijd = leeftijd
        self.punt = punt

    def __str__(self):
        return "Student: {} is {} jaar en heeft {} % ".format(self.naam,self.leeftijd,self.punt)

    def toon_student_info(self):
        print(self.__str__())

s = Student("Bert",22,85)
s2 = Student("Cindy",21,82)
s3 = Student("Dennis",24,75)
s4 = Student("Erika",20,68)
s5 = Student("Alex",21,76)
s6 = Student("Zoe",19,91)
s7 = Student("Guido",18,49)
s8 = Student("Lindsay",22,68)

klas_a = [s,s3,s5,s7]
klas_b = [s2,s4,s6,s8]
