class Ball:
  '''
  документация
  '''
  pass

ball_1 = Ball ()
ball_2 = Ball ()

class Point:
  def __init__(self,x_0,y_0):
    self.x = x_0
    self.y = y_0  

  def __str__(self):
    return f'Point : {self.x}, {self.y}'
    
  def move (self, dx, dy):
    self.x += dx
    self.y += dy

p = Point(2,5)

print(p)

p.move(5, -8)


print(p)

