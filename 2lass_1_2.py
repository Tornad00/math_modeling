states = ['отсутствуют', "цветение", "зелёный", "красный"]
index = 0
kol=5
spra = "Не занимайся этим, это ад!!!!!!"
class Tomato:
  def __init__(self):
    self.state = states[1]
  def grow (self):
    if self.state < len(states) - 1:
      self.state += 1 
  def is_ripe(self):
    if state == len(states) - 1:
      return True

      
class TomatoBush:
  def __init__ (self, tomatoes):
    self.tomato = []
    for i in kol:
      self.tomatos.append(Tomato())
  def grow_all(aelf):
    for tomato in self.tomatos:
      tomato.grow
  def all_are_ripe(self):
    for tomato in self.tomatos:
      if tomato.is_rape:
        continue
      else:
        break
      return True
  def give_away_all(self):
    



class Garden:
  def __init__ (self, name_0, plant):
    self.name = name_0
    salfe.plant = TomatoBush

  def work(self, ):
    u = TomatoBush()
    u.grow.all(slfe, states)

  def  harvest(self, ):
    s = TomatoBush()
    s.all_are_riple(self, )

  def knowledge_base(self, spra):
    print (spra)