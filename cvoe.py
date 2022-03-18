from Box2D.examples.framework import Framework
from Box2D import *

class Simulation(Framework):
    def __init__(self):
        super(Simulation, self).__init__()

        # Ground body
        self.world.CreateBody(shapes=b2LoopShape(vertices=[(20, 0), (20, 40), (-20, 40), (-20, 0)]))
        # Dynamic body
        circle = b2FixtureDef(shape=b2CircleShape(radius=2), density=1, friction=1.0, restitution=0.5)
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0,30), fixtures=circle, linearVelocity=(5, 0))

    def Step(self, settings):
        super(Simulation, self).Step(settings)

if __name__ == "__main__":
    Simulation().run()
##pip instal Box2D##