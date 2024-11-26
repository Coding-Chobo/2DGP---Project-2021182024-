from pico2d import *
import game_framework
import game_world
import random

from alba import Chunsik ,Ballon , Girl
from table import Table, Guest

# MenuSprite Speed
TIME_PER_ACTION_m = 1.0
ACTION_PER_TIME_m = 1.0 / TIME_PER_ACTION_m
FRAMES_PER_ACTION_m = 2

# Table Speed
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
            [1, (2,0), 0, (2,1), 0, (2,2), 0, 8],
            [1, 1, 0, 1, 0, 1, 0, 7],
            [10, 0, 0, 0, 0, 0, 0, 6],
            [10, 0, 0, 0, 0, 0, 0, 5],
            [1, 1, 0, 1, 0, 1, 0, 4],
            [1, (2,3), 0, (2,4), 0, (2,5), 0, 3],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        #테이블 세팅
        self.menu_gap = 76
        self.tables = [Table() for i in range(6)]
        for o in range(6):
            self.tables[o].x = (o % 3) * 2 + 1
            if o < 3:
                self.tables[o].y = 1
            else : 
                self.tables[o].y = 6
        self.get_table_limit_time = 150
        self.get_table_time = 0

        self.alba = Ballon()
        self.world_width = 800
        self.world_height = 800

    def update(self):
        self.menu_frame = (self.menu_frame + FRAMES_PER_ACTION_m * ACTION_PER_TIME_m * game_framework.frame_time) % 3
        tablelist = []  # 조건문 바깥에서 먼저 초기화
        if self.alba.select :
         # 일정 시간마다 빈 테이블을 찾아서 손님 넣기
            if self.get_table_time < self.get_table_limit_time:
                    self.get_table_time = (self.get_table_time + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            else:  # 일정 시간이 넘어가면 빈 테이블을 찾아 정보 초기화
                self.get_table_time = 0 
                for b in range(6):
                    if not self.tables[b].is_active:
                        tablelist.append(b)
                # 빈 테이블이 있을 때만 선택
                if tablelist:
                    #빈테이블 중 랜덤 테이블 정하기
                    i = random.choice(tablelist)
                    t =  self.tables[i]
                    tablelist.clear()
                    t.is_active = True
                    #게스트 수 정하기
                    c = random.randint(1, 2)
                    t.guest_amount = c 
                    for _ in range(c):
                        t.guest[_] = Guest()
                        #t.guest[_].
                    print(f'table_number = {i}')
                    print(f'amount = {t.guest_amount}')
                else:
                    print("모든 테이블이 활성 상태입니다.")
            for o in range(6):
                self.tables[o].update()
                


    def is_walkable(self,cell):
        if isinstance(cell, int):
            return cell == 0 or cell == 10  # 숫자 0일 경우만 이동 가능
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
                                       self.world_width - 100,(6-i) * (self.menu_size + 3) + 55,#x,y
                                       self.menu_gap,self.menu_gap)#width,height - 화면안에서 너비
        for i in range(6):
            if self.tables[i].is_active :
               self.tables[i].draw()
        

