from pico2d import *
import play_mode
import alba_mode
import game_framework

def init():
    global running
    global image
    global font
    global blink
    global time

    image = load_image('resource/how to play.png')
    font = load_font('resource/ENCR10B.TTF', 24)
    running = True
    blink = True
    time = 0

def finish():
    global image
    del image

def update():
    global running
    global blink
    global time
    if running:
        time = (time + game_framework.frame_time)
        if time > 0.5:
            time = 0
            blink = not blink

def draw():
    global blink
    clear_canvas()
    image.draw(400,400)
    if blink:
        font.draw(250,750,'Press Space for Next',(255,255,122))
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
             match event.key:
                case pico2d.SDLK_SPACE:
                    game_framework.change_mode(alba_mode)
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()                    