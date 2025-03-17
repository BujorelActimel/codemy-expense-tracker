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
current_screen = "add" # main sau add
input_amount = ""
input_description = ""
is_income = True

# elemente grafice
add_income_button = Rect((WIDTH//2 - 180, HEIGHT-80), (160, 50))
add_expense_button = Rect((WIDTH//2 + 20, HEIGHT-80), (160, 50))
back_button = Rect((20, 20), (100, 40))
save_button = Rect((WIDTH//2 -75, 340), (150, 50))
amount_input = Rect((WIDTH//2-150, 160), (300, 40))
description_input = Rect((WIDTH//2-150, 240), (300, 40))


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


def draw_main_screen():
    global budget
    # titlu
    screen.draw.text("Buget Personal", midtop=(WIDTH//2, 30), fontsize=36, color=BLACK)

    # balance card
    balance_card = Rect((WIDTH//2-150, 100), (300, 100))
    screen.draw.filled_rect(balance_card, WHITE)
    screen.draw.rect(balance_card, PRIMARY)

    balance_text = "Current Balance:"
    balance_amount = f'{budget["balance"]} Lei'

    screen.draw.text(balance_text, midtop=(balance_card.centerx, balance_card.top + 20), fontsize=24, color=BLACK)
    screen.draw.text(balance_amount, center=balance_card.center, fontsize=32, color=SUCCESS if budget["balance"] >= 0 else DANGER)

    # income si expense
    income_total = get_total_income()
    expense_total = get_total_expenses()

    income_card = Rect((WIDTH//4-100, 230), (200, 80))
    screen.draw.filled_rect(income_card, WHITE)
    screen.draw.rect(income_card, SUCCESS)
    screen.draw.text("Total income:", midtop=(income_card.centerx, income_card.top + 10), fontsize=20, color=BLACK)
    screen.draw.text(f"{income_total} Lei", center=income_card.center, fontsize=24, color=SUCCESS)

    expense_card = Rect((WIDTH*3//4-100, 230), (200, 80))
    screen.draw.filled_rect(expense_card, WHITE)
    screen.draw.rect(expense_card, DANGER)
    screen.draw.text("Total expenses:", midtop=(expense_card.centerx, expense_card.top + 10), fontsize=20, color=BLACK)
    screen.draw.text(f"{expense_total} Lei", center=expense_card.center, fontsize=24, color=DANGER)

    # lista de tranzactii
    draw_transaction_list()

    # butoane de adaugat
    screen.draw.filled_rect(add_income_button, SUCCESS)
    screen.draw.text("+ Add Income", center=add_income_button.center, fontsize=18, color=WHITE)

    screen.draw.filled_rect(add_expense_button, DANGER)
    screen.draw.text("+ Add Expense", center=add_expense_button.center, fontsize=18, color=WHITE)


def draw_transaction_list():
    screen.draw.text("Recent Transactions:", midtop=(WIDTH//2, 340), fontsize=24, color=BLACK)

    recent_transactions = budget["transactions"][-3:] if len(budget["transactions"]) >= 3 else budget["transactions"]
    

    if recent_transactions:
        y_pos = 380
        for transaction in reversed(recent_transactions):
            tx_rect = Rect((WIDTH//2-200, y_pos), (400, 40))
            screen.draw.filled_rect(tx_rect, WHITE)

            color = SUCCESS if transaction["is_income"] else DANGER
            prefix = "+" if transaction["is_income"] else "-"

            screen.draw.text(transaction["description"], midleft=(tx_rect.left + 10, tx_rect.centery), fontsize=18, color=BLACK)
            screen.draw.text(f"{prefix}{transaction['amount']} Lei", midright=(tx_rect.right-10, tx_rect.centery), fontsize=18, color=color)

            y_pos += 45
    else:
        screen.draw.text("No transactions. Add income or expenses.", center=(WIDTH//2, 410), fontsize=18, color=GRAY)


def draw_add_screen():
    # Titlu
    if is_income:
        title = "Adauga Venit"
        title_color = SUCCESS
    else:
        title = "Adauga Cheltuiala"
        title_color = DANGER

    # title = "Adauga Venit" if is_income else "Adauga Cheltuiala"
    # title_color = SUCCESS if is_income else DANGER

    screen.draw.text(title, midtop=(WIDTH//2, 30), fontsize=32, color=title_color)

    # Buton inapoi
    screen.draw.filled_rect(back_button, PRIMARY)
    screen.draw.text("Inapoi", center=back_button.center, fontsize=18, color=WHITE)

    # Formular
    # Camp suma
    screen.draw.text("Suma (Lei):", midtop=(WIDTH//2, 130), fontsize=20, color=BLACK)
    screen.draw.filled_rect(amount_input, WHITE)
    screen.draw.rect(amount_input, BLACK)
    screen.draw.text(input_amount, midleft=(amount_input.left+10, amount_input.centery), fontsize=20, color=BLACK)


    # Camp descrierea
    screen.draw.text("Descriere:", midtop=(WIDTH//2, 210), fontsize=20, color=BLACK)
    screen.draw.filled_rect(description_input, WHITE)
    screen.draw.rect(description_input, BLACK)
    screen.draw.text(input_description, midleft=(description_input.left+10, description_input.centery), fontsize=20, color=BLACK)


    # Buton salvare
    screen.draw.filled_rect(save_button, title_color)
    screen.draw.text("Salveaza", center=save_button.center, fontsize=20, color=WHITE)



def draw():
    screen.fill(BACKGROUND)

    if current_screen == "main":
        draw_main_screen()
    else:
        draw_add_screen()


load_budget()
pgzrun.go()