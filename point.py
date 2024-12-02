from pico2d import *
import pickle

class Point:
    def __init__(self):
        self.totalpoint = 0
        self.trash = 0
        self.clean_table = 0
        self.guest_totalamount = 0
        self.totalstatus = 0


        self.amount_sell= [ 0 for o in range(5)]
        self.font = load_font('resource/ENCR10B.TTF', 16)
    def draw(self):
        for i in range(5):
            self.font.draw(95 + 85 * i,800 - 105,f'{self.amount_sell[i]}')
        self.font.draw(95,800 - 55,f'{self.totalpoint}')
        self.font.draw(250,800 - 55,f'{self.guest_totalamount}')
        self.font.draw(350,800 - 55,f'{self.totalstatus}')

    def update(self):
        self.totalpoint = 2700 * (self.amount_sell[0] + self.amount_sell[2]) + 3200 * (self.amount_sell[1] + self.amount_sell[3] + self.amount_sell[4])

    def get_point(self,food):
        if food == 7: #튀김
            self.amount_sell[4] += 1
        elif food == 6: #떡볶이
            self.amount_sell[0] += 1
        elif food == 5: #김밥
            self.amount_sell[1] += 1
        elif food == 4: #순대
            self.amount_sell[2] += 1
        elif food == 3: #라면
            self.amount_sell[3] += 1
    def save_point(self):
        self.totalpoint += self.totalstatus * 1000
        self.totalpoint += self.clean_table * 2000
        self.totalpoint -= self.trash * 2000
        #기존 데이터를 불러오거나 새로 생성
        if os.path.exists('game.sav'):
            with open('game.sav', 'rb') as f:
                points = pickle.load(f)
        else:
            points = []  # 파일이 없으면 빈 리스트 생성
        
        # 새 점수를 추가하고 내림차순 정렬
        points.append(self.totalpoint)
        points.sort(reverse=True)  # 내림차순 정렬

        # 저장
        with open('game.sav', 'wb') as f:
            pickle.dump(points, f)

    def load_points(self):
        # 저장된 점수를 불러오기
        if os.path.exists('game.sav'):
            with open('game.sav', 'rb') as f:
                points = pickle.load(f)
                return points
        return []
    def save(self):
        with open('game.sav', 'wb') as f:
            pickle.dump(self.totalpoint, f)    
 
