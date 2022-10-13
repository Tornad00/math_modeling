import random
states = ['отсутствует', 'цветение', 'опыление', 'зеленый', 'красный']

TOMATO_RIPED = 0
TOMATO_READY = len(states)-1

class WrongTomatoState(Exception):
  pass


def get_state_str(state):
  if state > 0 and state <= TOMATO_READY:
    return states[state]
  else:
    raise WrongTomatoState

spra = 'садоводство это весело и прикольно, садишь томаты, балдеешь на свежем воздухе, сказка!!!'


class Tomato:
  start_index = 0
  def  __init__(self, gardener):
    self.index = Tomato.start_index
    self.state = 1
    self.gardener = gardener
    Tomato.start_index+=1
  def grow(self):
    print(self,' > ', end='')
    if self.state < TOMATO_READY:
      self.state += self.gardener.skill_gard()
    print(self)
  def is_ripe(self):
    return (self.state >= TOMATO_READY)
  def __str__(self):
    return f'{self.__class__.__name__}, idx:{self.index}, state:{self.state}'
      

class TomatoBush:
  def  __init__(self, tomatos_count: int, gardener):
    self.tomatos = []
    for _ in range(tomatos_count):
      self.tomatos.append(Tomato(gardener))
  def grow_all(self):
    for tomato in self.tomatos:
      tomato.grow()
  def all_are_ripe(self):
    for tomato in self.tomatos:
      if not tomato.is_ripe():
        return False
    return True
  def give_away_all(self):
    if self.all_are_ripe():
      self.tomatos.clear()
    

class Gardener:
  def  __init__(self, name: str, skill: int):
    self.name = name
    self.bush = None
    self.skill = skill 
  def work(self):
    self.bush.grow_all()
  def assign_bush(self, bush):
    self.bush = bush
  def harvest(self):
    if self.bush.all_are_ripe():
      self.bush.give_away_all()
      print('дело сделано')
  def knowledge_base(self):
    print(spra)
  def skill_gard(self):
    chance = 0
    if self.skill >= 0 and self.skill <= 30:
      chance = random.uniform(0, 0.3)
    elif self.skill >= 31 and self.skill >= 60:
      chance = random.uniform(0.3, 0.6)
    else:
     chance = random.uniform(0.6, 1)
    return chance 
    print(chance)
    

# -----------------------------------------
g = Gardener("Bob", random.randint(0, 100))
b = TomatoBush(random.randint(0, 30), g)
g.assign_bush(b)

iter = 0
print(b.all_are_ripe())

while not b.all_are_ripe():
  print(f'Iteration: {iter}')
  g.work()
  g.harvest()
  iter+=1
  print()


print('The end')