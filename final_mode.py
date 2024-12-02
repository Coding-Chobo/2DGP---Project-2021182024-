from pico2d import *
import play_mode
import pickle
import os
import game_framework

def init():
    global running
    global image
    global large_font
    global small_font
    global blink
    global time
    global point

    image = load_image('resource/tuk_credit.png')
    large_font = load_font('resource/Google.TTF', 24)
    small_font = load_font('resource/ENCR10B.TTF', 16)
    running = True
    blink = True
    time = 0
    point = play_mode.point

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
    clear_canvas()
    image.draw(400,400)
    for i in range(5):
        if i == 0 or i == 2:
            small_font.draw(200,450 - 50 * i,f'x {point.amount_sell[i]} = {point.amount_sell[i] * 2700}')
        else :
            small_font.draw(200,450 - 50 * i,f'x {point.amount_sell[i]} = {point.amount_sell[i] * 3200}')
    small_font.draw(200,250,f'x {point.trash} = {point.trash * 2000}')
    large_font.draw(200,200,f'{point.totalpoint}')
    large_font.draw(200,150,f'{point.guest_totalamount}')
    large_font.draw(200,100,f'{point.totalstatus}')

        # 랭킹 데이터를 파일에서 불러오고 정렬
    if os.path.exists('game.sav'):
        with open('game.sav', 'rb') as f:
            ranking = pickle.load(f)  # 저장된 점수 리스트
        ranking.sort(reverse=True)  # 내림차순 정렬

        # 랭킹 출력
        small_font.draw(500, 550, 'Rankings:', )
        for idx, score in enumerate(ranking[:5]):  # 상위 5개 점수 출력
            small_font.draw(500, 500 - idx * 20, f'{idx + 1}. {score}')
 
    if blink:
        large_font.draw(250,50,'Press Space for Next')
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
             match event.key:
                case pico2d.SDLK_SPACE:
                    play_mode.map.end = True
                    game_framework.pop_mode()
                    
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()