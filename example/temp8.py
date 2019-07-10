class PayGildong :
    def __init__(self) :
        self.day = 25
        self.__money = 1000000

    def changeMoney(self, money) :
        self.__money = money

    def getMoney(self) :
        return self.__money

gildong = PayGildong()
print(gildong.day)

#print(gildong.__money)

print(gildong.getMoney())

gildong.changeMoney(1100000)

print(gildong.getMoney())
