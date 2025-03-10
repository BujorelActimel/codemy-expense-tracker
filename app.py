import pgzrun
import json
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
# starea aplicatiei
current_screen = "main" # main sau add
input_amount = ""
input_description = ""
is_income = True

# elemente grafice
add_income_button = Rect((WIDTH//2 - 180, HEIGHT-80), (160, 50))
add_expense_button = Rect((WIDTH//2 + 20, HEIGHT-80), (160, 50))
back_button = Rect((20, 20), (100, 40))
save_button = Rect((WIDTH//2 -75, 340), (150, 50))
amount_input = Rect((WIDTH//2-150, 160), (300, 400))
description_input = Rect((WIDTH//2-150, 240), (300, 400))


def load_budget():
    global budget
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            budget = json.load(file)


def save_budget():
    with open("budget_data.json", "w") as file:
        json.dump(budget, file)


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

    save_budget()


def get_total_income():
    suma = 0
    for transaction in budget["transactions"]:
        if transaction["is_income"]:
            suma += transaction["amount"]
    return suma

def get_total_expenses():
    suma = 0
    for transaction in budget["transactions"]:
        if not transaction["is_income"]:
            suma += transaction["amount"]
    return suma


def draw():
    screen.fill(BACKGROUND)
    screen.draw.text("Buget Personal", center=(WIDTH//2, HEIGHT//2), fontsize=36, color=BLACK)


pgzrun.go()
load_budget()