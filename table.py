from pico2d import *
import game_framework
import game_world
import random

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

TIME_PER_ACTIONG = 1.5
ACTION_PER_TIMEG = 1.0 / TIME_PER_ACTIONG
FRAMES_PER_ACTIONG = 8

class Table:
    def __init__(self):
        self.image = load_image('resource/table_sprite.png')
        self.x = 0
        self.y = 0
        self.order = {8:1}
        self.step = 0
        self.clean_status = 0
        self.waiting_time = 0
        self.is_active = False
        self.status = 2
        self.guest_amount = 0
        self.guest_frame_size = 128
        self.guest = [None,None]
        
    def update(self):
        if self.is_active:
            for o in self.guest :
                if type(o) == Guest:
                    o.update()
            #test를 위해서 0을 곱함
            self.waiting_time += 0 * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            if self.waiting_time > 200: 
                if self.status == 0:
                    self.reset_status()
                else:     
                    self.status -= 1
                    self.waiting_time = 0
    def draw(self):
        if self.step == 2:
            self.image.clip_draw((3- self. clean_status) * 200,0
                                 ,200,120
                                 ,210 + 154 * (self.x // 2),63 + 67 * (7 - self.y)
                                 ,90,60)
        if self.is_active : 
            a = 0
            for o in self.guest :
                if type(o) == Guest:
                    o.image.clip_draw(self.status * self.guest_frame_size,a * 2 * self.guest_frame_size + int(o.frame) * self.guest_frame_size,
                                     self.guest_frame_size,self.guest_frame_size,
                                     213 + 152 * (self.x // 2),63 + 67 * (7 - self.y) + 46 - 106 * a,
                                     120,120)                                      
                    a += 1

    def reset_status(self):
        self.order = {8:1}
        self.step = 0
        self.waiting_time = 0
        self.is_active = False
        self.status = 2
        self.guest_amount = 0
        self.guest = [None,None]
        self.clean_status = 0

    def get_order(self):
        self.order = {}
        print(self.order)
        for a in range(self.guest_amount):
            self.order[random.randint(0, 4) + 3] = self.guest[a].type
        print(self.order)
    def check_order(self,food):
        if self.step == 2 and self.clean_status > 0:
            self.clean_status -=1
            if self.clean_status <= 0:
                self.reset_status()
        elif food in self.order and self.order[food] > 0:
            self.order[food] -= 1
            self.is_finish()
            return True

    def is_finish(self):
            if all(value == 0 for value in self.order.values()):
                if self.step == 0:
                    self.get_order()
                    self.waiting_time = 0
                    self.status += 1
                    self.step = 1
                    print("물을 받았습니다.")
                elif self.step == 1:
                    self.clean_status = 3
                    self.waiting_time = 0
                    self.status += 1 
                    self.step = 2
                    print("주문을 전부 받았습니다.")

class Guest:
    def __init__(self):
        self.type = random.randint(1, 2)
        self.guset1_image = load_image('resource/guest1_sprite.png')   
        self.guset2_image = load_image('resource/guest2_sprite.png')      
        if self.type == 1:
            self.image = self.guset1_image
        elif self.type == 2:
            self.image = self.guset2_image

        self.frame_size = 128
        self.frame = 0  
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTIONG*ACTION_PER_TIMEG*game_framework.frame_time) % 2
    def draw(self):
        pass