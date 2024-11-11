from pico2d import *
import main_play
import game_framework

def init():
    global running
    global image
    global logo_start_time

    image = load_image('tuk_credit.png')
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
        game_framework.change_mode(main_play)
        

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
