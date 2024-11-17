from pico2d import *
import game_framework
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Worker:
    def __init__(self,game_map):
        self.image = load_image('resource/character.png')
        self.arrow = load_image('resource/arrow.png')
        self.cooking_sprite = load_image('resource/food_sprite.png')
        self.kimbap = load_image('resource/kimbap.png')
        self.fry = load_image('resource/fry.png')
        self.soondae = load_image('resource/soondae.png')
        self.ttukbokki = load_image('resource/ttukbokki.png')
        self.ramen = load_image('resource/ramen.png')
        self.water = load_image('resource/water.png')
        self.gaze = load_image('resource/gaze_sprite.png')

        self.map = game_map
        self.plate = [0, 0, 0, 0]        
        self.x, self.y = 4,3
        self.dir = 0
        self.speed = 0.2

        self.frame_x = 0
        self.frame_y = 0
        self.frame_size = 64
        self.rotate = False
        self.arrow_active = False
        self.cook_step = [0, 0, 0, 0, 0]
        self.cook_type = 10

    def update(self):
        if self.dir == 1:  # 왼쪽으로 이동
            if self.frame_x > -1:
                self.frame_x -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
            else:
                self.frame_x = 0
                self.x -= 1
                self.dir = 0
        elif self.dir == 2:  # 오른쪽으로 이동
            if self.map.is_walkable(int(self.x + 1), int(self.y)):
                if self.frame_x < 1:
                    self.frame_x += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
                else:
                    self.frame_x = 0
                    self.x += 1
                    self.dir = 0
        elif self.dir == 3:  # 아래쪽으로 이동
            if self.map.is_walkable(int(self.x), int(self.y - 1)):
                if self.frame_y > -1:
                    self.frame_y -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
                else:
                    self.y -= 1
                    self.dir = 0
                    self.frame_y = 0
        elif self.dir == 4:  # 위쪽으로 이동
            if self.map.is_walkable(int(self.x), int(self.y + 1)):
                if self.frame_y < 1:
                    self.frame_y += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
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
       # 음식 게이지 그리기
        for i in range(5):
            
            self.gaze.clip_draw(self.cook_step[i] * 32,96 * (i % 2),32,96,737,461 - int((self.frame_size + 4.5) * i),20,self.frame_size + 4)

    def get_bb(self): 
        return 0, 0, 1600-1, 50