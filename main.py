import sys
sys.path.append(r"C:\Users\dbdal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from pico2d import *
import random
from object_1 import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
def reset_world():
    global running
    global map
    global worker
    global world

    running = True
    world = []

    map = Map()
    worker = Worker()
    world.append(map)
    world.append(worker)

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas(800,717)

# initialization code
reset_world()
# game main loop code

while running :
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()