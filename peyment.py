
class Payment:
    a=30
    def __init__(self,price):
        self.__price=price
        
    def __print_discount(self):
        print('Tabrik!! %d takhfif darid'%Payment.a)

    def set_price(self,discount):
        if discount=='gorban98':
            self.__price=self.__price - (self.__price*(Payment.a/100))
            self.__print_discount()

    def get_price(self):
        return self.__price

dvd=Payment(30)
print(dvd.get_price())
dvd.set_price('gorban98')
print(dvd.get_price())