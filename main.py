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
            elif event.key == SDLK_x: # 들고있는 음식 회전 시키기
                worker.rotate = True
            if worker.dir == 0: # 멈춰있을때
                if event.key == SDLK_LEFT:
                    if map.data[worker.y][worker.x - 1] == 0:
                        worker.dir = 1
                    elif map.data[worker.y][worker.x - 1] == 2:
                        #if worker.plate[0] == 
                        pass
                elif event.key == SDLK_RIGHT:
                    if map.data[worker.y][worker.x + 1] == 0:
                        worker.dir = 2
                    elif map.data[worker.y][worker.x + 1] == 9: #쓰레기통
                        if worker.plate[2] != 0:
                            worker.plate[2] = 0
                            point.trashcnt += 1
                elif event.key == SDLK_UP:
                    if map.data[worker.y + 1][worker.x] == 0:
                        worker.dir = 4
                elif event.key == SDLK_DOWN:
                    if map.data[worker.y - 1][worker.x] == 0:
                        worker.dir = 3
                #음식 제조 및 상호작용키
                elif event.key == SDLK_SPACE:
                    if worker.x == 6:
                        if worker.y >= 1 and worker.y <= 6:
                            worker.cook_type = map.data[worker.y][worker. x + 1] - 3
                        
def reset_world():
    global running
    global map
    global worker
    global world
    global point
    running = True
    world = []
    point = Point()
    map = Map()
    worker = Worker(map)
    world.append(map)
    world.append(worker)

def update_world():
    for o in world:
        o.update()
    

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
    delay(0.01)
# finalization code

close_canvas()