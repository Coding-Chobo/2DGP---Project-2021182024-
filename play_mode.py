import random

from pico2d import *
import game_framework

import game_world
import alba_mode
import howtoplay
import final_mode
from map import Map
from worker import Worker
from alba import Chunsik ,Ballon ,Girl
from point import Point

# boy = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN: 
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_x: # 들고있는 음식 회전 시키기
                worker.rotate = True
            if worker.dir == 0: # 멈춰있을때
                if event.key == SDLK_LEFT:
                    cell = map.data[7 - worker.y][worker.x - 1]
                    if isinstance(cell, tuple):
                        table_number = cell[1]
                        t = map.tables[table_number]
                        if t.is_active:
                            if t.check_order(worker.plate[0]):                          
                                worker.plate[0] = 0
                    else: 
                        if map.is_walkable(cell):
                            worker.dir = 1
                        #달봉이(배달부)에게 전달
                        if map.data[7 - worker.y][worker.x] == 10:
                            if type(map.alba) == Chunsik:
                                if map.alba.check_order(worker.plate[0]):
                                    worker.plate[0] = 0
                elif event.key == SDLK_RIGHT:
                    cell = map.data[7 - worker.y][worker.x + 1]
                    if isinstance(cell, tuple) and worker.making == False:
                        table_number = cell[1]
                        t = map.tables[table_number]
                        if t.is_active:
                            if t.check_order(worker.plate[2]):                               
                                worker.plate[2] = 0
                    else: 
                        if map.is_walkable(cell) and worker.making == False:
                            worker.dir = 2  
                        elif map.data[worker.y][worker.x + 1] == 9: #쓰레기통
                            if worker.plate[2] != 0:
                                worker.plate[2] = 0
                                point.trash += 1
                elif event.key == SDLK_UP:
                    cell  = map.data[(worker.y + 1)][worker.x]
                    if map.is_walkable(cell) and worker.making == False:
                        worker.dir = 4
                elif event.key == SDLK_DOWN:
                    cell  = map.data[(worker.y - 1)][worker.x]
                    if map.is_walkable(cell) and worker.making == False:
                        worker.dir = 3
                #음식 제조 및 상호작용키
                elif event.key == SDLK_SPACE:
                    if worker.x == 6:
                        if worker.y >= 1 and worker.y <= 6:
                            worker.cook_type = map.data[worker.y][worker. x + 1] - 3
                            if worker.cook_type % 2 == 0:
                                if worker.cook_step[worker.cook_type] < 5:
                                    worker.making = True
                            elif worker.cook_type != 5 : 
                                if worker.cook_step[worker.cook_type] < 4:
                                    worker.making = True

def init():
    global worker
    global map
    global point
    map = Map()
    game_world.add_object(map, 0)

    worker = Worker(map)
    game_world.add_object(worker, 1)

    point = Point()
    game_world.add_object(point, 1)
    game_framework.push_mode(howtoplay)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    if map.time_h == 13 and all(not o.is_active for o in map.tables):
        game_framework.push_mode(final_mode)
    game_world.handle_collisions()



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

