from pico2d import *
import game_framework
import game_world
import random

from alba import Chunsik ,Ballon , Girl

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Map:
    def __init__(self):
        self.image = load_image('resource/map.png')
        self.menu_sprite = load_image('resource/menu_sprite.png')
        self.menu_size = 64
        self.menu_frame = 0
        self.data = [
            [1, 1, 1, 1, 1, 1, 0, 9],
            [1, (2, 0), 0, (2,1), 0, (2,2), 0, 8],
            [1, 1, 0, 1, 0, 1, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 5],
            [1, 1, 0, 1, 0, 1, 0, 4],
            [1, (2,3), 0, (2,4), 0, (2,5), 0, 3],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        #테이블 세팅
        self.menu_gap = 92
        self.tables = [Table() for i in range(6)]
        for o in range(6):
            self.tables[o].x = (o % 3) * 2 + 1
            if o < 3:
                self.tables[o].y = 1
            else : 
                self.tables[o].y = 6
            print("x :",self.tables[o].x,", y :",self.tables[o].y)
        self.get_table_limit_time = 100
        self.get_table_time = 0

        self.alba = Ballon()

        self.world_width = 800
        self.world_height = 800
    def update(self):
        self.menu_frame = (self.menu_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        tablelist = []  # 조건문 바깥에서 먼저 초기화
        if self.alba.select :
         # 일정 시간마다 빈 테이블을 찾아서 손님 넣기
            if self.get_table_time < self.get_table_limit_time:
                    self.get_table_time = (self.get_table_time + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            else:  # 일정 시간이 넘어가면 빈 테이블을 찾아 정보 초기화
                for b in range(6):
                    if not self.tables[b].is_active:
                        tablelist.append(b)
                # 빈 테이블이 있을 때만 선택
                if tablelist:
                    i = random.choice(tablelist)
                    print(i)
                    tablelist.clear()
                    c = random.randint(1, 2)
                    self.tables[i].is_active = True
                    self.tables[i].guest_amount = c
                    order = 0
                    for a in range(c):
                        b = random.randint(1, 2)
                        order += b
                else:
                    print("모든 테이블이 활성 상태입니다.")
                self.get_table_time = 0 
    
    def is_walkable(self,x,y):
        if 0 <= y < len(self.data) and 0 <= x < len(self.data[y]):
            cell = self.data[y][x]
            if isinstance(cell, int):
                return cell == 0  # 숫자 0일 경우만 이동 가능
            elif isinstance(cell, tuple):
                return cell[0] == 0  # 튜플의 첫 번째 요소가 0일 경우만 이동 가능
        return False

    def set_alba(self, alba):
        if alba == 'ChunSik':
            self.alba = Chunsik()
        elif alba == 'Ballon':
            self.alba = Ballon()
        elif alba == 'Girl':
            self.alba = Girl()
        self.alba.select = True
        game_world.add_object(self.alba,1)
    
    def draw(self):
        self.image.clip_draw(0,0,self.world_width,self.world_height,self.world_width / 2,self.world_height / 2)
        for i in range(0,6):
            self.menu_sprite.clip_draw(i * self.menu_size,int(self.menu_frame) * self.menu_size, #left, bottom
                                       self.menu_size,self.menu_size, #width,height - png안에서 너비
                                       self.world_width - self.menu_gap-8,(6-i) * (self.menu_size + 4) + 56,#x,y
                                       self.menu_gap,self.menu_gap)#width,height - 화면안에서 너비
        for i in range(6):
            self.tables[i].draw()

class Table:
    def __init__(self):
        self.image = load_image('resource/table_sprite.png')
        self.x = 0
        self.y = 0
        self.order = {}
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
            self.waiting_time += 1
            if self.waiting_time == 150:
                if self.status == 0:
                    self.reset_status()
                    
                self.status -= 1
                print(self.status)
                self.waiting_time = 0
    def draw(self):
        if self.clean_status != 0:
            self.image.clip_draw((3- self.clean_status) * 200,0,200,120,self.x,self.y)
        if self.is_active : 
            for o in self.guest :
                pass
                #o.image.clipdraw()
                #(self.status * self.guest_frame_size,o * 2 * self.guest_frame_size,self.guest_frame_size,self.guest_frame_size)

    def reset_status(self):
        self.order = {}
        self.step = 0
        self.waiting_time = 0
        self.is_active = False
        self.status = 2
        self.guest_amount = 0
        self.guest = [None,None]

class Guest:
    def __init__(self,type = 1):
        self.type = type
        self.guset1_image = load_image('resource/guest1_sprite.png')   
        self.guset2_image = load_image('resource/guest2_sprite.png')      
        if self.type == 1:
            self.image = self.guset1_image
        elif self.type == 2:
            self.image = self.guset2_image

        self.frame_size = 128
        self.frame = 0  
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 2
    def draw(self):
        pass