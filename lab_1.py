

class Human:
  def __init__ (self, name, age, money, appart):
    self.default_name = name
    self.default_age = age
    self._security_money = money
    self._security_appaert = appart

  def info(self):
    print (self.default_name, self.default_age, self._security_money, self._security_appaert)
    return

  def make_deal(self):
    self._security_money = self._security_money - 6000000
    self._security_appaert += 1
    m.info()

  def earn_money(self):
    self._security_money = self._security_money + 80000
    m.buy_house()
    return self._security_money

  def buy_house(self):
    if self._security_money >=  6000000: #House.final_price()##:
      m.make_deal()
      print("сделке быть")

    else:
      m.earn_money()
      print("ты слишко беден")


class House:
  def __init__ (self, area, price):
    self._area = area
    self._price = price

  def final_price (self, price):
    self._price = self.price * 0.7
    return self._price

class SmallHouse(House):
  def __init__ (self, area, price):
    super().__init__(area, price)

m = Human("BOB", 21, 0, 0)
h = SmallHouse(40, 100000)
m.earn_money()


