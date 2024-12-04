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
    global x

    image = load_image('resource/final_page.png')
    large_font = load_font('resource/Bold.TTF', 24)
    small_font = load_font('resource/Bold.TTF', 16)
    running = True
    blink = True
    time = 0
    x = 130
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
            small_font.draw(x,515 - 48 * i,f'x {point.amount_sell[i]} = {point.amount_sell[i] * 2700}')
        else :
            small_font.draw(x,515 - 48 * i,f'x {point.amount_sell[i]} = {point.amount_sell[i] * 3200}')
    small_font.draw(x ,275,f'x {point.trash} = -{point.trash * 2000}',(255,50,50))
    large_font.draw(x - 30 ,200,f'{point.food_money}')
    large_font.draw(x - 30,150,f'{point.guest_totalamount}')
    large_font.draw(x - 30,100,f'{point.totalstatus}')
    small_font.draw(x + 260,208,f'{point.food_money}')
    small_font.draw(x + 260,208 - 30,f'{point.totalstatus * 1000}')
    small_font.draw(x + 260,208 - 30 * 2,f'- {point.trash * 2000}', (255,50,50))
    small_font.draw(x + 260,208 - 30 * 3,f'-10000', (255,50,50))
    large_font.draw(x + 260,205 - 30 * 4,f'{point.totalpoint}')
    small_font.draw(x + 170, 118,'Worker')
    large_font.draw(x + 170, 85,'Total')

    # 랭킹 데이터를 파일에서 불러오고 정렬
    if os.path.exists('save/game.sav'):
        with open('save/game.sav', 'rb') as f:
            ranking = pickle.load(f)  # 저장된 점수 리스트
        

        # 랭킹 출력
        large_font.draw(405, 515, 'Ranking Top 5', )
        for idx, score in enumerate(ranking[:5]):  # 상위 5개 점수 출력
            small_font.draw(410, 468 - idx * 47.2, f'{idx + 1}         {score}')
 
    if blink:
        large_font.draw(250,30,'Press Space for New Game',(255,255,122))
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
             match event.key:
                case pico2d.SDLK_SPACE:
                    play_mode.map.end = True
                    game_framework.pop_mode()
                    
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()