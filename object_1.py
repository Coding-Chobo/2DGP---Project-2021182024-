from pico2d import *
import random
# Game object class here
class Map:
    def __init__(self):
        self.image = load_image('basic_map.png')
        self.data = [[1,2,0,2,0,2,0,3],
                     [1,1,0,1,0,1,0,3],
                     [0,0,0,0,0,0,0,3],
                     [0,0,0,0,0,0,0,3],
                     [1,1,0,1,0,1,0,3],
                     [1,2,0,2,0,2,0,3],
                     [1,1,1,1,1,1,1,4]]

    def draw(self):
        self.image.draw(400,717/2)

    def update(self):
        pass



class Worker:
    def __init__(self):
        self.x, self.y = 4,4
        self.image = load_image('character.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw((self.x) * 100 + 50,(self.y) * 100)
