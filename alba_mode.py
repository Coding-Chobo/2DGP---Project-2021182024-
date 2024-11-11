from pico2d import *
import game_world
import game_framework
import main_play
from pannel import Pannel
def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel,3)
    
def update():
    pass

def finish():
    global pannel
    game_world.remove_object(pannel)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_mode()
                case pico2d.SDLK_0:
                    main_play.map.set_alba('None')
                case pico2d.SDLK_1:
                    main_play.map.set_alba('Ballon')
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    main_play.map.set_alba('Girl')
                    game_framework.pop_mode()
                case pico2d.SDLK_3:
                    main_play.map.set_alba('ChunSik')
                    game_framework.pop_mode()
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()