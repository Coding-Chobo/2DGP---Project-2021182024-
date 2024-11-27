from pico2d import *
import game_framework
import play_mode
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
        self.cloud = load_image('resource/Cloud.png')
        self.order_sprite = load_image('resource/Order_Food.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.x = 0
        self.y = 0
        self.order = {8:1}
        self.step = 0
        self.clean_status = 0
        self.eating_time = 0
        self.waiting_time = 0
        self.waiting_limit = 200
        self.is_active = False
        self.status = 2
        self.frame = 0
        self.guest_amount = 0
        self.guest_frame_size = 128
        self.guest = [None,None]
        self.percent = 70
    def update(self):
        if self.is_active:
            if self.step == 2:
                self.frame = (self.frame + FRAMES_PER_ACTIONG*ACTION_PER_TIMEG*game_framework.frame_time) % 2
                if self.eating_time < 60:
                    self.eating_time += (FRAMES_PER_ACTIONG*ACTION_PER_TIMEG*game_framework.frame_time)
                else :
                    self.eating_time = 0
                    self.frame = 0
                    self. step = 3
            #테이블의 대기시간에 따른 상태변화
            elif self.step < 2:
                self.waiting_time += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
                if self.waiting_time > self.waiting_limit: 
                    if self.status == 0:
                        self.reset_status()
                    else:     
                        self.status -= 1
                        self.waiting_time = 0
            #게스트 업데이트
            for o in self.guest :
                if type(o) == Guest:
                    o.update()            
    def draw(self):
        #테이블 쓰레기 스프라이트 그리기
        if self.step == 3:
            self.image.clip_draw((3- self. clean_status) * 200,0
                                 ,200,120
                                 ,210 + 154 * (self.x // 2),63 + 67 * (7 - self.y)
                                 ,90,60)
        #게스트 그리기
        if self.is_active : 
            if self.step <= 2:
                if self.step > 0:
                    second = 0
                    for key, value in self.order.items():
                        self.order_sprite.clip_draw((7-key)*64,0,64,64,212 + 154 * (self.x // 2) -20 + second * 45,63 + 67 * (7 - self.y),50,50)
                        if value > 0:
                            self.font.draw(212 + 154 * (self.x // 2) -10 + second * 45,75 + 67 * (7 - self.y),f'{value}',(0,0,0))                
                        second += 1
                a = 0
                for o in self.guest :
                    if type(o) == Guest:
                        o.image.clip_draw(self.status * self.guest_frame_size,a * 2 * self.guest_frame_size + int(o.frame) * self.guest_frame_size,
                                         self.guest_frame_size,self.guest_frame_size,
                                         214 + 152 * (self.x // 2),63 + 67 * (7 - self.y) + 46 - 106 * a,
                                         120,120)                                      
                        a += 1
        #먹을때 구름 그리기
        if self.step == 2:
            self.cloud.clip_draw(int(self.frame) * 200,0
                                 ,200,120
                                 ,210 + 154 * (self.x // 2),63 + 67 * (7 - self.y)
                                 ,150,120)

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
        available_menus = list(range(3, 8))

        # 손님 수가 메뉴 수보다 적을 경우, 손님 수만큼 고르고 아니면 메뉴 전체를 다 고른다
        if self.guest_amount <= len(available_menus):
            selected_menus = random.sample(available_menus, self.guest_amount)
        else:
            raise ValueError("손님 수가 메뉴 수보다 많아서 메뉴를 중복 없이 고를 수 없습니다.")

        # 메뉴를 손님과 매칭
        for a in range(self.guest_amount):
            self.order[selected_menus[a]] = self.guest[a].type
            print(self.order)

    def check_order(self,food):
        if self.step == 3 and self.clean_status > 0:
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
        percent = random.randint(0,100)       
        if percent < play_mode.map.percent:
            self.type = 1
        else :
            self.type = 2
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