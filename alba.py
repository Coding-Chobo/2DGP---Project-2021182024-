from pico2d import *
import play_mode
import random
import game_framework

# Action Speed
TIME_PER_ACTION = 1.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class Ballon:
    def __init__(self):
        self.get_food = False
        self.x = 70
        self.y = 550
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Ballon.png')
        self.select = False
    
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y,84,140)

    def update(self):   
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4

class Girl:
    def __init__(self):
        self.get_food = False
        self.x = 70
        self.y = 650
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Girl.png')
        self.select = False
   
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y,84,140)
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        if self.select :
            self.y -= 10 * FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
        if self.y < 75:
            self. y = 630

class Chunsik:
    def __init__(self):
        self.get_food = False
        self.x = 70
        self.y = 650
        self.step = 0 
        #0은 배달 받기 전
        #1은 음식 대기 상태
        #2은 배달 중
        #3은 리젠 타임
        self.frame = 0
        self.framesize = 96
        self.image = load_image('resource/Chunsik.png')
        self.order_sprite = load_image('resource/Order_Food.png') 
        self.font = load_font('ENCR10B.TTF', 16)
        self.select = False

        self.order = {}
        self.delivery_time = 0
        self.regen_time = 20
    
    def draw(self):
        self.image.clip_draw(int(self.frame) * self.framesize,0,self.framesize,160,self.x,self.y,84,140)
        if self.step == 1: 
            second = 0
            for key, value in self.order.items():
                self.order_sprite.clip_draw((7-key)*64,0,64,64,self.x + 50,self.y - 25 + 50 * second,50,50)
                if value > 0:
                    self.font.draw(self.x + 60,self.y - 15 + 50 * second,f'{value}',(0,0,0))                
                second += 1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 4
        if self.select :
            #위에서 내려오기 시작
            if self.step == 0:
                if self.y > 300:
                    self.y -= 5 * FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
                else :
                    self.y = 300
                    self.step += 1
                    self.get_order()
            #음식받고 배달 시작
            if self.step == 2:
                if self.y > 70 :
                    self.y -= 5 * FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
                else : 
                    self.step = 3
                    self.y = 1000
            #밑으로 사라진 후 리젠 타임 계산
            if self.step == 3:
                self.delivery_time += FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time
                if self.delivery_time > self.regen_time :
                    self.step = 0
                    self.delivery_time = 0
                    self.y = 620

    def get_order(self):
        menu = random.sample(range(3, 8), 2)
        for item in menu:
            self.order[item] = 1
        print(self.order)
    
    def check_order(self,food):
        if food in self.order and self.order[food] > 0:
            self.order[food] -= 1
            play_mode.point.get_point(food)
            if all(value == 0 for value in self.order.values()):
                self.order = {}
                self.step += 1
            return True
                 



class Background:
    def __init__(self):
        self.image = load_image('resource/alba_select.png')
        pass
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,400)