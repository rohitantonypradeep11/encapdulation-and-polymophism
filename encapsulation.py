class computer:
    def __init__(self):
        self.__maxprize = 900
    def sell(self):
        print(self.__maxprize)
    def setprize(self,prize):
        self.__maxprize = prize
c = computer()
c.sell()
c.__maxprize = 1050
c.sell()
c.setprize(1000)
c.sell()