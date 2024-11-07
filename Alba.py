from pico2d import *
import game_world

class Ballon:
    global image
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
    def draw(self):
        image.clip_draw(self.frame * 96,2 * 160,96,160,50,self.y,40,50)

    def update(self):
        self.frame = (self.frame + 1) % 4

class Girl:
    global image
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
    def draw(self):
        image.clip_draw(self.frame * 96,1 * 160,96,160,50,self.y,40,50)
    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
            
class Chunsik:
    global image
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
    def draw(self):
        image.clip_draw(self.frame * 96,0 * 160,96,160,50,self.y,40,50)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
