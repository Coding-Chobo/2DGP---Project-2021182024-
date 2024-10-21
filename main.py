from pico2d import *
import random
from object_1 import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                if map.data[worker.y][worker.x - 1] == 0:
                    worker.x -= 1
            elif event.key == SDLK_RIGHT:
                if map.data[worker.y][worker.x + 1] == 0:
                    worker.x += 1
            elif event.key == SDLK_UP:
                if map.data[worker.y + 1][worker.x] == 0:
                    worker.y += 1
            elif event.key == SDLK_DOWN:
                if map.data[worker.y - 1][worker.x] == 0:
                    worker.y -= 1
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

open_canvas(800,800)

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