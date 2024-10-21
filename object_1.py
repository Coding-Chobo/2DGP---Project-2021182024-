import sys
sys.path.append(r"C:\Users\dbdal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from pico2d import *
import random
# Game object class here
class Map:
    def __init__(self):
        self.image = load_image('basic_map.png')
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
        self.image.clip_draw(0,0,800,800,400,400)

    def update(self):
        pass



class Worker:
    def __init__(self):
        self.x, self.y = 4,3
        self.image = load_image('character.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw((self.x+2) * 75 ,(self.y) * 67 + 75)
