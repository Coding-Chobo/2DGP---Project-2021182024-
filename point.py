from pico2d import *


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
        self.totalpoint += self.clean_table * 2000
        self.totalpoint -= self.trash * 2000


    def get_point(self,food):
        if food == 7:
            self.amount_sell[4] += 1
        elif food == 6:
            self.amount_sell[0] += 1
        elif food == 5:
            self.amount_sell[1] += 1
        elif food == 4:
            self.amount_sell[2] += 1
        elif food == 3:
            self.amount_sell[3] += 1