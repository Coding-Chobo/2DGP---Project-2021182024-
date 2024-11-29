from pico2d import *
import game_framework
#플레이어 이동을 위한 프레임
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#플레이어 애니메이션을 위한 프레임
TIME_PER_ACTION_a = 1.5
ACTION_PER_TIME_a = 1.0 / TIME_PER_ACTION_a
FRAMES_PER_ACTION_a = 8

#플레이어 화살표를 위한 프레임
TIME_PER_ACTION_b = 1.5
ACTION_PER_TIME_b = 1.0 / TIME_PER_ACTION_b
FRAMES_PER_ACTION_b = 8

#음식제작하는 손을 그리기 위한 프레임
TIME_PER_ACTION_h = 0.3
ACTION_PER_TIME_h = 1.0 / TIME_PER_ACTION_h
FRAMES_PER_ACTION_h = 4


class Worker:
    def __init__(self,game_map):
        self.image = load_image('resource/PlayerSheet.png')
        self.arrow = load_image('resource/arrow.png')
        self.cooking_sprite = load_image('resource/food_sprite.png')
        self.kimbap = load_image('resource/kimbap.png')
        self.fry = load_image('resource/fry.png')
        self.soondae = load_image('resource/soondae.png')
        self.ttukbokki = load_image('resource/ttukbokki.png')
        self.ramen = load_image('resource/ramen.png')
        self.water = load_image('resource/water.png')
        self.gaze = load_image('resource/gaze_sprite.png')
        self.hand = load_image('resource/Hand-Sheet.png')
        self.map = game_map
        self.plate = [0, 0, 0, 0]        
        self.x, self.y = 4,3
        self.dir = 0
        self.speed = 0.2

        self.frame = 0
        self.frame_a = 0
        self.frame_b = 0
        self.frame_h = 0        
        self.frame_x = 0
        self.frame_y = 0
        self.frame_size = 64
        self.rotate = False
        self.arrow_active = False
        self.making = False
        self.making_time = 0
        self.cook_step = [0, 0, 0, 0, 0]
        self.cook_type = 10

        self.font = load_font('ENCR10B.TTF', 8)
    def update(self):
        if self.dir == 1:  # 왼쪽으로 이동
            if self.frame_x > -1:
                self.frame_x -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
            else:
                self.frame_x = 0
                self.x -= 1
                self.dir = 0
        elif self.dir == 2:  # 오른쪽으로 이동
            if self.frame_x < 1:
                self.frame_x += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
            else:
                self.frame_x = 0
                self.x += 1
                self.dir = 0
        elif self.dir == 3:  # 아래쪽으로 이동
            if self.frame_y > -1:
                self.frame_y -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
            else:
                self.y -= 1
                self.frame_y = 0
                self.dir = 0
        elif self.dir == 4:  # 위쪽으로 이동
            if self.frame_y < 1:
                self.frame_y += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * self.speed
            else:
                self.y += 1
                self.frame_y = 0
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
            print(f'{self.x}, {self.y}')
        #음식 만드는 손 애니메이션
        if self.making == True:
            self.frame_h = (self.frame_h + FRAMES_PER_ACTION_h*ACTION_PER_TIME_h*game_framework.frame_time) % 2 
            if self.making_time < FRAMES_PER_ACTION_h:
                self.making_time += FRAMES_PER_ACTION_h*ACTION_PER_TIME_h*game_framework.frame_time
            else:
                self.making_time = 0
                self.making = False
                self.frame_h = 0
    
        self.frame_a = (self.frame_a + FRAMES_PER_ACTION_a*ACTION_PER_TIME_a*game_framework.frame_time) % 3
        self.frame_b = (self.frame_b + FRAMES_PER_ACTION_b*ACTION_PER_TIME_b*game_framework.frame_time) % 2
    def draw(self):
        #플레이어 그리기
        self.image.clip_draw(int(self.frame_a) * 96,0,96,128,(self.x + self.frame_x+2) * 75 ,(self.y + self.frame_y) * 67 + 75)
        #만들어지는 메뉴 스프라이트 그리기
        for i in range(5):
            if self.cook_step[i] > 0:
                self.cooking_sprite.clip_draw(self.frame_size * (self.cook_step[i]- 1),i * self.frame_size
                                              ,self.frame_size,self.frame_size,
                                               661,(6-i) * (self.frame_size + 4) + 56)
        #들고있는 메뉴그리기
        gap = 45
        PI = 3.14159265358979
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
                #화살표 그리기
        if self.y == 6 or self.y == 1:
            self.arrow.clip_draw(int(self.frame_b) * 64, 0,64,64,(self.x + self.frame_x+2) * 75 - 30 ,(self.y + self.frame_y) * 67 + 55,48,48)
            self.arrow.clip_draw(int(self.frame_b) * 64,64,64,64,(self.x + self.frame_x+2) * 75 + 30 ,(self.y + self.frame_y) * 67 + 55,48,48)
        elif (self.x == 6):
            self.arrow.clip_draw(int(self.frame_b) * 64,64,64,64,(self.x + self.frame_x+2) * 75 + 30 ,(self.y + self.frame_y) * 67 + 55,48,48)
        elif (self.x == 0):
            self.arrow.clip_draw(int(self.frame_b) * 64, 0,64,64,(self.x + self.frame_x+2) * 75 - 30 ,(self.y + self.frame_y) * 67 + 55,48,48)
        #음식 만드는 손 그리기
        if self.making == True:
            self.hand.clip_draw(int(self.frame_h) * 64,0,64,64,(self.x + 2) * 75 + 15,(self.y) * 67 + 75)
        
        #좌표값을 구하기 위해 좌표값표시
        for i in range(40):
            for j in range(40):
                #self.font.draw(j * 20,i * 20,f'{j * 20}',(0 ,0 ,0))
                pass

    def get_bb(self): 
        return 0, 0, 1600-1, 50