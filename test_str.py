class Ding:

    def __init__(self):
        self.info = "Dit is een ding"
    def __str__(self):
        return(self.info)
    def print_info(self):
        print(self.__str__())

ding = Ding()
print(ding)
ding.print_info()

