from pico2d import *
import game_world
import game_framework
import play_mode
from alba import Background, Ballon, Girl, Chunsik
def init():
    global background
    global ballon
    global girl
    global chunsik
    background = Background()
    ballon = Ballon()
    girl = Girl()
    chunsik = Chunsik()

    chunsik.x ,chunsik.y = 150, 520
    ballon.x ,ballon.y = 410, 520
    girl.x ,girl.y = 650, 520    
    
    game_world.add_object(background,2)
    game_world.add_object(ballon,3)
    game_world.add_object(girl,3)
    game_world.add_object(chunsik,3)
    
def update():
    game_world.update()

def finish():
    game_world.remove_object(background)
    game_world.remove_object(ballon)
    game_world.remove_object(girl)
    game_world.remove_object(chunsik)

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
                    play_mode.map.set_alba('None')
                case pico2d.SDLK_1:
                    play_mode.map.set_alba('Ballon')
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.map.set_alba('Girl')
                    game_framework.pop_mode()
                case pico2d.SDLK_3:
                    play_mode.map.set_alba('ChunSik')
                    game_framework.pop_mode()
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()