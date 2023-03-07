class a:

    def __init__(self):
        self.waarde = "dit is klasse a"
    def toon_info(self):
        print(self.waarde)

class b:

    def __init__(self):
        self.waarde = "dit is klasse b"
    def voeg_a_toe(self,a):
        self.a = a
    def toon_info(self):
        print(self.waarde)
        print(self.a.toon_info())

vb_a = a()
vb_b = b()
vb_b.voeg_a_toe(vb_a)
vb_a.toon_info()
vb_b.toon_info()
