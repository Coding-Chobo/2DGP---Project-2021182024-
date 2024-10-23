from pico2d import *
import random
# Game object class here
class Map:
    def __init__(self):
        self.image = load_image('resource/basic_map.png')
        self.menu_sprite = load_image('resource/menu_sprite.png')
        self.world_width = 800
        self.world_height = 800
        self.menu_size = 64
        self.menu_gap = 92
        self.menu_frame = 0
        self.data = [[1,1,1,1,1,1,0,9],
                     [1,2,0,2,0,2,0,8],
                     [1,1,0,1,0,1,0,7],
                     [0,0,0,0,0,0,0,6],
                     [0,0,0,0,0,0,0,5],
                     [1,1,0,1,0,1,0,4],
                     [1,2,0,2,0,2,0,3],
                     [1,1,1,1,1,1,1,1]
                     ]
        self.get_table_limit_time = 600
        self.get_table_time = 0

    def draw(self):
        self.image.clip_draw(0,0,self.world_width,self.world_height,self.world_width / 2,self.world_height / 2)
        for i in range(0,6):
            self.menu_sprite.clip_draw(i * self.menu_size,self.menu_frame * self.menu_size, #left, bottom
                                       self.menu_size,self.menu_size, #width,height - png안에서 너비
                                       self.world_width - self.menu_gap-8,(6-i) * (self.menu_size + 4) + 56,#x,y
                                       self.menu_gap,self.menu_gap)#width,height - 화면안에서 너비
    def update(self):
        self.menu_frame =(self.menu_frame + 1) % 2
        
        self.get_table_time += 1

        

class Worker:
    def __init__(self):
        self.x, self.y = 4,3
        self.dir = 0
        self.frame_x = 0
        self.frame_y = 0
        self.frame_size = 64
        self.speed = 0.2
        self.plate = [0, 0, 0, 0]
        self.image = load_image('resource/character.png')
        self.cooking_sprite = load_image('resource/food_sprite.png')
        self.kimbap = load_image('resource/kimbap.png')
        self.fry = load_image('resource/fry.png')
        self.soondae = load_image('resource/soondae.png')
        self.ttukbokki = load_image('resource/ttukbokki.png')
        self.ramen = load_image('resource/ramen.png')
        self.water = load_image('resource/water.png')
        
        self.cook_step = [0, 0, 0, 0, 0]
        self.cook_type = 0 

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

        if self.cook_type == 3:
            self.cook_step[0] += 1
            self.cook_type = 0
        elif self.cook_type == 4:
            self.cook_step[0] += 1
            self.cook_type = 0
        elif self.cook_type == 5:
            self.cook_step[0] += 1
            self.cook_type = 0
        elif self.cook_type == 6:
            self.cook_step[0] += 1
            self.cook_type = 0
        elif self.cook_type == 7:
            self.cook_step[0] += 1
            self.cook_type = 0
        elif self.cook_type == 8:
            self.cook_step[0] += 1
            self.cook_type = 0
    def draw(self):
        #플레이어 그리기
        self.image.draw((self.x + self.frame_x+2) * 75 ,(self.y + self.frame_y) * 67 + 75)
        #들고있는 메뉴그리기
        gap = 50
        for i in range(4):
            if i == 0 or i == 2:
                if i == 0:
                    xgap = -gap
                else:
                    xgap = gap
                ygap = 0
            elif i == 1 or i == 3:
                if i == 3:
                    ygap = -gap
                else:
                    ygap = gap                
                xgap = 0

            if self.plate[i] == 3: #라면
                self.ramen.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 4: #순대
                self.soondae.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 5:#김밥
                self.kimbap.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 6:#떡볶이
                self.ttukbokki.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 7:#튀김
                self.fry.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 8:#물
                self.water.draw((self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
        #만들어지는 메뉴 스프라이트 그리기
        for i in range(5):
            if self.cook_step[i] > 0:
                self.cooking_sprite.clip_draw(self.frame_size * (self.cook_step[i]- 1),i * self.frame_size
                                              ,self.frame_size,self.frame_size,
                                               665,(6-i) * (self.frame_size + 4) + 56)


class Table:
    def __init__(self):
        self.order = []
        self.step = 0
        self.waiting_time = 0
        self.is_active = False
        self.status = 2
        self.guest_amount = random.randint(1,3)    
        self.guest1 = Guest()
        self.guest2 = Guest()
        #self.table_image = load_image('table_sprite.png')

    def update(self):
        if self.is_active:
            self.waiting_time += 1
            if self.waiting_time == 150:
                self.status -= 1
                self.waiting_time = 0
    def draw(self):
        pass
class Guest:
    def __init__(self):
        self.type = random.randint(1,3)
        #self.guset1_image = load_image('guest01_sprite.png')   
        #self.guset2_image = load_image('guest02_sprite.png')        
        if self.type == 1:
            pass
            #self.image = self.guset1_image
        elif self.type == 2:
            #elf.image = self.guset2_image
            pass
    def update(self):
        pass

