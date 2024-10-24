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
            if worker.dir == 0:
                if event.key == SDLK_LEFT:
                    if map.data[worker.y][worker.x - 1] == 0:
                        worker.dir = 1
                    elif map.data[worker.y][worker.x - 1] == 2:
                        #if worker.plate[0] == 
                        pass
                elif event.key == SDLK_RIGHT:
                    if map.data[worker.y][worker.x + 1] == 0:
                        worker.dir = 2
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
                            food = map.data[worker.y][worker.x+1]
                            if food == 3: #라면
                                if worker.cook_step[food -3] < 5:
                                    worker.cook_step[food -3] += 1
                                else:
                                   for i in range(4):
                                      if worker.plate[i] == 0:
                                        worker.plate[i] = food 
                                        break
                            elif food == 4: #순대
                                if worker.cook_step[food -3] < 4:
                                    worker.cook_step[food -3] += 1       
                                else:
                                   for i in range(4):
                                      if worker.plate[i] == 0:
                                        worker.plate[i] = food
                                        break                                              
                            elif food == 5: #김밥
                                if worker.cook_step[food -3] < 5:
                                    worker.cook_step[food -3] += 1
                                else:
                                   for i in range(4):
                                      if worker.plate[i] == 0:
                                        worker.plate[i] = food
                                        break                                 
                            elif food == 6: #떡볶이
                                if worker.cook_step[food -3] < 4:
                                    worker.cook_step[food -3] += 1       
                                else:
                                   for i in range(4):
                                      if worker.plate[i] == 0:
                                        worker.plate[i] = food        
                                        break
                            elif food == 7: #튀김
                                if worker.cook_step[food -3] < 5:
                                    worker.cook_step[food -3] += 1
                                else:
                                   for i in range(4):
                                      if worker.plate[i] == 0:
                                        worker.plate[i] = food
                                        break
                            elif food == 8: #물
                                for i in range(4):
                                    if worker.plate[i] == 0:
                                        worker.plate[i] = food
                                        break
                            
def reset_world():
    global running
    global map
    global worker
    global world
    global tables
    running = True
    world = []
    tables = [ Table() for n in range(6)]
    map = Map() 
    worker = Worker()
    world.append(map)
    world.append(worker)
    world += tables
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