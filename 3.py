def __init__(self, default_name, default_age):
    self.name = default_name
    self.age = default_age
    self.__money = 0
    self.__house = None

def info(self):
    print(f"Name: {self.name}\nAge: {self.age}\nMoney: {self.__money}\nHouse: {self.__house}")

@staticmethod
def default_info():
    print(f"Default Name: {Human.default_name}\nDefault Age: {Human.default_age}")

def earn_money(self, value):
    self.__money += value
    print(f"Earned {value} money! Current value: {self.__money}")

def buy_house(self, house, discount):
    final_price = house.final_price(discount)
    if self.__money < final_price:
        print("Not enough money!")
    else:
        self.make_deal(house, final_price)

def make_deal(self, house, price):
    self.__money -= price
    self.__house = house
