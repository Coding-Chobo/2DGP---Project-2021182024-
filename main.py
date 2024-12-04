from pico2d import open_canvas, delay, close_canvas
import game_framework

import logo_mode as start_mode
  
open_canvas(800, 800)
game_framework.run(start_mode)
close_canvas() 