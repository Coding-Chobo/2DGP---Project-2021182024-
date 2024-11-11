from pico2d import *
import game_world
import ball
import game_framework
import play_mode
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
                    play_mode.boy.set_item('Ballon')
                    game_framework.pop_mode()
                case pico2d.SDLK_1:
                    play_mode.boy.set_item('Girl')
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.set_item('ChunSik')
                    game_framework.pop_mode()
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()