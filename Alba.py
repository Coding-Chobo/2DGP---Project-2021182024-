from pico2d import *
import game_world

class Ballon:
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Ballon.png')
    def draw(self):
        self.image.clip_draw(self.frame * self.framesize,0,self.framesize,160,50,self.y,40,50)

    def update(self):
        self.frame = (self.frame + 1) % 4

class Girl:
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Girl.png')
    def draw(self):
        self.image.clip_draw(self.frame * self.framesize,0,self.framesize,160,50,self.y,40,50)
    
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.y -= 5
        if self.y < 25:
            self. y = 800

class Chunsik:
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Chunsik.png')
    def draw(self):
        self.image.clip_draw(self.frame * self.framesize,0,self.framesize,160,50,self.y,40,50)

    def update(self):
        if self.get_food == False and self.y > 400:
            self.y -= 5
        elif self.get_food == True and self.y <= 400:
            self.y -= 5
        if self.y < 25:
            self. y = 800
