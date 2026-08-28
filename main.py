import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines ot bet on (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? Rs.")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} and Rs.{MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def spins(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money to bet, your current balance is " + str(balance))
        else:
            break

    print(f"You are betting Rs.{bet} on {lines}. Total bet is equal to Rs.{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won Rs.{winnings} on {lines}.")
    print(f"You won on line:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: Rs.{balance}")
        answer = input("Press enter to play (q to quit):")
        if answer == "q":
            break
        else:
            balance += spins(balance)

    print(f"Current balance: Rs.{balance}")


main()
