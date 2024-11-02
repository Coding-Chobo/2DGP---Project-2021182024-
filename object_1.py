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
        self.tables = [Table() for i in range(6)] 
        self.data = [
            [1, 1, 1, 1, 1, 1, 0, 9],
            [1, (2, 0), 0, (2,1), 0, (2,2), 0, 8],
            [1, 1, 0, 1, 0, 1, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 5],
            [1, 1, 0, 1, 0, 1, 0, 4],
            [1, (2,3), 0, (2,4), 0, (2,5, ), 0, 3],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.get_table_limit_time = 600
        self.get_table_time = 0
        
    def is_walkable(self,x,y):
        if 0 <= y < len(self.data) and 0 <= x < len(self.data[y]):
            cell = self.data[y][x]
            if isinstance(cell, int):
                return cell == 0  # 숫자 0일 경우만 이동 가능
            elif isinstance(cell, tuple):
                return cell[0] == 0  # 튜플의 첫 번째 요소가 0일 경우만 이동 가능
        return False


    def draw(self):
        self.image.clip_draw(0,0,self.world_width,self.world_height,self.world_width / 2,self.world_height / 2)
        for i in range(0,6):
            self.menu_sprite.clip_draw(i * self.menu_size,self.menu_frame * self.menu_size, #left, bottom
                                       self.menu_size,self.menu_size, #width,height - png안에서 너비
                                       self.world_width - self.menu_gap-8,(6-i) * (self.menu_size + 4) + 56,#x,y
                                       self.menu_gap,self.menu_gap)#width,height - 화면안에서 너비
    def update(self):
        self.menu_frame =(self.menu_frame + 1) % 2
        if self.get_table_time < self.get_table_limit_time :
            self.get_table_time += 1
        else: #일정 시간넘어가면 빈테이블을 찾아 정보 초기화
            list = []
            for b in range(6):
                if self.tables[b].is_active == False:
                    list.append(b)
            
            i = random.choice(list)
            list.clear()
            c = random.randint(1,2)
            self.tables[i].is_active = True
            self.tables[i].guest_amount = c
            order = 0
            for a in range(c):
                b = random.randint(1,2)
                order += b #삭제고려대상
                self.tables[i].guest[a] = Guest(b)
            
            #for n in range(order):
            #   self.tables.order = {}
            #생성 타이머 초기화
            self.get_table_time=0

        

class Worker:
    def __init__(self,game_map):
        self.x, self.y = 4,3
        self.dir = 0
        self.speed = 0.2

        self.frame_x = 0
        self.frame_y = 0
        self.frame_size = 64
        self.map = game_map
        self.rotate = False
        self.arrow_active = True
        self.arrow = load_image('resource/arrow.png')
        
        self.plate = [0, 0, 0, 0]
        self.image = load_image('resource/character.png')
        
        self.cooking_sprite = load_image('resource/food_sprite.png')
        self.kimbap = load_image('resource/kimbap.png')
        self.fry = load_image('resource/fry.png')
        self.soondae = load_image('resource/soondae.png')
        self.ttukbokki = load_image('resource/ttukbokki.png')
        self.ramen = load_image('resource/ramen.png')
        self.water = load_image('resource/water.png')
        self.gaze = load_image('gaze_sprite.png')
        self.alba = load_image('ALBA_sprite.pnt')
        self.cook_step = [0, 0, 0, 0, 0]
        self.cook_type = 10

        self.Alba.image
    def update(self):
        if self.dir == 1:  # 왼쪽으로 이동
            if self.frame_x > -1:
                self.frame_x -= self.speed
            else:
                self.frame_x = 0
                self.x -= 1
                self.dir = 0
        elif self.dir == 2:  # 오른쪽으로 이동
            if self.map.is_walkable(int(self.x + 1), int(self.y)):
                if self.frame_x < 1:
                    self.frame_x += self.speed
                else:
                    self.frame_x = 0
                    self.x += 1
                    self.dir = 0
        elif self.dir == 3:  # 아래쪽으로 이동
            if self.map.is_walkable(int(self.x), int(self.y - 1)):
                if self.frame_y > -1:
                    self.frame_y -= self.speed
                else:
                    self.y -= 1
                    self.dir = 0
                    self.frame_y = 0
        elif self.dir == 4:  # 위쪽으로 이동
            if self.map.is_walkable(int(self.x), int(self.y + 1)):
                if self.frame_y < 1:
                    self.frame_y += self.speed
                else:
                    self.frame_y = 0
                    self.y += 1
                    self.dir = 0
        #음식 만들기 단계
        if self.cook_type >= 0 and self.cook_type < 5:
            if self.cook_type % 2 == 0:
                if self.cook_step[self.cook_type] < 5:
                    self.cook_step[self.cook_type] += 1
                else:
                    for i in range(4):
                        if self.plate[i] == 0:
                            self.plate[i] = self.cook_type + 3
                            self.cook_step[self.cook_type] = 0
                            break
            else : 
                if self.cook_step[self.cook_type] < 4:
                    self.cook_step[self.cook_type] += 1
                else:
                   for i in range(4): 
                        if self.plate[i] == 0:
                            self.plate[i] = self.cook_type + 3
                            self.cook_step[self.cook_type] = 0
                            break
            self.cook_type = 10
        elif self.cook_type == 5 :
            for i in range(4): 
                if self.plate[i] == 0:
                    self.plate[i] = 8
                    break
            self.cook_type = 10
        #들고있는 접시 돌리기
        if self.rotate == True : 
            temp = self.plate[3]
            for i in range(3,0,-1):
                self.plate[i] = self.plate[i - 1]
            self.plate[0] = temp
            self.rotate = False
    def draw(self):
        #플레이어 그리기
        self.image.draw((self.x + self.frame_x+2) * 75 ,(self.y + self.frame_y) * 67 + 75)
        #만들어지는 메뉴 스프라이트 그리기
        for i in range(5):
            if self.cook_step[i] > 0:
                self.cooking_sprite.clip_draw(self.frame_size * (self.cook_step[i]- 1),i * self.frame_size
                                              ,self.frame_size,self.frame_size,
                                               661,(6-i) * (self.frame_size + 4) + 56)
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
            PI = 3.14159265358979
            if self.plate[i] == 3: #라면
                self.ramen.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 4: #순대
                self.soondae.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 5:#김밥
                self.kimbap.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 6:#떡볶이
                self.ttukbokki.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 7:#튀김
                self.fry.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
            elif self.plate[i] == 8:#물
                self.water.clip_composite_draw(0,0,self.frame_size,self.frame_size,PI/2 * (i + 2),'',(self.x + self.frame_x+2) * 75 + xgap, (self.y + self.frame_y) * 67 + 75 + ygap)
       # 음식그리기
        for i in range(5):
            self.gaze.clip_draw(self.cook_step[i] * 32,0,32,96,700,400,20,100)


class Table:
    def __init__(self):
        self.order = {}
        self.step = 0
        self.waiting_time = 0
        self.is_active = False
        self.status = 2
        self.guest_amount = 0
        self.guest = [None,None]
        self.table_image = load_image('resource/table_sprite.png')

    def update(self):
        if self.is_active:
            self.waiting_time += 1
            if self.waiting_time == 150:
                self.status -= 1
                print(self.status)
                self.waiting_time = 0
    def draw(self):
        pass


class Guest:
    def __init__(self,type):
        self.type = type
        #self.guset1_image = load_image('guest01_sprite.png')   
        #self.guset2_image = load_image('guest02_sprite.png')        
        if self.type == 1:
            pass
            #self.image = self.guset1_image
        elif self.type == 2:
            #self.image = self.guset2_image
            pass
    def update(self):
        pass

class Point:
    def __init__(self):
        self.trashcnt = 0
        self.s_food = [0,0,0,0,0]
        self.tip = 0
        self.total_point = 0

class Alba:
    def __init__(self):
        self.image = load_image('ALBA_sprite.png')
        

        pass