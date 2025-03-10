import pgzrun
import os


# setari pentru window
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
WIDTH = 800
HEIGHT = 600
TITLE = "Buget Personal"


#             R     G    B
BACKGROUND = (245, 245, 245)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
PRIMARY = (65, 105, 225)
SUCCESS = (50, 205, 50)
DANGER = (220, 20, 60)
GRAY = (128, 128, 128)


budget = {
    "balance": 0,
    "transactions": []
}


def add_transaction(amount: int, description: str, is_income=True):
    transaction = {
        "amount": amount,
        "description": description,
        "is_income": is_income
    }

    budget["transactions"].append(transaction)

    if is_income:
        budget["balance"] += amount
    else:
        budget["balance"] -= amount


def draw():
    screen.fill(BACKGROUND)
    screen.draw.text("Buget Personal", center=(WIDTH//2, HEIGHT//2), fontsize=36, color=BLACK)

pgzrun.go()
