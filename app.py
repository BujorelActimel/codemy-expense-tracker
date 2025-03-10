import pgzrun
import os

# setari pentru window
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
WIDTH = 800
HEIGHT = 600
TITLE = "Buget Personal"

#             R     G    B
BACKGROUND = (245, 245, 245)
BLACK = (30, 30, 30)

def draw():
    screen.fill(BACKGROUND)
    screen.draw.text("Buget Personal", center=(WIDTH//2, HEIGHT//2), fontsize=36, color=BLACK)

pgzrun.go()