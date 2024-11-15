from pico2d import *
import game_framework

# Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Ballon:
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Ballon.png')
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4

class Girl:
    def __init__(self):
        self.get_food = False
        self.x = 50
        self.y = 800
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Girl.png')
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y)
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        #self.y -= 5
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
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        #if self.get_food == False and self.y > 300:
        #    self.y -= 5
        #elif self.get_food == True and self.y <= 300:
        #    self.y -= 5
        if self.y < 25:
            self. y = 800

class Background:
    def __init__(self):
        self.image = load_image('resource/alba_select.png')
        pass
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,400)