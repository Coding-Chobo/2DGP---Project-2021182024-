from pico2d import *
import play_mode
import game_framework

def init():
    global running
    global image
    global logo_start_time

    image = load_image('resource/tuk_credit.png')
    running = True
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global running
    global running
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(play_mode)
        

def draw():
    clear_canvas()
    image.draw(400,400)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
