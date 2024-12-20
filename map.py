from pico2d import *
import game_framework
import game_world
import random
import play_mode
import final_mode
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
        self.bgm = load_music('resource/background_music.mp3')
        self.font = load_font('resource/Bold.TTF', 16)
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
        self.menu_size = 64
        self.menu_frame = 0
        self.time_m = 0
        self.time_h = 12
        self.limit_hour = 16
        self.end = False

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
        self.percent = 70
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
            elif self.time_h < self.limit_hour:  # 일정 시간이 넘어가면 빈 테이블을 찾아 정보 초기화
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
                    play_mode.point.guest_totalamount += c
                    t.guest_amount = c 
                    for _ in range(c):
                        t.guest[_] = Guest()
            for o in range(6):
                self.tables[o].update()
            #게임월드 시간 측정
            if self.time_h < self.limit_hour:
                self.time_m += game_framework.frame_time
            if self.time_m >= 60:
                self.time_h += 1
                self.time_m = 0
            if self.time_h >= self.limit_hour and all(not o.is_active for o in self.tables):
                if not self.end:
                    play_mode.point.save_point()
                    game_framework.push_mode(final_mode)
                
                


    def is_walkable(self,cell):
        if isinstance(cell, int):
            return cell == 0 or cell == 10  # 숫자 0일 경우만 이동 가능
        return False

    def set_alba(self, alba):
        if alba == 'ChunSik':
            self.alba = Chunsik()
        elif alba == 'Ballon':
            self.get_table_limit_time = 130
            self.alba = Ballon()
        elif alba == 'Girl':
            self.percent = 55
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
        self.font.draw(640,560,f'{self.time_h}       {int(self.time_m)}',(255,255,255))
        for i in range(6):
            if self.tables[i].is_active :
               self.tables[i].draw()
        

