from pico2d import *
import random
# Game object class here
class Map:
    def __init__(self):
        self.image = load_image('basic_map.png')
        self.menu_sprite = load_image('menu_sprite.png')
        self.world_width = 800
        self.world_height = 800
        self.menu_size = 64
        self.menu_gap = 92
        self.frame = [0,0,0,0,0,0]
        self.data = [[1,1,1,1,1,1,0,4],
                     [1,2,0,2,0,2,0,3],
                     [1,1,0,1,0,1,0,3],
                     [0,0,0,0,0,0,0,3],
                     [0,0,0,0,0,0,0,3],
                     [1,1,0,1,0,1,0,3],
                     [1,2,0,2,0,2,0,3],
                     [1,1,1,1,1,1,1,1]
                     ]

    def draw(self):
        self.image.clip_draw(0,0,self.world_width,self.world_height,self.world_width / 2,self.world_height / 2)
        for i in range(0,6):
            self.menu_sprite.clip_draw(i * self.menu_size,self.frame[i] * self.menu_size, #left, bottom
                                       self.menu_size,self.menu_size, #width,height - png안에서 너비
                                       self.world_width - self.menu_gap-8,(7 - i) * (self.menu_size + 2.5) - 6,#x,y
                                       self.menu_gap,self.menu_gap)#width,height - 화면안에서 너비
    def update(self):
        pass

class Worker:
    def __init__(self):
        self.x, self.y = 4,3
        self.dir = 0
        self.frame_x = 0
        self.frame_y = 0
        self.image = load_image('character.png')
        self.speed = 0.2
        self.plate = [0, 0, 0, 0]
        self.kimbap = load_image('kimbab.png')
        self.fry = load_image('fry.png')
        self.soondae = load_image('soondae.png')
        self.ttukbokki = load_image('ttukbokki.png')
        self.ramen = load_image('ramen.png')
        self.water = load_image('water.png')
        
        
    def update(self):
        if self.dir == 1: # 왼쪽으로
            if self.frame_x > -1:
                self.frame_x -= self.speed
            else :
                self.frame_x = 0
                self.x -= 1
                self.dir = 0
        elif self.dir == 2: # 오른쪽으로
            if self.frame_x < 1:
                self.frame_x += self.speed
            else :
                self.frame_x = 0
                self.x += 1
                self.dir = 0
        elif self.dir == 3: # 아래쪽으로
            if self.frame_y > -1:
                self.frame_y -= self.speed
            else :
                self.y -= 1
                self.dir = 0
                self.frame_y = 0
        elif self.dir == 4: # 위쪽으로
            if self.frame_y < 1:
                self.frame_y += self.speed
            else :
                self.frame_y = 0
                self.y += 1
                self.dir = 0

    def draw(self):
        #플레이어 그리기
        self.image.draw((self.x + self.frame_x+2) * 75 ,(self.y + self.frame_y) * 67 + 75)
        #들고있는 메뉴그리기
        for i in range(0,4):
            if i == 0 or i == 2:
                if i == 0:
                    xgap = -30
                else:
                    xgap = 30
                ygap = 0
            elif i == 1 or i == 3:
                if i == 3:
                    ygap = -30
                else:
                    ygap = 30                
                xgap = 0

            if self.plate[i] == 1: #떡볶이
                self.ttukbokki.draw(self.x + xgap, self.y + ygap)
            elif self.plate[i] == 2: #순대
                self.soondae.draw(self.x + xgap, self.y + ygap)
            elif self.plate[i] == 3:#김밥
                self.kimbap.draw(self.x + xgap, self.y + ygap)
            elif self.plate[i] == 4:#라면
                self.ramen.draw(self.x + xgap, self.y + ygap)
            elif self.plate[i] == 5:#후라이
                self.fry.draw(self.x + xgap, self.y + ygap)
            elif self.plate[i] == 6:#물
                self.ttukbokki.draw(self.x + xgap, self.y + ygap)            

class Table:
    def __init__(self):
        self.table = load_image('table_sprite.png')
        self.guset1 = load_image('guest01_sprite.png')
        self.guset2 = load_image('guest02_sprite.png')
    